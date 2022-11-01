
class Hero:
    health = 100
    def __init__(self, health):
        self.health = health
        self.inventory = {}

    def seeiventory(self):
        liste = {}
        for items in self.inventory:
            liste[items.name]= self.inventory[items]
        return f'Inventory: {liste}'

    def takedamage(self, damage):
        self.health = self.health-damage
        return str(self.health+damage)+' - '+str(damage)

    def addtoinventory(self, item, count):
        if item in self.inventory:
            if item.maxstack > self.inventory[item]+count:
                self.inventory[item] = self.inventory[item]+count
            else:
                self.inventory[item] = item.maxstack
        else:
            self.inventory[item] = count
        return None

    def removetoinventory(self, item, count):
        if item in self.inventory:
            if self.inventory[item] < count:
                print("ERROR: NOT ENOUGH ITEMS")
            if self.inventory[item] == count:
                self.inventory.pop(item)
            else:
                self.inventory[item] = self.inventory[item] - count
        else:
            print("ERROR NO ITEM")


class Item:
    def __init__(self, name, usable, maxstack):
        self.name = str(name)
        self.usable = bool(usable)
        self.maxstack = int(maxstack)

