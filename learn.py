import random

class Enemy:

    def __int__(atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy(50, 70)
enemy1.getAtk()

enemy2 = Enemy(63, 66)
enemy2.getAtk()