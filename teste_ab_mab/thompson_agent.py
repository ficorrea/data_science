import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# criação do agente
class ThompsonAgent():
    def __init__(self, prob_list):
        self.prob_list = prob_list
    
    def __name__(self):
        return 'ThompsonAgent'
    
    def pull(self, bandit_machine):
        if random.random() < self.prob_list[bandit_machine]:
            return 1
        else:
            return 0
    
    def choose_best_machine(self, success, failure):
            probs = np.random.beta(success, failure)
            return np.argmax(probs) 
    
    def reward_plot(self, success, failure):
            linestyle = ['-', '--']
            x = np.linspace(0, 1, 1002)[1:-1]
            plt.clf()
            plt.xlim(0, 1.0)
            plt.ylim(0, 30)
            for a, b, ls in zip(success, failure, linestyle):
                dist = beta(a, b)
                plt.plot(x, dist.pdf(x), ls=ls, c='black', label=f'Alpha: {a} Beta: {b}')
                plt.draw()
                plt.pause(0.001)
                plt.legend(loc=0)
    
    def print_final_metrics(self, probs_machines, avg_accumulated_reward):
        print('Final metric')
        for i in range(len(probs_machines)):
            print(f'Prob machine {i}: {probs_machines[i]}%')
        print(f'Avg accumulated reward {avg_accumulated_reward}\n')
    
    def run(self):
        # parâmetros do modelo
        trials = 1000 # -> quantidade de escolhas feitas pelas pessoas
        episodes = 200 # -> "tempo" até a avaliação das tentativas
        first_trial_print = 0 # -> printa o primeiro trial
        first_episode_print = 0 # -> printa o primeiro episode
        plot_reward = 0 # -> printa o gráfico de distribuição

        # definição do agente
        # self.prob_list = [0.25, 0.80]
        # bandit = ThompsonAgent(self.prob_list)

        # métricas
        prob_reward = np.zeros(len(self.prob_list))
        prob_machine_0 = 0
        prob_machine_1 = 0
        acummulated_reward_array = []
        avg_acummulated_reward_array = []

        for episode in range(episodes):
            success = np.ones(len(self.prob_list))
            failure = np.full(len(self.prob_list), 1e-5)
            reward_machine = np.zeros(len(self.prob_list))
            bandit_choose = np.full(len(self.prob_list), 1e-5)
            accumulated_reward = 0

            for trial in range(trials):
                # escolha do melhor bandit
                bandit_machine = self.choose_best_machine(success, failure)
                
                # recompensa do agente
                reward = self.pull(bandit_machine)
                
                # incrementando dados de sucesso e falha 
                # para distribuição beta
                if reward:
                    success[bandit_machine] += 1
                else:
                    failure[bandit_machine] += 1
                
                # plot
                if plot_reward:
                    self.eward_plot(success, failure)
                
                # guarda recompensa para avaliação
                reward_machine[bandit_machine] += reward # -> soma do reward de cada máquina
                bandit_choose[bandit_machine] += 1 # -> quantidade de vezes que a máquina foi escolhida
                accumulated_reward += reward # -> total acumulado de reward por trial

        
            # cálculo das métricas do episode
            prob_reward += reward_machine / bandit_choose
            acummulated_reward_array.append(accumulated_reward)
            avg_acummulated_reward_array.append(np.mean(accumulated_reward))
            
        # cálculo métricas do experimento
        probs_machines = [prob_reward[i] / episodes * 100 for i in range(len(self.prob_list))]
        avg_accumulated_reward = np.mean(avg_acummulated_reward_array)
        # self.print_final_metrics(probs_machines, avg_accumulated_reward)
        
        return probs_machines, avg_accumulated_reward