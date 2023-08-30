import turtle
import pandas

data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()
print(state_list)
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

mark = turtle.Turtle()
mark.color('black')
mark.speed('fastest')
mark.penup()
mark.hideturtle()

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title="Guess the State", prompt="What's another state's name")
    answer = answer.title()

    if answer == 'Exit':
        missing_state = [n for n in state_list if n not in guessed_states ]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in state_list:
        guessed_states.append(answer)
        state_data = data[data.state == answer]
        mark.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        mark.write(answer)

screen.exitonclick()
