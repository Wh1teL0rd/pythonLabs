"""
This is petrol drone class
"""
from .drone import Drone


# pylint: disable=too-many-arguments
# pylint: disable=line-too-long
class PetrolDrone(Drone):
    """A class representing a petrol drone.

    Args:
        current_speed (float): The current speed of the drone.
        current_altitude (float): The current altitude of the drone.
        tank_capacity (float): The tank capacity of the drone. Defaults to 0.
        type_of_fuel (str): The type of fuel used by the drone. Defaults to 0.
        fuel_consumption_per_hour (float, optional): The fuel consumption per hour of the drone. Defaults to 0.

    Attributes:
        tank_capacity (float): The tank capacity of the drone.
        type_of_fuel (str): The type of fuel used by the drone.
        fuel_consumption_per_hour (float): The fuel consumption per hour of the drone.

    Methods:
        get_max_flying_distance_at_current_speed(): Calculates and returns the maximum flying distance
        at the current speed based on the tank capacity and fuel consumption.
        __str__(): Returns a string representation of the petrol drone.

    Inherits from:
        Drone: A base class representing a generic drone.
    """

    def __init__(self, current_speed, current_altitude, tank_capacity=0, type_of_fuel=0, fuel_consumption_per_hour=0):
        """
           Initializes a PetrolDrone object.

               :param: current_speed (float): The current speed of the petrol drone in meters per minute.
               :param: current_altitude (float): The current altitude of the petrol drone in meters.
               :param: tank_capacity (float): The tank capacity of the petrol drone in liters. Defaults to 0.
               :param: type_of_fuel (str): The type of fuel used by the petrol drone. Defaults to 0.
               :param: fuel_consumption_per_hour (float): The fuel consumption rate of
               the petrol drone in liters per hour. Defaults to 0.
           """
        super().__init__(current_speed, current_altitude)
        self.tank_capacity = tank_capacity
        self.type_of_fuel = str(type_of_fuel)
        self.fuel_consumption_per_hour = fuel_consumption_per_hour
        self.favorite_set = {"fuel", "engine"}

    def get_max_flying_distance_at_current_speed(self):
        """Calculates and returns the maximum flying distance at the current speed
         based on the tank capacity and fuel consumption.

        Returns:
            float: The maximum flying distance at the current speed.
        """
        return self.tank_capacity / self.fuel_consumption_per_hour * self.current_speed

    def __str__(self):
        """
        Returns a string representation of drone.

        Returns:
            str: A string representation of drone.
        """
        return f"{self.__class__.__name__}: {self.__dict__}"
