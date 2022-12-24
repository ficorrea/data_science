from random_agent import RandomAgent
from omniscient_agent import OmniscientAgent
from greedy_agent import GreedyAgent
from epsilon_greed_agent import EpsilonGreedyAgent
from thompson_agent import ThompsonAgent

import numpy as np

prob_list = [.25, .80]

ra_probs_metrics, om_probs_metrics , gr_probs_metrics, epg_probs_metrics, tp_probs_metrics = [], [], [], [], []
ra_rwd_metrics, om_rwd_metrics , gr_rwd_metrics, epg_rwd_metrics, tp_rwd_metrics = [], [], [], [], []

for i in range(5):
    ra = RandomAgent(prob_list)
    ra_probs, ra_acc_rwd = ra.run()
    ra_probs_metrics.append(ra_probs)
    ra_rwd_metrics.append(ra_acc_rwd)

    om = OmniscientAgent(prob_list)
    om_probs, om_acc_rwd = om.run()
    om_probs_metrics.append(om_probs)
    om_rwd_metrics.append(om_acc_rwd)

    gr = GreedyAgent(prob_list)
    gr_probs, gr_acc_rwd = gr.run()
    gr_probs_metrics.append(gr_probs)
    gr_rwd_metrics.append(gr_acc_rwd)

    epg = EpsilonGreedyAgent(prob_list)
    epg_probs, epg_acc_rwd = epg.run()
    epg_probs_metrics.append(epg_probs)
    epg_rwd_metrics.append(epg_acc_rwd)

    tp = ThompsonAgent(prob_list)
    tp_probs, tp_acc_rwd = tp.run()
    tp_probs_metrics.append(tp_probs)
    tp_rwd_metrics.append(tp_acc_rwd)

def print_metrics(probs, rwd, agent):
    print(f'{agent}: {np.average(probs, axis=0)} -- {agent}: {np.mean(rwd)}')

print_metrics(ra_probs_metrics, ra_rwd_metrics, ra.__name__())
print_metrics(om_probs_metrics, om_rwd_metrics, om.__name__())
print_metrics(gr_probs_metrics, gr_rwd_metrics, gr.__name__())
print_metrics(epg_probs_metrics, epg_rwd_metrics, epg.__name__())
print_metrics(tp_probs_metrics, tp_rwd_metrics, tp.__name__())