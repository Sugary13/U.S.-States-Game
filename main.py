import turtle
import pandas

screen = turtle.Screen()
text = turtle.Turtle()

data = pandas.read_csv("50_states.csv")

guess_list = []
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_list = data.state.to_list()
x_list = data.x.to_list()
y_list = data.y.to_list()
text.hideturtle()
text.penup()


correct_answers = 0

while correct_answers < 50:
    answer_state = screen.textinput(title= f"{correct_answers}/50 States Correct",
                                             prompt="What is another the state's name?")
    if not answer_state:
        break
    else:
        answer_state = answer_state.title()

    if answer_state in states_list and answer_state not in guess_list:
        guess_list.append(answer_state)
        answer_index = states_list.index(answer_state)
        x = x_list[answer_index]
        y = y_list[answer_index]
        text.goto(x, y)
        text.write(answer_state)
        print(f"{answer_state} is correct!.")
        correct_answers += 1

    else:
        print(f"{answer_state} is not correct or you already guessed it.")





screen.exitonclick()





