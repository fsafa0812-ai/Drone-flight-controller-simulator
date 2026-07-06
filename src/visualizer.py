import pygame

WIDTH = 600
HEIGHT = 700

SKY = (180, 220, 255)
BLACK = (0, 0, 0)
GREEN = (50, 180, 50)
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)

# ---------------------------
# DRONE IMAGE
# ---------------------------
drone_image = pygame.image.load("assets/drone.png")
drone_image = pygame.transform.scale(drone_image, (80, 60))

# ---------------------------
# CLOUDS STATE
# ---------------------------
clouds = [
    [100, 80],
    [300, 120],
    [500, 60]
]


def draw_drone(screen, x, altitude, velocity, target, battery, flight_mode, frame, wind):

    screen.fill(SKY)

    # ---------------------------
    # CLOUDS (ANIMATION)
    # ---------------------------
    for cloud in clouds:
        cloud[0] -= 0.3  # movement speed

        if cloud[0] < -80:
            cloud[0] = 650

        cx, cy = cloud

        pygame.draw.circle(screen, WHITE, (int(cx), cy), 20)
        pygame.draw.circle(screen, WHITE, (int(cx + 20), cy - 10), 25)
        pygame.draw.circle(screen, WHITE, (int(cx + 40), cy), 20)

    # ---------------------------
    # GROUND + LANDING PAD
    # ---------------------------
    pygame.draw.rect(screen, GREEN, (0, 650, WIDTH, 50))
    pygame.draw.rect(screen, GRAY, (230, 620, 140, 10))

    font = pygame.font.SysFont(None, 24)
    screen.blit(font.render("H", True, WHITE), (292, 590))

    # ---------------------------
    # DRONE POSITION
    # ---------------------------
    y = 590 - int(altitude * 40)

    x = max(20, min(x, WIDTH - 80))

    screen.blit(drone_image, (x, y))

    # ---------------------------
    # DASHBOARD
    # ---------------------------
    font = pygame.font.SysFont(None, 28)

    screen.blit(font.render("DRONE TELEMETRY", True, BLACK), (20, 20))

    screen.blit(font.render(f"Altitude : {altitude:.2f} m", True, BLACK), (20, 60))
    screen.blit(font.render(f"Velocity : {velocity:.2f} m/s", True, BLACK), (20, 90))
    screen.blit(font.render(f"Target   : {target:.2f} m", True, BLACK), (20, 120))
    screen.blit(font.render(f"Battery  : {battery:.0f}%", True, BLACK), (20, 150))
    screen.blit(font.render(f"Mode     : {flight_mode}", True, BLACK), (20, 180))

    # ---------------------------
    # WIND INDICATOR
    # ---------------------------
    screen.blit(font.render(f"Wind : {wind:.2f} m/s", True, BLACK), (20, 210))

    bar_x = 150
    bar_y = 220
    bar_width = 120
    bar_height = 10

    pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), 1)

    # Normalize wind (-0.3 to +0.3)
    wind_normalized = int((wind + 0.3) / 0.6 * bar_width)
    wind_normalized = max(0, min(wind_normalized, bar_width))

    pygame.draw.rect(
        screen,
        (255, 120, 120),
        (bar_x, bar_y, wind_normalized, bar_height)
    )

    pygame.display.flip()