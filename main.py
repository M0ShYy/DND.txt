from classes import *

Player = Hero(health=100)
rope = Item("Rope", True, 10)

print(f'Health: {Player.health}')
Player.addtoinventory(rope, 2)
print(Player.seeiventory())
Player.addtoinventory(rope, 12)
print(Player.seeiventory())