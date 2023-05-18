from managers.DroneManager import DroneManager
from models.CombatDrone import CombatDrone
from models.DeliveryDrone import DeliveryDrone
from models.ElectroDrone import ElectroDrone
from models.PetrolDrone import PetrolDrone

print("\t\tFIRST PART\n")

drones = [ElectroDrone(40, 280, 8000, 7000, 900), DeliveryDrone(35, 350, 9600, 9000),
          CombatDrone(60, 130, 3, 5000), PetrolDrone(60, 230, 25, "Benzin", 2.5)]

for drone in drones:
    print(drone.__class__.__name__, drone.__dict__)

fleet = DroneManager()
fleet.add_drones(drones)
fleet.add_drone(PetrolDrone(20, 130, 24, "Kerosin", 1.5))

print("\n\t\tSECOND PART\n")
print("Drones current altitude bigger than 270: \n")

drones1 = fleet.find_altitude_bigger_than(270)

for drone in drones1:
    print(drone.__class__.__name__, drone.__dict__)

print("\nDrones current speed bigger than 50\n")

drones2 = fleet.find_speed_bigger_than(50)

for drone in drones2:
    print(drone.__class__.__name__, drone.__dict__)
