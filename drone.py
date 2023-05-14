class Drone:
    _instance = None

    def __init__(self, current_speed=10, current_altitude=5, battery_capacity=200, current_battery_level=200):
        self._current_speed = current_speed
        self._current_altitude = current_altitude
        self._battery_capacity = battery_capacity
        self._current_battery_level = current_battery_level

    def fly_at(self, speed_meters_per_minute, altitude):
        self._current_speed = speed_meters_per_minute
        self._current_altitude = altitude

    def charge_battery(self, amount):
        self._current_battery_level += amount

    def use_battery(self, amount):
        self._current_battery_level -= amount

    def get_current_speed(self):
        return self._current_speed

    def set_current_speed(self, speed):
        self._current_speed = speed

    def get_current_altitude(self):
        return self._current_altitude

    def set_current_altitude(self, altitude):
        self._current_altitude = altitude

    def get_battery_capacity(self):
        return self._battery_capacity

    def set_battery_capacity(self, capacity):
        self._battery_capacity = capacity

    def get_current_battery_level(self):
        return self._current_battery_level

    def set_current_battery_level(self, level):
        self._current_battery_level = level

    @staticmethod
    def get_instance():
        if not Drone._instance:
            Drone._instance = Drone()
        return Drone._instance

    def __str__(self):
        return f"Drone(current_speed={self._current_speed}, current_altitude={self._current_altitude}," \
               f" battery_capacity={self._battery_capacity}, current_battery_level={self._current_battery_level})"
