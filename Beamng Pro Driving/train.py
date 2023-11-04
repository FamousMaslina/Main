import stable_baselines3 as sb3
from curl_rl.env_wrappers import BeamNGDriveEnv

# Create a BeamNGDrive environment.
env = BeamNGDriveEnv(scenario_path="path/to/scenario.xml")

# Initialize the agent.
agent = CURLBeamNGDriveAgent(env.observation_space, env.action_space)

# Train the agent.
model = sb3.PPO(agent, env)
model.learn(total_timesteps=1000000)

# Save the trained agent.
agent.save("trained_agent.pkl")
