from models.Drone import Drone


class DeliveryDrone(Drone):
    def __init__(self, current_speed, current_altitude, max_payload=200, current_battery_level=0):
        super().__init__(current_speed, current_altitude)
        self.max_payload = max_payload
        self.current_battery_level = current_battery_level
        self.current_payload = 0

    def get_max_flying_distance_at_current_speed(self):
        return self.current_battery_level / 10 * self.current_speed

    def load_drone(self, cargo_weight):
        if cargo_weight >= self.max_payload:
            self.current_payload = self.max_payload
        else:
            self.current_payload += cargo_weight

    def __str__(self):
        return f"DeliveryDrone(current_speed={self.current_speed}, current_altitude={self.current_altitude}," \
            f" max_payload={self.max_payload}, current_battery_level={self.current_battery_level}," \
            f" current_payload={self.current_payload})"