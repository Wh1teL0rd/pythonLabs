from models.Drone import Drone


class PetrolDrone(Drone):
    def __init__(self, current_speed, current_altitude, tank_capacity=0, type_of_fuel=0, fuel_consumption_per_hour=0):
        super().__init__(current_speed, current_altitude)
        self.tank_capacity = tank_capacity
        self.type_of_fuel = type_of_fuel
        self.fuel_consumption_per_hour = fuel_consumption_per_hour

    def get_max_flying_distance_at_current_speed(self):
        return self.tank_capacity / self.fuel_consumption_per_hour * self.current_speed

    def __str__(self):
        return f"PetrolDrone(current_speed={self.current_speed}, current_altitude={self.current_altitude}," \
            f" tank_capacity={self.tank_capacity}, type_of_fuel={self.type_of_fuel}," \
            f" fuel_consumption_per_hour={self.fuel_consumption_per_hour})"