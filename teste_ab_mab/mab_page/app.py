from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import numpy as np

from random import random

app = Flask(__name__)

VISIT = int(1)
CONTROL = 'control'
TREATMENT = 'treatment'

def treatment_data(df, field):
    data = df.groupby(field).sum().reset_index()[['click', 'no_click']].T
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

def mab(success, failure):
    '''Thompson Agent'''
    prob_reward = np.random.beta(success, failure)
    return np.argmax(prob_reward)

@app.route('/home')
def index():
    df = pd.read_csv('data_experiment.csv')
    df['no_click'] = df.apply(lambda x: x['visit'] - x['click'], axis=1)
    success, failure = treatment_data(df, 'group')
    
    bandit = mab(success, failure)
    
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