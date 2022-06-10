import gym

env =gym.make("FrozenLake-v1")
env.reset()
env.render()
env.close()
