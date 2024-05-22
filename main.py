from turtle import Turtle , Screen
import random

is_race_on = False

sc = Screen() # creat a window

sc.setup(500,400)  # set the size of the window

user_bet = sc.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")
# creates a window that takes text input 
print(user_bet)  # prints the window

colors = ["red","green","orange","blue","purple"] # list of colors

y_position = [-70,-40,-10,20,50] # y position of the turtles
all_turtles = []

for turtle_index in range(0,5): # creat 5 turtles
  new_turtle = Turtle() # creat a turtle
  new_turtle.color(colors[turtle_index]) # set the color of the turtle
  new_turtle.shape("turtle") # set the shape of the turtle
  new_turtle.penup() # lift the pen up so that it does not draw
  new_turtle.goto(x = -230, y = y_position[turtle_index]) # set the position of the turtle
  all_turtles.append(new_turtle)
  
if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
        
    random_distance = random.randint(0,10)
    turtle.forward(random_distance)
  

sc.exitonclick() # keep the window open