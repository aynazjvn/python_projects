import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

states = data["state"].tolist()
guessed_states = []
# remained_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                              prompt="What's another state's name").title()
    if answer == "Exit":
        remained_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         remained_states.append(state)
        data_to_learn = pandas.DataFrame(remained_states)
        data_to_learn.to_csv("states_to_learn.csv")

        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)





