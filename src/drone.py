class Drone:
    def __init__(self):
        self.x = 280
        self.x_velocity = 0.0
        self.altitude = 0.0
        self.velocity = 0.0
        self.mass = 1.0

    def display_status(self):
        print(f"Altitude : {self.altitude:.2f} m")
        print(f"Velocity : {self.velocity:.2f} m/s")