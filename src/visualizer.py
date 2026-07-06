import pygame

WIDTH = 600
HEIGHT = 700

SKY = (180, 220, 255)
BLACK = (0, 0, 0)
GREEN = (50, 180, 50)
GRAY = (80, 80, 80)
RED = (220, 50, 50)


def draw_drone(screen, x, altitude, velocity, target, battery,flight_mode, frame):

    screen.fill(SKY)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 650, WIDTH, 50))

    # Convert altitude to screen position
    y = 650 - int(altitude * 40)

    # Keep drone inside the screen
    x = max(20, min(x, WIDTH - 60))

    # Drone body
    pygame.draw.rect(screen, GRAY, (x, y, 40, 15))

    # Drone arms
    pygame.draw.line(screen, BLACK, (x - 20, y + 7), (x + 60, y + 7), 3)

    # Simple propeller animation
    prop_length = 8 + (frame % 6)

    pygame.draw.line(
        screen, RED,
        (x - 20 - prop_length, y + 7),
        (x - 20 + prop_length, y + 7),
        2
    )

    pygame.draw.line(
        screen, RED,
        (x + 60 - prop_length, y + 7),
        (x + 60 + prop_length, y + 7),
        2
    )

    # Landing legs
    pygame.draw.line(screen, BLACK, (x + 5, y + 15), (x, y + 25), 2)
    pygame.draw.line(screen, BLACK, (x + 35, y + 15), (x + 40, y + 25), 2)

    # Dashboard
    font = pygame.font.SysFont(None, 28)

    screen.blit(font.render(f"Altitude : {altitude:.2f} m", True, BLACK), (20, 20))
    screen.blit(font.render(f"Velocity : {velocity:.2f} m/s", True, BLACK), (20, 50))
    screen.blit(font.render(f"Target   : {target:.2f} m", True, BLACK), (20, 80))
    screen.blit(font.render(f"Battery  : {battery:.0f}%", True, BLACK), (20, 110))

    # Flight mode
    difference= target- altitude
    if abs(difference)<= 0.2 and abs(velocity)<=0.1:
        mode = "HOVER"
    elif difference > 0:
        mode = "ASCENDING"
    else:
        mode = "DESCENDING"

    screen.blit(font.render(f"Mode     : {mode}", True, BLACK), (20, 140))

    pygame.display.flip()