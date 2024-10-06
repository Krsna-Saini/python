import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
my_man=Player()
car_system=CarManager()
my_scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=my_man.move, key="Up")
car_gen_control=0

freq=5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_gen_control+=1
    if car_gen_control%freq==0:
        car_system.create_car()
    car_system.move()

    # detecting colision with cars
    for cars in car_system.car_list:
        if cars.distance(my_man)<25:
            game_is_on=False

    # detecting collision with upper wall
    if my_man.is_reached():
        my_scoreboard.increase_score()
        my_man.reset_position()
        # increasing level
        car_system.increase_level()
        if freq>1:
            freq-=1

my_man.hideturtle()
for car in car_system.car_list:
    car.hideturtle()
screen.reset()
my_scoreboard.Game_over()
screen.exitonclick()
