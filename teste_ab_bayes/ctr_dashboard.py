import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")

def get_ctr(df, group):
    data = (
        df.loc[df.group == group, 'click'].cumsum() /
        df.loc[df.group == group, 'visit'].cumsum())
    return data

def get_x_size(df, group):
    return np.arange(len(df[df.group == group]))

def animate(i):
    df = pd.read_csv('data_experiment.csv')
    
    # Control
    CTR_GROUP = 'control'
    cx = get_x_size(df, CTR_GROUP)
    cy = get_ctr(df, CTR_GROUP)

    # Control
    CTR_TREAT = 'treatment'
    tx = get_x_size(df, CTR_TREAT)
    ty = get_ctr(df, CTR_TREAT)

    # Plot
    plt.cla()
    plt.plot(cx, cy, label=str.upper(CTR_GROUP))
    plt.plot(tx, ty, label=str.upper(CTR_TREAT))
    plt.legend(loc='upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()