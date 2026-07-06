import pygame

from drone import Drone
from physics import update_drone
from controller import PIDController
from visualizer import draw_drone, WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Flight Controller Simulator")

clock = pygame.time.Clock()

drone = Drone()

pid = PIDController(
    kp=2.0,
    ki=0.1,
    kd=1.0
)

target_altitude = 10.0
dt = 0.1

frame = 0

running = True

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Increase target altitude
            if event.key == pygame.K_UP:
                target_altitude += 0.2

            # Decrease target altitude
            if event.key == pygame.K_DOWN:
                target_altitude = max(0, target_altitude - 0.2)

    # Smooth horizontal movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        drone.x -= 5

    if keys[pygame.K_RIGHT]:
        drone.x += 5

    # Keep drone inside the screen
    drone.x = max(20, min(drone.x, WIDTH - 60))

    # PID control
    control = pid.compute(
        target_altitude,
        drone.altitude,
        dt
    )

    thrust = drone.mass * 9.81 + control

    update_drone(drone, thrust, dt)

    # Draw everything
    draw_drone(
        screen,
        drone.x,
        drone.altitude,
        target_altitude,
        frame
    )

    frame += 1

    clock.tick(60)

pygame.quit()