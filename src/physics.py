GRAVITY = 9.81


def update_drone(drone, thrust, dt):
    # Net force
    force = thrust - (drone.mass * GRAVITY)

    # Acceleration
    acceleration = force / drone.mass

    # Update velocity
    drone.velocity += acceleration * dt

    # Update altitude
    drone.altitude += drone.velocity * dt

    # Prevent the drone from going below the ground
    if drone.altitude < 0:
        drone.altitude = 0
        drone.velocity = 0
        