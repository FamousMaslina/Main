import numpy as np

# Load the trained agent.
agent = CURLBeamNGDriveAgent.load("trained_agent.pkl")

# Initialize the environment.
env = BeamNGDriveEnv(scenario_path="path/to/scenario.xml")

# Evaluate the agent.
total_reward = 0
for i in range(100):
    episode_reward = 0
    state = env.reset()
    while True:
        action = agent.select_action(state)
        next_state, reward, done, info = env.step(action)

        episode_reward += reward
        state = next_state

        if done:
            break

    total_reward += episode_reward

# Print the average episode reward.
print("Average episode reward:", total_reward / 100)
