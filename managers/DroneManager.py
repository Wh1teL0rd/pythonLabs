class DroneManager:
    def __init__(self):
        self.drone_list = []

    def add_drone(self, new_drone):
        self.drone_list.append(new_drone)

    def add_drones(self, drones):
        self.drone_list.extend(drones)

    def find_altitude_bigger_than(self, altitude):
        return [drone for drone in self.drone_list if drone.current_altitude > altitude]

    def find_speed_bigger_than(self, speed):
        return [drone for drone in self.drone_list if drone.current_speed > speed]
