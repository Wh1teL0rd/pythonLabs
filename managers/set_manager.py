"""
This is SetManager class
"""


class SetManager:
    """A class representing a Set Manager.

    The Set Manager is responsible for managing sets of objects from a regular manager.
    It provides iteration, length, indexing, and next functionality based on the favorite sets
    of the objects in the regular manager.

    Attributes:
        regular_manager (RegularManager): The regular manager containing the objects.

    Methods:
        __iter__(): Returns an iterator that iterates over the objects in the favorite sets.
        __len__(): Returns the total length of all favorite sets combined.
        __getitem__(index): Returns the item at the specified index in the combined favorite sets.
        __next__(): Raises a StopIteration exception.

    """

    def __init__(self, regular_manager):
        """
        Initializes a new instance of the SetManager class.

        :param: (RegularManager): The regular manager containing the objects.

        """
        self.regular_manager = regular_manager

    def __iter__(self):
        """
        Returns an iterator that iterates over the objects in the favorite sets.

            :return: iterator: An iterator over the objects in the favorite sets.
        """
        for drone in self.regular_manager.drone_list:
            yield from drone.favorite_set

    def __len__(self):
        """
        Returns the total length of all favorite sets combined.

            :return: int: The total length of all favorite sets combined.
        """
        total_len = 0
        for drone in self.regular_manager.drone_list:
            total_len += len(drone.favorite_set)
        return total_len

    def __getitem__(self, index):
        """
        Returns the item at the specified index in the combined favorite sets.

            :param: index (int): The index of the item to retrieve.

            :return: object: The item at the specified index in the combined favorite sets.

            :raises: IndexError: If the index is out of range.
        """
        count = 0
        for drone in self.regular_manager.drone_list:
            if count <= index < count + len(drone.favorite_set):
                inner_index = index - count
                return list(drone.favorite_set)[inner_index]
            count += len(drone.favorite_set)
        raise IndexError("list index out of range")

    def __next__(self):
        """
        Raises a StopIteration exception.

        This method is required for iterator compatibility but is not used in SetManager.

            :raises: StopIteration: Always raised to indicate the end of iteration.
        """
        raise StopIteration()
