from Life import *
from parameters import *


class Snake(Life):
    direction = RIGHT

    def move(self):

        self.ai();
        
        head = self.locations[-1]
        if self.direction == RIGHT:
            newHead = (head[0] + 1, head[1])
        elif self.direction == DOWN:
            newHead = (head[0], head[1] + 1)
        elif self.direction == LEFT:
            newHead = (head[0] - 1, head[1])
        elif self.direction == UP:
            newHead = (head[0] , head[1] - 1)
        else:
            pass

        self.checkEnviroment(newHead)

    def checkEnviroment(self,newHead):
        
        result,life = self.world.detectCollision(newHead)

        if result == HIT_BORDER:
            self.die()
        elif result == HIT_FOOD:
            self.locations.append(newHead)
            self.world.foods.remove(newHead)
            if len(self.world.foods) == 0:
                self.world.addFood()

        elif result == HIT_LIFE and life == self:
            self.die()
        else:
            self.locations.pop(0)
            self.locations.append(newHead)


    def changeDirection(self,direction):
        self.direction = direction
    

    def ai(self):
        currentHead = self.locations[-1]
        nextHeads = self.getNextMoves(currentHead);
        for i in nextHeads:
            nextResult,life = self.world.detectCollision((i[0],i[1]))

            i.append(nextResult)
            if nextResult == 0 or nextResult == HIT_FOOD:
                self.evaluateDistance(i,self.world.foods[0])
            else:
                i.append(9999)

        nextHeads.sort(key = lambda x:x[4]);
        # print(nextHeads)
        self.changeDirection(nextHeads[0][2])

    def getNextMoves(self,head):
        right = [head[0] + 1, head[1], RIGHT]
        down = [head[0], head[1] + 1, DOWN]
        left = [head[0] - 1, head[1], LEFT]
        up = [head[0], head[1] - 1, UP]

        return [right,down,left,up]

    
    def evaluateDistance(self,location1, location2):
        location1.append(abs(location1[0] - location2[0]) + abs(location1[1] - location2[1]))