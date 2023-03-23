from turtle import Turtle
import turtle

import pandas
import pandas as pd
screen = turtle.Screen()
counter=0
not_written_states={"state":[]}
written_states=[]
text=Turtle()
text.penup()
text.hideturtle()
screen.title("U.S States Game ")
image="blank_states_img.gif"
screen.addshape(image)
data = pd.read_csv("50_states.csv")
turtle.shape(image)
while counter!=50:
    answer_state=screen.textinput(title=f"{counter}/50 States Correct" ,prompt= "What's another state name ?  ").title()
    if answer_state =='Exit':
        break
    if answer_state in data["state"].to_string(index=False) and answer_state not in written_states:
        x = int(data[data["state"]==answer_state]["x"].to_string(index = False))
        y = int(data[data["state"]==answer_state]["y"].to_string(index = False))
        text.setpos(x,y)
        text.write(answer_state)
        counter+=1
        written_states.append(answer_state)
states = data["state"].values.tolist()
# for state in states:
#     if state not in written_states:
#         not_written_states["state"].append(state)
not_written_states = [state for state in data.state if state not in written_states ]
not_written_states = pandas.DataFrame(not_written_states)
not_written_states.to_csv("states_to_learn.csv")

