# from stable_baselines3 import PPO
# import gymnasium as gym
# import torch

# # Confirma se há CUDA disponível
# print("CUDA disponível?", torch.cuda.is_available())

# # Cria o ambiente
# env = gym.make("CartPole-v1")

# # Treina o agente usando CUDA (caso disponível)
# model = PPO("MlpPolicy", env, verbose=1, device="cuda" if torch.cuda.is_available() else "cpu")

# model.learn(total_timesteps=100_000)
import torch
print(torch.version.cuda)           # deve mostrar algo como '11.8'
print(torch.cuda.is_available())    # deve retornar True
print(torch.cuda.current_device())  # deve retornar 0
print(torch.cuda.get_device_name(0))  # deve retornar o nome da GPU