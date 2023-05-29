"""
This is main file to show how code work
"""

from managers.drone_manager import DroneManager
from managers.set_manager import SetManager
from models.combat_drone import CombatDrone
from models.delivery_drone import DeliveryDrone
from models.electro_drone import ElectroDrone
from models.petrol_drone import PetrolDrone


drones = [ElectroDrone(40, 280, 8000, 7000, 900), DeliveryDrone(35, 350, 9600, 9000),
          CombatDrone(60, 130, 3, 5000), PetrolDrone(60, 230, 25, "Benzin", 2.5)]

fleet = DroneManager()
fleet.add_drones(drones)
fleet.add_drone(PetrolDrone(20, 130, 24, "Kerosin", 1.5))

print("List of drones:")

for drone in fleet:
    print(drone)

print("\nMax flying distance list:")

drones3 = fleet.get_max_flying_distance_list()

for max_distance in drones3:
    print(max_distance)

print("\nList of attributes by value type str:")

drones4 = fleet.get_attributes_by_value_type(str)

for attr_by_value in drones4:
    print(attr_by_value)


def altitude_condition(some_drone):
    return some_drone.current_altitude > 200


print("\nCheck condition current_altitude > 200:")

result = fleet.check_condition(altitude_condition)

print("All drones satisfy the altitude condition:", result["all"])
print("At least one drone satisfies the altitude condition:", result["any"])

set_manager = SetManager(fleet)

print("\nLength of SetManager: ", len(set_manager))
print("\nItems in sets: ")
for item in set_manager:
    print(item)

fleet.drone_list[0].fly_at(200, 300)
fleet.drone_list[2].fly_at(100, 3000)
