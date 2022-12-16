from flask import Flask, render_template, redirect, url_for
from random import random
import pandas as pd

app = Flask(__name__)

GROUP = 'control'
VISIT = int(1)

def fill_csv(data):
    df_main = pd.read_csv('data_experiment.csv')
    df_event = pd.DataFrame(data, index=[0])

    # Parse
    df_event['click'] = df_event['click'].astype(int)
    df_event['visit'] = df_event['visit'].astype(int) 

    df = pd.concat([df_main, df_event])
    df.to_csv('data_experiment.csv', index=False, encoding='utf8')

@app.route('/home')
def index():
    return render_template('page_layout_blue.html')

@app.route('/yes', methods=['POST'])
def yes_event():
    data = {'click': 1, 'visit': VISIT, 'group': GROUP}
    fill_csv(data)
    return redirect(url_for('index'))

@app.route('/no', methods=['POST'])
def no_event():
    data = {'click': 0, 'visit': VISIT, 'group': GROUP}
    fill_csv(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000)