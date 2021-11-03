# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
fill_color = "blue"
shape_size = 3
shape = "triangle"
score = 0
font_setup = ("Arial",20,"normal")
timer = 30
counter_interval = 1000
timer_up = False
list = ["green","red","yellow"]
new_color = [1,2,3]
#-----initialize turtle-----
painter = trtl.Turtle()
painter.shape("triangle")
painter.shapesize(3)
painter.fillcolor("blue")

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-375,290)

counter = trtl.Turtle()
#-----game functions--------
def painter_clicked(x,y):
    if timer > 0:
        update_score()
        change_position()
        random_color(x)
        random_shape(y)
    else:
        painter.hideturtle()
def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    painter.penup() 
    painter.goto(new_xpos,new_ypos)
def update_score():
    global score
    score+=1
    score_writer.clear()
    score_writer.write(score,font=font_setup)
def countdown():
    counter.hideturtle()
    global timer, timer_up
    counter.clear()
    counter.penup()
    counter.goto(-50,290)
    if timer <= 0:
        counter.write("Time's up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def random_color(x):
    x = rand.randint(0,2)
    wn.bgcolor(list[x])
def random_shape(y):
    y = rand.randint(0,2)
    painter.shapesize(new_color[y])
#-----events----------------
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
painter.onclick(painter_clicked)
wn.mainloop()