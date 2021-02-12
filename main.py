import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")

# Turtle only works with images of .gif type
background_image = "blank_states_img.gif"
screen.addshape(background_image)

# turtle.register_shape(background_image)
turtle.shape(background_image)
turtle.penup()

# Get coordinates of where the mouse was clicked
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# When the user clicks on the map to point to a state, the screen will actually exit
# So instead of screen.exitonclick(), timmy.mainloop() is used
# screen.exitonclick()

df = pd.read_csv("50_states.csv")
# print(df)

timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()

all_states = df['state'].to_list()
guessed_states = []

score = 0
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What is the name of the next state?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        # OR
        # if df["state"].str.contains(answer_state).any():
        guessed_states.append(answer_state)
        score += 1
        row = df[df["state"] == answer_state]
        # print(row)
        # New turtle required, because if turtle.goto() is written,
        # the background image moves with the turtle
        timmy.goto(int(row["x"]), int(row["y"]))
        timmy.write(answer_state)

# Show all un-guessed states in a .csv file
missed_states = []
for states in all_states:
    if states not in guessed_states:
        missed_states.append(states)

with open('Missed States.csv', 'w') as file:
    file.write(str(missed_states))
