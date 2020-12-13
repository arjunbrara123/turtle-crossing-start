# Import libraries and custom classes
import time                         # Library for creating delay between animation screens
from turtle import Screen, Turtle   # Screen for GUI
from player import Player           # Custom class for the playable character the user controls
from car_manager import CarManager  # Custom class to autogenerate bots as cars
from scoreboard import Scoreboard   # Custom cass to display the users level


# Create debugging mode
def debug_mode():
    for car in car_manager.cars_on_road:
        print(car.pos())
    breakpoint()


# Initialise object references
screen = Screen()                       # Initialise turtle screen object
screen.tracer(0)                        # Turn off automatic screen updating and set to manual only
screen.setup(width=600, height=600)     # Initialise GUI screen
screen.title("Turtle Crossing")
scoreboard = Scoreboard()               # Initialise scoreboard object
car_manager = CarManager()              # Initialise Car Manager object
player = Player()                       # Initialise Player object

# Initial game setup

# Road dashed lines
for y in [-210, -20, 20, 210]:
    liner = Turtle()
    liner.penup()
    liner.setposition(-300, y)
    for i in range(60):  # Set number of dashes to loop though
        liner.penup()  # Lift pen off screen
        liner.forward(10)  # Move forward without drawing line
        liner.pendown()  # Put pen back on screen to start drawing again
        liner.forward(10)  # Draw white line

# Set up player controls
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(debug_mode, "d")

# Start game playing
game_is_on = True                   # Looping variable to indicate if we want to keep the game still playing
frame = 0
level = 0
while game_is_on:                   # Start the continuous game loop until this variable is set to False
    time.sleep(0.1)                 # Pause by 0.1 seconds between frames to create animation effect
    frame += 1
    screen.update()                 # Update screen and show user latest frame

    if frame % 6 == 0:
        car_manager.add_car()
    car_manager.move(level)

    for car in car_manager.cars_on_road:
        if player.distance(car) < 10:
            scoreboard.game_over(level)
            player.color("red")
            player.shape("circle")
            player.shapesize(3)
            screen.update()
            game_is_on = False

    if player.level_complete():
        level += 1
        scoreboard.refresh(level)
        player.next_level()

screen.exitonclick()