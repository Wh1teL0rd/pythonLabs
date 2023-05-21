from models.drone import Drone


class CombatDrone(Drone):
    """A class representing a combat drone.

    Args:
        current_speed (float): The current speed of the drone.
        current_altitude (float): The current altitude of the drone.
        max_ammo (float): The maximum ammo capacity of the drone. Defaults to 0.
        current_battery_level (float): The current battery level of the drone. Defaults to 0.

    Attributes:
        current_ammo (float): The current ammo count of the drone.
        max_ammo (float): The maximum ammo capacity of the drone.
        current_battery_level (float): The current battery level of the drone.

    Methods:
        fire(): Fires a shot from the drone.
        reload(): Reloads the drone with ammo.
        get_max_flying_distance_at_current_speed(): Calculates the maximum flying distance
        at the current speed and battery level.

    Inherits from:
        Drone: A base abstract class representing a drone.

    """

    def __init__(self, current_speed, current_altitude, max_ammo=0, current_battery_level=0):
        super().__init__(current_speed, current_altitude)
        self.current_ammo = max_ammo
        self.max_ammo = max_ammo
        self.current_battery_level = current_battery_level

    def fire(self):
        """Fires a shot from the drone."""
        if self.current_ammo > 0:
            self.current_ammo -= 1
            print("Firing! Ammo left:", self.current_ammo)
        else:
            print("Out of ammo. Reload!")

    def reload(self):
        """Reloads the drone with ammo."""
        self.current_ammo = self.max_ammo
        print("Reloading. Ammo reloaded:", self.max_ammo)

    def get_max_flying_distance_at_current_speed(self):
        """Calculates the maximum flying distance at the current speed and battery level.

        Returns:
            float: The maximum flying distance.

        """
        return self.current_battery_level / 15 * self.current_speed

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"
