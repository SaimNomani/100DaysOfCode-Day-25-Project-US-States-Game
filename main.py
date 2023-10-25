import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_coor(x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
US_states_df = pandas.read_csv('50_states.csv')
US_states_list = US_states_df.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    user_answer = (screen.textinput(title=f"{len(guessed_states)}/{50} States Correct",
                                    prompt="What's another state's name?")).title()
    if user_answer == 'Exit':
        states_left = []
        for state in US_states_list:
            if state not in guessed_states:
                states_left.append(state)
        states_left_data = {
            "States Left": states_left
        }
        states_left_df = pandas.DataFrame(states_left_data)
        states_left_df.to_csv('states_to_learn.csv')
        break
    if user_answer in US_states_list and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        row = US_states_df[US_states_df.state == user_answer]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(float(row.x), float(row.y))
        t.write(f"{row.state.item()}", align='center', font=('Arial', 10, 'bold'))

screen.exitonclick()
