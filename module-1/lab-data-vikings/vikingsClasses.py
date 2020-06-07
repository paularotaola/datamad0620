
# Soldier
class Soldier:
    def __init__ (self, health, strenght):
        self.health = health
        self.strenght = strenght
    
    def attack(self):
        return self.strenght
    def receiveDamage(self, damage):
        self.health = self.health- damage
# Viking
class Viking (Soldier):
    def __init__(self, name, health, strenght):
        super().__init__(health, strenght)
        self.name = name
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon
class Saxon(Soldier):
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health < 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in act of combat"
# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self):
        self.vikingArmy.append("1")
    def addSaxon(self, Saxon):
        self.saxonArmy.append("1")
    def vikingAttack(self):
        viking_rd =random.choice(self.vikingArmy)
        saxon_rd =random.choice(self.saxonArmy)
        return saxon_rd.receiveDamage(viking_rd.strenght)
    def saxonAttack():
        viking_rd =random.choice(self.vikingArmy)
        saxon_rd =random.choice(self.saxonArmy)
        return viking_rd.receiveDamage(saxon_rd.strenght)
     
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) ==0:
            return "Saxons have fought for their lives and survive another day..."
        elif (len(self.saxonArmy) > 0) or (len(self.vikingArmy) > 0):
            return "Vikings and Saxons are still in the thick of battle"