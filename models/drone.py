"""
This is abstract drone class
"""
from abc import ABC, abstractmethod


class Drone(ABC):
    """A base abstract class representing a drone.

    Args:
        current_speed (float): The current speed of the drone. Defaults to 10.
        current_altitude (float): The current altitude of the drone. Defaults to 5.

    Attributes:
        current_speed (float): The current speed of the drone.
        current_altitude (float): The current altitude of the drone.

    Methods:
        fly_at(speed_meters_per_minute, altitude): Sets the current speed and altitude of the drone.
        get_max_flying_distance_at_current_speed(): Abstract method to be implemented by
        subclasses for calculating the maximum flying distance at the current speed.

    Inherits from:
        ABC: A helper class that has ABCMeta as its metaclass. It allows
        the creation of abstract base classes by adding the @abstractmethod decorator.

    """

    def __init__(self, current_speed=10, current_altitude=5):
        """
            Initializes a new instance of the Drone class.

            :param: current_speed (float): The current speed of the drone in meters
             per minute. Default is 10.
            :param: current_altitude (float): The current altitude of the drone in meters.
            Default is 5.
            :param: favourite_set (set):
            """
        self.current_speed = current_speed
        self.current_altitude = current_altitude
        self.favorite_set = set()

    def fly_at(self, speed_meters_per_minute, altitude):
        """Sets the current speed and altitude of the drone.

            :param: speed_meters_per_minute (float): The speed in meters per minute to set.
            :param: altitude (float): The altitude to set.

        """
        self.current_speed = speed_meters_per_minute
        self.current_altitude = altitude

    @abstractmethod
    def get_max_flying_distance_at_current_speed(self):
        """
        Gets the maximum flying distance achievable at the current speed.

        Returns:
            float: The maximum flying distance in meters.
        """
    def __iter__(self):
        return iter(self.favorite_set)
