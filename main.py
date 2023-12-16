import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

df_states = pd.read_csv("50_states.csv")
states = df_states['state'].to_list()


score = 0
wrong_answer = 0

while wrong_answer < 6:
    screen.update()
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another states's name").title()
    if answer_state in states:
        score += 1
        x = df_states['x'][df_states["state"] == answer_state].to_list()
        y = df_states['y'][df_states["state"] == answer_state].to_list()
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.pu()
        t1.goto(x[0], y[0])
        t1.write(answer_state, align='center',
                 font=("Courier", 10, "normal"))

        states.remove(answer_state)
    else:
        wrong_answer += 1


t2 = turtle.Turtle()
t2.hideturtle()
t2.pu()
t2.goto(0, 0)
t2.write(f"Limit reached ! Your Score is {score}", align='center',
         font=("Courier", 24, "normal"))


remaining_states = pd.DataFrame({'state': states})
remaining_states.to_csv('states_to_learn.csv')


screen.exitonclick()
