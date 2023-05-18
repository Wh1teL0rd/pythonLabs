from models.Drone import Drone


class ElectroDrone(Drone):
    def __init__(self, current_speed, current_altitude, battery_capacity=0, fuel_consumption_per_hour=0,
                 current_battery_level=0):
        super().__init__(current_speed, current_altitude)
        self.battery_capacity = battery_capacity
        self.current_battery_level = current_battery_level
        self.fuel_consumption_per_hour = fuel_consumption_per_hour

    def charge_battery(self, amount):
        self.current_battery_level += amount
        if self.current_battery_level > self.battery_capacity:
            self.current_battery_level = self.battery_capacity

    def use_battery(self, amount):
        self.current_battery_level -= amount
        if self.current_battery_level < 0:
            self.current_battery_level = 0

    def get_max_flying_distance_at_current_speed(self):
        return self.current_battery_level / self.fuel_consumption_per_hour * self.current_speed

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"
