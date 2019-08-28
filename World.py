from random import randint
from parameters import *

class World:

    def __init__(self,size):
        self.size = size
        self.foods = []
        self.lives = []

    def addFood(self):
        food = (randint(1,self.size-1),randint(1,self.size-1))
        while self.detectCollision(food) != (0,None):
            food = (randint(1,self.size-1),randint(1,self.size-1))
        self.foods.append(food);
    
    def detectCollision(self, location):
        if location[0] < 0 or location[0] >= self.size or location[1] < 0 or location[1] >= self.size:
            return (HIT_BORDER,None)

        if location in self.foods:
            return (HIT_FOOD,None)


        for i in self.lives:
            for j in i.locations:
                if location == j:
                    return (HIT_LIFE,i)

        return (0,None)

    
    def addLife(self,life):
        self.lives.append(life)
        
