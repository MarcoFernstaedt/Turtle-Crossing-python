import random
from turtle import Turtle

from matplotlib.dates import TU

COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCRAMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        new_car = Turtle('sqare')
        new_car.shapesize(2, 1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)