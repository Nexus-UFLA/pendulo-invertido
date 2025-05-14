import gymnasium as gym
from stable_baselines3 import SAC
import torch


# ambiente contínuo, renderização “human”
env = gym.make("InvertedPendulum-v5", render_mode="human")

# SAC (ação contínua) é adequado para Box(-?)→torque
model = SAC("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=200_000)

# avaliação
obs, info = env.reset(seed=0)
for _ in range(500):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    if done or truncated:
        obs, info = env.reset()
env.close()

from stable_baselines3 import PPO
model = PPO("MlpPolicy", env, verbose=1, device="cuda" if torch.cuda.is_available() else "cpu")
model.learn(total_timesteps=200_000)
