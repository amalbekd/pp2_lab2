import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, p):
        dx = p.x - self.x
        dy = p.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)