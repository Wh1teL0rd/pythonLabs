class Drone:
    instance = None

    def __init__(self, current_speed=10, current_altitude=5, battery_capacity=200, current_battery_level=200):
        self.current_speed = current_speed
        self.current_altitude = current_altitude
        self.battery_capacity = battery_capacity
        self.current_battery_level = current_battery_level

    def fly_at(self, speed_meters_per_minute, altitude):
        self.current_speed = speed_meters_per_minute
        self.current_altitude = altitude

    def charge_battery(self, amount):
        self.current_battery_level += amount

    def use_battery(self, amount):
        self.current_battery_level -= amount

    @staticmethod
    def get_instance():
        if not Drone.instance:
            Drone.instance = Drone()
        return Drone.instance

    def __str__(self):
        return f"Drone(current_speed={self.current_speed}, current_altitude={self.current_altitude}," \
               f" battery_capacity={self.battery_capacity}, current_battery_level={self.current_battery_level})"


drones = [Drone(70, 600, 7000, 100), Drone(), Drone.get_instance(), Drone.get_instance()]

for drone in drones:
    print(drone)
