import random
import numpy as np

# criação do agente
class GreedyAgent():
    def __init__(self, prob_list):
        self.prob_list = prob_list
    
    def __name__(self):
        return 'GreedyAgent'
    
    def pull(self, bandit_machine):
        if random.random() < self.prob_list[bandit_machine]:
            return 1
        else:
            return 0
    
    # função para escolha do melhor bandit
    def choose_best_machine(self):
        total_trials = 0
        while 1:
            rewards = np.array([self.pull(i) for i in range(len(self.prob_list))])
            bandits = [1 for i in range(len(self.prob_list))]
            probs = rewards / bandits
            total_trials += len(self.prob_list)
            if np.count_nonzero(probs == 1) == 1:
                max_prob = np.where(probs == np.max(probs))[0]
                return total_trials, max_prob[0]
    
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
        eps_init = 1

        # métricas
        prob_reward = np.zeros(len(self.prob_list))
        prob_machine_0 = 0
        prob_machine_1 = 0
        acummulated_reward_array = []
        avg_acummulated_reward_array = []
  

        for episode in range(episodes):
            reward_machine = np.zeros(len(self.prob_list))
            bandit_choose = np.full(len(self.prob_list), 1e-5)
            accumulated_reward = 0
            
            if eps_init:
                total_trials, bandit_machine = self.choose_best_machine()
                # print(f'Total users used to get best machine: {total_trials}\n')
                eps_init = 0
            
            for trial in range(trials - total_trials):
                
                # recompensa do agente
                reward = self.pull(bandit_machine)
                total_trials = 0
                
                # guarda recompensa para avaliação
                reward_machine[bandit_machine] += reward # -> soma do reward de cada máquina 
                bandit_choose[bandit_machine] += 1 # -> quantidade de vezes que a máquina foi escolhida
                accumulated_reward += reward # -> total acumulado de reward por trial
            
            # print first trial
            if first_trial_print:
                print('First trial')
                print(f'Reward machine: {reward_machine}')
                print(f'Machine choosen: {bandit_choose}')
                print(f'Acc reward trial: {accumulated_reward}\n')
                first_trial_print = 0
            
            # cálculo das métricas do episode
            prob_reward += reward_machine / bandit_choose
            acummulated_reward_array.append(accumulated_reward)
            avg_acummulated_reward_array.append(np.mean(accumulated_reward))
            
            # print first episode
            if first_episode_print:
                print('First episode')
                print(f'Prob reward episode: {prob_reward}')
                print(f'Acc reward episode: {acummulated_reward_array}')
                print(f'Avg acc reward episode: {avg_acummulated_reward_array}\n')
                first_episode_print = 0

        # cálculo métricas do experimento
        probs_machines = [prob_reward[i] / episodes * 100 for i in range(len(self.prob_list))]
        avg_accumulated_reward = np.mean(avg_acummulated_reward_array)
        # self.print_final_metrics(probs_machines, avg_accumulated_reward)

        return probs_machines, avg_accumulated_reward