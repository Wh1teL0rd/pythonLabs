"""
This is DroneManager class contains list of drones
"""
from decorators.log_arguments_to_file import log_arguments_to_file


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

            :param: new_drone (Drone): The drone to be added.

        """
        self.drone_list.append(new_drone)

    def add_drones(self, drones):
        """Adds multiple drones to the manager.

            :param: drones (list): A list of drones to be added.

        """
        self.drone_list.extend(drones)

    def find_altitude_bigger_than(self, altitude):
        """Finds drones with altitude greater than the specified value.

            :param: altitude (float): The altitude threshold.

            :return: list: A list of drones with altitude greater than the threshold.

        """
        return [drone for drone in self.drone_list if drone.current_altitude > altitude]

    def find_speed_bigger_than(self, speed):
        """Finds drones with speed greater than the specified value.

            :param: speed (float): The speed threshold.


            :return: list: A list of drones with speed greater than the threshold.

        """
        return [drone for drone in self.drone_list if drone.current_speed > speed]

    def __len__(self):
        """Returns the number of drones in the manager."""
        return len(self.drone_list)

    def __getitem__(self, index):
        """Returns the drone at the specified index."""
        return self.drone_list[index]

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.drone_list):
            raise StopIteration
        else:
            drone = self.drone_list[self.current_index]
            self.current_index += 1
            return drone

    def get_max_flying_distance_list(self):
        """Returns a list of maximum flying distances at current speed for all drones in the manager."""
        return [drone.get_max_flying_distance_at_current_speed() for drone in self.drone_list]

    def get_concatenated_objects_with_index(self):
        """Returns the concatenation of each object with its index in the list."""
        return [f'{index}: {obj}' for index, obj in enumerate(self.drone_list)]

    def get_concatenated_object_and_result(self):
        """Returns the concatenation of each object and the result of the method execution."""
        results = self.get_max_flying_distance_list()
        return [f'{obj}: {result}' for obj, result in zip(self.drone_list, results)]

    @log_arguments_to_file("arguments.log")
    def get_attributes_by_value_type(self, value_type):
        """Returns a dictionary with attributes and their values of the specified value type.

            :param: value_type (type): The type of values to filter attributes.

            :return: dict: A dictionary containing attributes and their values of the specified value type.

        """
        return {attr: value for obj in self.drone_list for attr, value in obj.__dict__.items() if
                isinstance(value, value_type)}

    def check_condition(self, condition):
        """
        Checks the condition for all objects in the drone manager.

            :param: condition (callable): The condition to check for each object.

            :return: dict: A dictionary with keys "all" and "any" representing the results of the condition.

        """
        all_condition = all(condition(drone) for drone in self.drone_list)
        any_condition = any(condition(drone) for drone in self.drone_list)
        return {"all": all_condition, "any": any_condition}
