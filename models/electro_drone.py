"""
This is electro drone class
"""
from .drone import Drone


# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
class ElectroDrone(Drone):
    """A class representing an electro drone.

    Args:
        current_speed (float): The current speed of the drone.
        current_altitude (float): The current altitude of the drone.
        battery_capacity (float): The battery capacity of the drone. Defaults to 0.
        fuel_consumption_per_hour (float): The fuel consumption per hour of the drone.
        Defaults to 0.
        current_battery_level (float): The current battery level of the drone. Defaults to 0.

    Attributes:
        battery_capacity (float): The battery capacity of the drone.
        current_battery_level (float): The current battery level of the drone.
        fuel_consumption_per_hour (float): The fuel consumption per hour of the drone.

    Methods:
        charge_battery(amount): Charges the battery of the drone by the specified amount.
        use_battery(amount): Uses the battery of the drone by the specified amount.
        get_max_flying_distance_at_current_speed(): Calculates and returns the maximum flying
        distance at the current speed based on the battery level and fuel consumption.
        __str__(): Returns a string representation of the electro drone.

    Inherits from:
        Drone: A base class representing a generic drone.
    """

    def __init__(self, current_speed, current_altitude, battery_capacity=0,
                 fuel_consumption_per_hour=0, current_battery_level=0):
        """
        Initializes a Drone object.

        :param: current_speed (float): The current speed of the drone in meters per minute.
        :param: current_altitude (float): The current altitude of the drone in meters.
        :param: battery_capacity (float): The battery capacity of the drone in ampere-hours.
         Defaults to 0.
        :param: fuel_consumption_per_hour (float): The fuel consumption rate of
        the drone in liters per hour. Defaults to 0.
        :param: current_battery_level (float): The current battery level of
        the drone in ampere-hours. Defaults to 0.

        """

        super().__init__(current_speed, current_altitude)
        self.battery_capacity = battery_capacity
        self.current_battery_level = current_battery_level
        self.fuel_consumption_per_hour = fuel_consumption_per_hour
        self.favorite_set = {"batteries", "charger"}

    def charge_battery(self, amount):
        """Charges the battery of the drone by the specified amount.

           :param: amount (float): The amount to charge the battery.
        """
        self.current_battery_level += amount
        if self.current_battery_level > self.battery_capacity:
            self.current_battery_level = self.battery_capacity

    def use_battery(self, amount):
        """Uses the battery of the drone by the specified amount.

            :param: amount (float): The amount to use from the battery.
        """
        self.current_battery_level -= amount
        if self.current_battery_level < 0:
            self.current_battery_level = self.battery_capacity

    def get_max_flying_distance_at_current_speed(self):
        """Calculates and returns the maximum flying distance at the current speed
        based on the battery level and fuel consumption.

            :return: float: The maximum flying distance at the current speed.
        """
        return self.current_battery_level / self.fuel_consumption_per_hour * self.current_speed

    def __str__(self):
        """
        Returns a string representation of drone.

            :return: str: A string representation of drone.
        """
        return f"{self.__class__.__name__}: {self.__dict__}"
