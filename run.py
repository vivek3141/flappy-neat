import gym, gym_ple
import time
env = gym.make("FlappyBird-v0")
env.reset()
for i in range(100):
    env.render()
    reward = env.step(env.action_space.sample())
env.close()
