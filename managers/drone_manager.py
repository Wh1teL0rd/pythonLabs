"""
This is DroneManager class contains list of drones
"""


class DroneManager:
    """A class representing a drone manager.

    Attributes:
        drone_list (list): A list of drones managed by the manager.

    Methods:
        add_drone(new_drone): Adds a single drone to the manager.
        add_drones(drones): Adds multiple drones to the manager.
        find_altitude_bigger_than(altitude): Finds drones with altitude
         greater than the specified value.
        find_speed_bigger_than(speed): Finds drones with speed greater than the specified value.

    """

    def __init__(self):
        """
           Initializes an instance of DroneManager.

           This method initializes the `drone_list` attribute as an empty list.

        """
        self.drone_list = []

    def add_drone(self, new_drone):
        """Adds a single drone to the manager.

        Args:
            new_drone (Drone): The drone to be added.

        """
        self.drone_list.append(new_drone)

    def add_drones(self, drones):
        """Adds multiple drones to the manager.

        Args:
            drones (list): A list of drones to be added.

        """
        self.drone_list.extend(drones)

    def find_altitude_bigger_than(self, altitude):
        """Finds drones with altitude greater than the specified value.

        Args:
            altitude (float): The altitude threshold.

        Returns:
            list: A list of drones with altitude greater than the threshold.

        """
        return [drone for drone in self.drone_list if drone.current_altitude > altitude]

    def find_speed_bigger_than(self, speed):
        """Finds drones with speed greater than the specified value.

        Args:
            speed (float): The speed threshold.

        Returns:
            list: A list of drones with speed greater than the threshold.

        """
        return [drone for drone in self.drone_list if drone.current_speed > speed]
