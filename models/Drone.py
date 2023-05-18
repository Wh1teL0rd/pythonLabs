from abc import ABC, abstractmethod


class Drone(ABC):
    def __init__(self, current_speed=10, current_altitude=5):
        self.current_speed = current_speed
        self.current_altitude = current_altitude

    def fly_at(self, speed_meters_per_minute, altitude):
        self.current_speed = speed_meters_per_minute
        self.current_altitude = altitude

    @abstractmethod
    def get_max_flying_distance_at_current_speed(self):
        pass

    def __str__(self):
        return f"Drone(current_speed={self.current_speed}, current_altitude={self.current_altitude}"
