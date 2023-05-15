from drone import Drone

drones = [Drone(70, 600, 7000, 100), Drone(), Drone.get_instance(), Drone.get_instance()]

for drone in drones:
    print(drone)
