from drone import Drone
from physics import update_drone
from controller import PIDController
import time

print("🚁 Drone Flight Controller Simulator")
print("------------------------------------")

drone = Drone()

# Create PID controller
pid = PIDController(kp=5.0, ki=0.2, kd=2.0)

target_altitude = 10.0  # meters
dt = 0.1

for step in range(100):

    # PID calculates extra thrust
    control = pid.compute(target_altitude, drone.altitude, dt)

    # Base thrust to counter gravity
    thrust = drone.mass * 9.81 + control

    update_drone(drone, thrust, dt)

    print(
        f"Time: {(step+1)*dt:.1f}s | "
        f"Altitude: {drone.altitude:.2f} m | "
        f"Velocity: {drone.velocity:.2f} m/s | "
        f"Thrust: {thrust:.2f} N"
    )

    time.sleep(0.1)