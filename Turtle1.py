import turtle 
sc=turtle.Screen()
sc.bgcolor("black")
sc.setup(400,500)
turtle.title("Welcome to turtle window")
T=turtle.Turtle()
T.speed("fastest")
T.hideturtle()
colors=['pink','red','green','brown','blue','yellow','orange','violet']
for i in range(5):
    for j in range(8):
        T.pencolor(colors[j])
        for k in range(360):
            T.forward(i+1)
            T.right(1)
        T.right(360/8)

