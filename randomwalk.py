import turtle as t
import random
abhi = t.Turtle();
directions = (0,90,180,270)
abhi.pensize(20)
abhi.speed(10)
abhi.color("brown")
for _ in range(200):
    abhi.forward(30)
    abhi.setheading(random.choice(directions))
