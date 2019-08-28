from random import randint

class Life:
    def __init__(self,world,index,startLocation = (0, 0), control="AI"):
        
        if startLocation == (0,0):
            self.locations = [(randint(1, world.size - 10),randint(1, world.size - 1))]
        else:
            self.locations = [startLocation]
        self.world = world
        self.index = index
        self.control = control



    def die(self):
        print("Points: " + str(len(self.locations)))
        for i in self.locations:
            self.world.foods.append(i)
        self.world.lives.remove(self)
        print(self.world.lives)
    