import numpy as np
import random

class MDP:
    def __init__(self):
        self.states = ['s1', 's2']
        self.actions = ['a1', 'a2']
        self.transition_model = {
            ('s1', 'a1'): {'s1': 0.8, 's2': 0.2},
            ('s1', 'a2'): {'s1': 0.8, 's2': 0.2},
            ('s2', 'a1'): {'s1': 0.2, 's2': 0.8},
            ('s2', 'a2'): {'s1': 0.2, 's2': 0.8}
        }
        self.reward = {
            ('s1', 'a1'): 10,
            ('s1', 'a2'): 5,
            ('s2', 'a1'): 2,
            ('s2', 'a2'): 1
        }
        self.discount = 0.9
            
    def array_diff(self, array1, array2):
        return np.sum(np.abs(np.array(list(array1.values())) - np.array(list(array2.values()))))
        
    def value_iteration(self):
        # Initialize value function
        V = {state: 0 for state in self.states}
        
        # Loop until convergence 
        while True:  
            new_V = V.copy()
            for state in self.states:
                all_Qs = []
                for action in self.actions:
                    weighted_sum = 0
                    for next_state, prob in self.transition_model[(state, action)].items():
                        weighted_sum += prob * V[next_state]
                    Q = self.reward[(state, action)] + self.discount * weighted_sum
                    all_Qs.append(Q)
                    
                new_V[state] = max(all_Qs)

            print(self.array_diff(V, new_V))
            
            if self.array_diff(V, new_V) < 1e-6:
                break
            V = new_V
        return V
    
    
    def epsilon_greedy_action_selection(self, state, Q, epsilon=0.2):
        if np.random.rand() < epsilon:
            # exploration: select a random action
            return random.choice(self.actions)
        else:
            # Exploitation: select the action with the highest Q value
            q_values = {action: Q[(state, action)] for action in self.actions}
            return max(q_values, key=q_values.get)
            
    
    def q_learning(self, lr=0.1):
        # Initialize Q function and the state
        Q = {(state, action): 0 for action in self.actions for state in self.states}
        s = 's1'
        
        # note this is different from the self.transition model above, imagine this is how the interaction
        # will happen in a real world. Here we have to give it a simulated world.
        transition_prob = {
            ('s1', 'a1'): {'s1': 0.8, 's2': 0.2},
            ('s1', 'a2'): {'s1': 0.8, 's2': 0.2},
            ('s2', 'a1'): {'s1': 0.2, 's2': 0.8},
            ('s2', 'a2'): {'s1': 0.2, 's2': 0.8}
        }
        
        # Loop until convergence 
        while True:
            Q_old = Q.copy()
            a = self.epsilon_greedy_action_selection(s, Q)
            r = self.reward[(s, a)]
            # this new state is obtained by actually interacting with the real world
            prob = transition_prob[(s, a)]
            s_new = np.random.choice(a=list(prob.keys()), p=list(prob.values()))
            
            all_action_values = [Q[(s_new, a_new)] for a_new in self.actions]

            Q[(s, a)] += lr * (r + self.discount * max(all_action_values) - Q[(s, a)])
            
            if self.array_diff(Q_old, Q) < 1e-4:
                break
            
            s = s_new
            
        return Q
        
                    
mdp = MDP()
print("Value iteration: ", mdp.value_iteration(), "\n")
print("Q Learning     : ", mdp.q_learning())

