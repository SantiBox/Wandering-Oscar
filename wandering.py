import random
 
class  wandering:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.y = y
        self.x = x

    def position (self):
        return (self.x, self.y)

    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5

class ComunWandering(wandering):
    def __init__(self, name):
        super().__init__(name)
       
    def walk(self):
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.y += dy
        self.x += dx
        return [dx, dy]

class RightWandering(wandering):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        dx, dy = random.choice([(0,5),(5,0),(-1,0),(0,-1)])
        self.y += dy
        self.x += dx
        return [dx, dy]

class LeftWandering(wandering):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        dx, dy = random.choice([(0,1),(1,0),(-5,0),(0,-5)])
        self.y += dy
        self.x += dx
        return [dx, dy]