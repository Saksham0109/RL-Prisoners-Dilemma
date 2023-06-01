#Implementing Q-Learning Algorithm for the Prisoner Dilemma environment
import numpy as np

class QLearning():
    def __init__(self, env1,env2, alpha=0.1,epsilon=0.1):
        self.env1 = env1
        self.env2 = env2
        self.alpha = alpha
        #No gamma as it is single state environment
        self.epsilon = epsilon
        self.Q = np.zeros((self.env1.observation_space.n, self.env1.action_space.n))
        self.Q2 = np.zeros((self.env2.observation_space.n, self.env2.action_space.n))

    def train(self, num_episodes=1000):
        for episode in range(num_episodes):
            #Setting the initial state
            state = self.env1.reset()
            state2=self.env2.reset()
            #Getting the action for both agents
            if np.random.random() < self.epsilon:
                action1 = self.env1.action_space.sample()
            else:
                action1 = np.argmax(self.Q[state])
            if np.random.random() < self.epsilon:
                action2 = self.env2.action_space.sample()
            else:
                action2 = np.argmax(self.Q2[state])
            #Taking the action and getting the reward
            next_state, reward, done, _ = self.env1.step([action1,action2])
            next_state2,reward2,done2,_ = self.env2.step([action2,action1])
            self.Q[state, action1] += (self.alpha *(reward-self.Q[state, action1]))
            self.Q2[state2, action2] += (self.alpha *(reward2-self.Q2[state2, action2]))
            state = next_state
            state2 = next_state2