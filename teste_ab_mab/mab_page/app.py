from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np

app = Flask(__name__)

VISIT = int(1)
CONTROL = 'control'
TREATMENT = 'treatment'

def treatment_data(df, group_field, comparison_fields=[None, None]):
    data = (
        df
        .groupby(group_field)
        .sum()
        .reset_index()[comparison_fields]
        .T)
    data = data.to_numpy()
    return data[0], data[1]

def fill_csv(data):
    df_main = pd.read_csv('data_experiment.csv')
    df_event = pd.DataFrame(data, index=[0])

    # Parse
    df_event['click'] = df_event['click'].astype(int)
    df_event['visit'] = df_event['visit'].astype(int) 

    df = pd.concat([df_main, df_event])
    df.to_csv('data_experiment.csv', index=False, encoding='utf8')

def save_proportion_data(data):
    with open('data.txt', 'a+') as file:
        file.writelines(f'{data}\n')

def thompson_mab(success, failure):
    '''Thompson Agent'''
    prob_reward = np.random.beta(success, failure)
    return np.argmax(prob_reward)

def greedy_mab(clicks, visits):
    '''Greedy Agent'''
    proportion = clicks / visits
    save_proportion_data(proportion)
    if len(set(proportion)) != 1:
        return np.argmax(proportion)
    else:
        return np.random.randint(low=0, high=2, size=1)[0]

def calc_linear_decay(r, x):
    return 1 * (1 - r)**x
    
def calc_exp_decay(k, t):
    return 1 * np.exp(-k*t)
    
def epsilon_greedy_mab(epsilon, clicks, visits):
    if epsilon >= 0.5:
        return np.random.randint(low=0, high=2, size=1)[0]
    else:
        return greedy_mab(clicks, visits)

@app.route('/home')
def index():
    df = pd.read_csv('data_experiment.csv')
    df['no_click'] = df.apply(lambda x: x['visit'] - x['click'], axis=1)

    # Greedy MAB
    # clicks, visits = treatment_data(df, 'group', ['click', 'visit'])
    # bandit = greedy_mab(clicks, visits)

    # Epsilon Greedy MAB
    decay = 0.7
    epsilon = calc_exp_decay(decay, df.shape[0])
    clicks, visits = treatment_data(df, 'group', ['click', 'visit'])
    bandit = epsilon_greedy_mab(epsilon, clicks, visits)

    # # Thompson MAB
    # success, failure = treatment_data(df, 'group', ['click', 'no_click'])
    # bandit = thompson_mab(success, failure)
    
    if not bandit:
        return render_template('page_layout_blue.html')
    else:
        return render_template('page_layout_red.html')

@app.route('/yes', methods=['POST'])
def yes_event():
    if request.form['yescheckbox'] == 'red':
        data = {'click': 1, 'visit': VISIT, 'group': TREATMENT}
        fill_csv(data)
    else:
        data = {'click': 1, 'visit': VISIT, 'group': CONTROL}
        fill_csv(data)
    return redirect(url_for('index'))

@app.route('/no', methods=['POST'])
def no_event():
    if request.form['nocheckbox'] == 'red':
        data = {'click': 0, 'visit': VISIT, 'group': TREATMENT}
        fill_csv(data)
    else:
        data = {'click': 0, 'visit': VISIT, 'group': CONTROL}
        fill_csv(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()