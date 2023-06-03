"""
This is main file to show how code work
"""


from models.combat_drone import CombatDrone

new_combat_drone = CombatDrone(50, 200, 20, 100)

print(new_combat_drone)

new_combat_drone.reload()

new_combat_drone.current_ammo = 0

new_combat_drone.fire()
