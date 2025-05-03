import pygame
import numpy as np
import matplotlib.pyplot as plt

# Inicialização
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Parâmetros físicos
g = 9.81
l = 150              # comprimento do pêndulo (px)
m = 1.0
dt = 0.02
cart_speed = 5
torque_mag = 15
b = 0.1            # atrito do pêndulo

# Estado inicial
theta_0 = 0  # ângulo inicial em graus
theta = np.radians(theta_0)
omega = 0.0
cart_x = width // 2

# Gráfico ao vivo
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], label="θ (graus)")
ax.set_xlim(0, 10)
ax.set_ylim(0, 2 * np.pi)
ax.set_title("Simulação do Pêndulo Invertido")
ax.set_ylabel("Ângulo (rad)")
ax.set_xlabel("Tempo (s)")
ax.grid()
ax.legend()

# Dados para plot
theta_list = []
time_list = []
t = 0
frame = 0

running = True
while running:
    torque = 0.0
    move_cart = 0.0
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        torque = -torque_mag
        move_cart = -cart_speed
    if keys[pygame.K_RIGHT]:
        torque = torque_mag
        move_cart = cart_speed

    # Atualizar física do pêndulo
    alpha = (g / (l / 100)) * np.sin(theta) + torque / m + b * omega
    omega -= alpha * dt
    theta = theta % (2 * np.pi)
    theta += omega * dt

    # Atualizar posição do carrinho
    cart_x += move_cart
    cart_x = max(50, min(width - 50, cart_x))

    # Calcular posição da ponta do pêndulo
    pivot = (cart_x, height // 3)
    x = pivot[0] + l * np.sin(theta)
    y = pivot[1] + l * np.cos(theta)

    # Desenho
    screen.fill((30, 30, 30))
    cart_width = 80
    cart_height = 20
    pygame.draw.rect(screen, (180, 180, 180), (cart_x - cart_width//2, pivot[1], cart_width, cart_height))
    pygame.draw.line(screen, (200, 200, 200), pivot, (x, y), 5)
    pygame.draw.circle(screen, (255, 100, 100), (int(x), int(y)), 12)
    pygame.display.flip()
    clock.tick(60)

    # Atualizar dados
    theta_list.append((theta))
    time_list.append(t)
    t += dt

    # Atualizar gráfico a cada 5 frames
    if frame % 5 == 0:
        line.set_data(time_list, theta_list)
        ax.set_xlim(max(0, t - 10), t + 1)
        ax.figure.canvas.draw()
        ax.figure.canvas.flush_events()

pygame.quit()

# Exibir gráfico final
plt.ioff()
plt.show()
