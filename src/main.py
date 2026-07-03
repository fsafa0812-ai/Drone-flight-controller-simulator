from drone import Drone
from physics import update_drone
import time

print("🚁 Drone Flight Controller Simulator")
print("------------------------------------")

drone = Drone()

thrust = 12.0      # Newtons
dt = 0.1           # Time step (seconds)

for step in range(20):
    update_drone(drone, thrust, dt)

    print(f"Time: {(step+1)*dt:.1f} s")
    drone.display_status()
    print("----------------------")

    time.sleep(0.1)