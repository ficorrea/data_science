import pandas as pd
import numpy as np
from scipy import stats

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")

# Cálculo de média e variância
def calc_u_sigma(clicks, visitas):
    u, var = stats.beta.stats(a=1 + clicks, b=1 + (visitas - clicks), moments='mv')
    return u, np.sqrt(var)

# Amostras da Normal dist 
def get_sample(u, sigma, N):
    return np.random.normal(loc=u, scale=1.25*sigma, size=N)

# Cálculo Beta dist
def calc_beta(x, clicks, visitas):
    return stats.beta.pdf(x, a=1 + clicks, b=1 + (visitas - clicks))

# Cálculo Normal (N) dist
def calc_n(x, u, sigma):
    return stats.norm.pdf(x, loc=u, scale=1.25*sigma)

# Cálculo de risco esperado
# O risco de escolher uma determinada página
def calc_expected_loss(x1, x2, y, N):
    return (1/N) * np.sum(((x1 - x2)*y)[x1 >= x2])

def get_cumsum(df, field):
    return df[field].cumsum()

# Cálculo da probabilidade de B melhor que A
def calc_probabilidade(clicks_a, visitas_a, clicks_b, visitas_b, N, loss=None):
    u_a, sigma_a = calc_u_sigma(clicks_a, visitas_a)
    u_b, sigma_b = calc_u_sigma(clicks_b, visitas_b)
    
    x_a = get_sample(u_a, sigma_a, N)
    x_b = get_sample(u_b, sigma_b, N)
    
    beta_a = calc_beta(x_a, clicks_a, visitas_a)
    beta_b = calc_beta(x_b, clicks_b, visitas_b)
    
    norm_a = calc_n(x_a, u_a, sigma_a)
    norm_b = calc_n(x_b, u_b, sigma_b)
    
    # Beta / Normal
    y = (beta_a * beta_b) / (norm_a * norm_b)
    
    # Somente onde B > A
    yb = y[x_b >= x_a]    
    
    # Probabilidade de B ser melhor que A
    p = (1 / N) * np.sum(yb)

    # Erro ao assumir B melhor que A
    if loss == 'A':
        return calc_expected_loss(x_b, x_a, y, N)
    elif loss == 'B':
        return calc_expected_loss(x_a, x_b, y, N)
    else:
        return p

def animate(i):
    df = pd.read_csv('data_experiment.csv')
    df = df.reset_index().rename(columns={'index': 'day'})

    # Pivot
    df = df.pivot(index='day', columns='group', values=['click', 'visit']).fillna(0)
    df.columns = ['click_control', 'click_treatment', 'visit_control', 'visit_treatment']
    df = df[['click_control', 'visit_control', 'click_treatment', 'visit_treatment']].reset_index(drop=True)
    
    # Rename
    rename = {'click_control': 'clicks_a', 
            'visit_control': 'visitas_a', 
            'click_treatment': 'clicks_b', 
            'visit_treatment': 'visitas_b'}
    df = df.rename(columns=rename)
    
    # Acc
    df['acc_clicks_a'] = get_cumsum(df, 'clicks_a')
    df['acc_visitas_a'] = get_cumsum(df, 'visitas_a')
    df['acc_clicks_b'] = get_cumsum(df, 'clicks_b')
    df['acc_visitas_b'] = get_cumsum(df, 'visitas_b')

    # Samples
    N = 1000

    # Get metrics
    df['probabilidade_b_bt_a'] = df.apply(lambda x: calc_probabilidade(x['acc_clicks_a'], x['acc_visitas_a'], x['acc_clicks_b'], x['acc_visitas_b'], N), axis=1)
    df['expected_loss_a'] = df.apply(lambda x: calc_probabilidade(x['acc_clicks_a'], x['acc_visitas_a'], x['acc_clicks_b'], x['acc_visitas_b'], N, loss='A'), axis=1)
    df['expected_loss_b'] = df.apply(lambda x: calc_probabilidade(x['acc_clicks_a'], x['acc_visitas_a'], x['acc_clicks_b'], x['acc_visitas_b'], N, loss='B'), axis=1)

    # X axis
    x = np.arange(df.shape[0])

    # Plot
    plt.cla()
    plt.plot(x, df['probabilidade_b_bt_a'], label='Probability B better A')
    plt.plot(x, df['expected_loss_a'], label='Risk chossing A')
    plt.plot(x, df['expected_loss_b'], label='Risk chossing B')
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()