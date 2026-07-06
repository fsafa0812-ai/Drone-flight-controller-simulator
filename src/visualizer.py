import pygame

WIDTH = 600
HEIGHT = 700

SKY = (180, 220, 255)
BLACK = (0, 0, 0)
GREEN = (50, 180, 50)
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)

# Load drone image
drone_image = pygame.image.load("assets/drone.png")
drone_image = pygame.transform.scale(drone_image, (80, 60))


def draw_drone(screen, x, altitude, velocity, target, battery, flight_mode,frame):

    screen.fill(SKY)

    # Clouds
    pygame.draw.circle(screen, WHITE, (100, 80), 25)
    pygame.draw.circle(screen, WHITE, (125, 65), 30)
    pygame.draw.circle(screen, WHITE, (150, 80), 25)

    pygame.draw.circle(screen, WHITE, (420, 120), 25)
    pygame.draw.circle(screen, WHITE, (445, 105), 30)
    pygame.draw.circle(screen, WHITE, (470, 120), 25)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 650, WIDTH, 50))

    # Landing pad
    pygame.draw.rect(screen, GRAY, (230, 620, 140, 10))

    font = pygame.font.SysFont(None, 30)
    h_text = font.render("H", True, WHITE)
    screen.blit(h_text, (292, 590))

    # Convert altitude to screen position
    y = 590 - int(altitude * 40)

    # Keep drone inside screen
    x = max(20, min(x, WIDTH - 80))

    # Draw drone image
    screen.blit(drone_image, (x, y))

    # Dashboard
    font = pygame.font.SysFont(None, 28)

    screen.blit(font.render("DRONE TELEMETRY", True, BLACK), (20, 20))
    screen.blit(font.render(f"Altitude : {altitude:.2f} m", True, BLACK), (20, 60))
    screen.blit(font.render(f"Velocity : {velocity:.2f} m/s", True, BLACK), (20, 90))
    screen.blit(font.render(f"Target   : {target:.2f} m", True, BLACK), (20, 120))
    screen.blit(font.render(f"Battery  : {battery:.0f}%", True, BLACK), (20, 150))
    screen.blit(font.render(f"Mode     : {flight_mode}", True, BLACK), (20, 180))

    pygame.display.flip()