from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.car_list=[]
        self.distance=STARTING_MOVE_DISTANCE
    def create_car(self):
        self.newcar=Turtle()
        self.newcar.color(random.choice(COLORS))
        self.newcar.shape("square")
        self.newcar.penup()
        self.newcar.goto(300,random.randint(-250,250))
        self.newcar.shapesize(stretch_len=2,stretch_wid=1)
        self.car_list.append(self.newcar)
    def move(self):
        for car in self.car_list:
            new_x=car.xcor()-self.distance
            car.goto(new_x,car.ycor())
    def increase_level(self):
        self.distance+=MOVE_INCREMENT