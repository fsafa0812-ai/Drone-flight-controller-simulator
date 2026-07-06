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
battery = 100.0
flight_mode = "HOVER"

running = True

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                target_altitude += 0.2

            if event.key == pygame.K_DOWN:
                target_altitude = max(0, target_altitude - 0.2)

    # Smooth horizontal movement
    keys = pygame.key.get_pressed()

    acceleration = 0.4
    friction = 0.90

    if keys[pygame.K_LEFT]:
        drone.x_velocity -= acceleration

    if keys[pygame.K_RIGHT]:
        drone.x_velocity += acceleration

    drone.velocity *= friction
    drone.x += drone.x_velocity

    # Keep drone inside screen
    if drone.x < 20:
        drone.x = 20
        drone.x_velocity = 0

    if drone.x > WIDTH - 60:
        drone.x = WIDTH - 60
        drone.x_velocity = 0

    # PID altitude control
    control = pid.compute(
        target_altitude,
        drone.altitude,
        dt
    )

    thrust = drone.mass * 9.81 + control

    update_drone(drone, thrust, dt)

    # Flight mode
    difference = target_altitude - drone.altitude

    if abs(difference) <= 0.2:
        flight_mode = "HOVER"
    elif difference > 0:
        flight_mode = "ASCENDING"
    else:
        flight_mode = "DESCENDING"

    print(drone.x)
    print(drone.x_velocity)
    draw_drone(
        screen,
        drone.x,
        drone.altitude,
        drone.velocity,
        target_altitude,
        battery,
        flight_mode,
        frame
    )

    frame += 1

    clock.tick(60)

pygame.quit()