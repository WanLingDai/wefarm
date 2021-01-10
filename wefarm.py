import turtle
wn = turtle.Screen()

farmer = turtle.Turtle()
farmer.shape("turtle")
farmer.penup()
farmer.back(70)

wheat = turtle.Turtle()
wheat.hideturtle()
wheat.penup()
wheat.shape("circle")
wheat.color("yellow")
wheat.back(90)
wheat.showturtle()


customer1 = turtle.Turtle()
customer1.hideturtle()
customer1.shape("turtle")
customer1.penup()
customer1.color("green")
customer1.forward(100)
customer1.left(90)
customer1.forward(30)
customer1.left(90)
customer1.showturtle()

customer2 = turtle.Turtle()
customer2.hideturtle()
customer2.shape("turtle")
customer2.penup()
customer2.color("blue")
customer2.forward(100)
customer2.right(90)
customer2.forward(30)
customer2.right(90)
customer2.showturtle()

customer1.write("I'll like to buy your wheat for $2.\n",font = ("Arial", 16, "normal"))
customer2.write("I'll like to buy your wheat for $3.\n",font = ("Arial", 16, "normal"))

answer = wn.textinput("","Would you like to 'sell for $2' or 'sell for $3' or 'not sell'?")

if answer == "sell for $2":
    farmer.write("I'll sell it for $2.\n", font = ("Arial", 16, "normal"))
    wheat.hideturtle()
    wheat.forward(210)
    wheat.left(90)
    wheat.forward(30)
    wheat.showturtle()
    customer1.undo()
    customer1.write("Thank you!\n", font = ("Arial", 16, "normal"))
    
elif answer == "sell for $3":
    farmer.write("I'll sell it for $3.\n", font = ("Arial", 16, "normal"))
    wheat.hideturtle()
    wheat.forward(210)
    wheat.right(90)
    wheat.forward(30)
    wheat.showturtle()
    customer2.undo()
    customer2.write("Thank you!\n", font = ("Arial", 16, "normal"))
    
elif answer == "not sell":
    farmer.write("Sorry, I'm not selling\n", font = ("Arial", 16, "normal"))

else:
    print("wrong input")
    


wn.mainloop()
