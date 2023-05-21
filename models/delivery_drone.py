from models.drone import Drone


class DeliveryDrone(Drone):
    """A class representing a delivery drone.

    Args:
        current_speed (float): The current speed of the drone.
        current_altitude (float): The current altitude of the drone.
        max_payload (float): The maximum payload capacity of the drone. Defaults to 200.
        current_battery_level (float): The current battery level of the drone. Defaults to 0.

    Attributes:
        max_payload (float): The maximum payload capacity of the drone.
        current_battery_level (float): The current battery level of the drone.
        current_payload (float): The current payload of the drone.

    Methods:
        get_max_flying_distance_at_current_speed(): Calculates the maximum flying
        distance at the current speed and battery level.
        load_drone(cargo_weight): Loads the drone with the given cargo weight.

    Inherits from:
        Drone: A base abstract class representing a drone.

    """

    def __init__(self, current_speed, current_altitude, max_payload=200, current_battery_level=0):
        super().__init__(current_speed, current_altitude)
        self.max_payload = max_payload
        self.current_battery_level = current_battery_level
        self.current_payload = 0

    def get_max_flying_distance_at_current_speed(self):
        """Calculates the maximum flying distance at the current speed and battery level.

        Returns:
            float: The maximum flying distance.

        """
        return self.current_battery_level / 10 * self.current_speed

    def load_drone(self, cargo_weight):
        """Loads the drone with the given cargo weight.

        Args:
            cargo_weight (float): The weight of the cargo to load.

        """
        if cargo_weight >= self.max_payload:
            self.current_payload = self.max_payload
        else:
            self.current_payload += cargo_weight

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"
