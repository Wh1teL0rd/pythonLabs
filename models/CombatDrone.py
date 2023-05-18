from models.Drone import Drone


class CombatDrone(Drone):
    def __init__(self, current_speed, current_altitude, max_ammo=0, current_battery_level=0):
        super().__init__(current_speed, current_altitude)
        self.current_ammo = max_ammo
        self.max_ammo = max_ammo
        self.current_battery_level = current_battery_level

    def fire(self):
        if self.current_ammo > 0:
            self.current_ammo -= 1
            print("Firing! Ammo left:", self.current_ammo)
        else:
            print("Out of ammo. Reload!")

    def reload(self):
        self.current_ammo = self.max_ammo
        print("Reloading. Ammo reloaded:", self.max_ammo)

    def get_max_flying_distance_at_current_speed(self):
        return self.current_battery_level / 15 * self.current_speed

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__dict__}"
