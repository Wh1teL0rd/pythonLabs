from models.Drone import Drone


class PetrolDrone(Drone):
    def __init__(self, current_speed, current_altitude, tank_capacity=0, type_of_fuel=0, fuel_consumption_per_hour=0):
        super().__init__(current_speed, current_altitude)
        self.tank_capacity = tank_capacity
        self.type_of_fuel = type_of_fuel
        self.fuel_consumption_per_hour = fuel_consumption_per_hour

    def get_max_flying_distance_at_current_speed(self):
        return self.tank_capacity / self.fuel_consumption_per_hour * self.current_speed
