#Implementing Prisoner Dilemma as a gym environment
import gym

class PrisonerEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = gym.spaces.Discrete(2)
        #Action Space 
        #0:Confessed 
        #1:Did not Confess
        self.observation_space = gym.spaces.Discrete(1)
        #Observation Space
        #There is only one state
        self.state = 0
        self.done = False
        self.reward = 0

    def step(self, action):
        if self.done:
            raise Exception("Episode is done")
        if action[0]==0:
            if action[1]==0:
                self.reward = -3 
                #Both players get a punishment of 3 years if both confess
            else:
                self.reward = 0
                #If other player does not confess while you confess, you are set free
        else:
            if action[1]==0:
                self.reward = -7
                #If other player confesses while you do not, you get a punishment of 7 years
            else:
                self.reward = -1
                #If both players do not confess, both get a punishment of 1 year
        self.done = True
        return self.state, self.reward, self.done, {}
    
    def reset(self):
        self.state = 0
        self.done = False
        self.reward = 0
        return self.state
