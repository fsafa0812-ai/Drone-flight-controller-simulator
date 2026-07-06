import pygame

WIDTH = 600
HEIGHT = 700

WHITE = (255, 255, 255)
SKY = (180, 220, 255)
BLACK = (0, 0, 0)
GREEN = (50, 180, 50)
GRAY = (80, 80, 80)
RED = (220, 50, 50)


def draw_drone(screen, x, altitude, target, frame):

    screen.fill(SKY)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 650, WIDTH, 50))

    # Convert altitude to screen position
    y = 650 - int(altitude * 40)

    # Keep drone inside the window
    if x < 20:
        x = 20
    if x > WIDTH - 60:
        x = WIDTH - 60

    # Drone body
    pygame.draw.rect(screen, GRAY, (x, y, 40, 15))

    # Arms
    pygame.draw.line(screen, BLACK, (x - 20, y + 7), (x + 60, y + 7), 3)

    # Propellers
    pygame.draw.circle(screen, RED, (x - 20, y + 7), 8, 2)
    pygame.draw.circle(screen, RED, (x + 60, y + 7), 8, 2)

    # Landing legs
    pygame.draw.line(screen, BLACK, (x + 5, y + 15), (x, y + 25), 2)
    pygame.draw.line(screen, BLACK, (x + 35, y + 15), (x + 40, y + 25), 2)

    font = pygame.font.SysFont(None, 30)

    altitude_text = font.render(
        f"Altitude: {altitude:.2f} m",
        True,
        BLACK
    )

    target_text = font.render(
        f"Target: {target:.2f} m",
        True,
        BLACK
    )

    screen.blit(altitude_text, (20, 20))
    screen.blit(target_text, (20, 55))

    pygame.display.flip()