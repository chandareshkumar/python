import turtle
import math
import os as o


w=turtle.Screen()
w.bgcolor("Black")
w.title("Space Invaders")



border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
      border_pen.fd(600)
      border_pen.lt(90)
border_pen.hideturtle()

#create player turtle

player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0,-250)



playerspeed=15


#enemy

enemy=turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,200)
enemyspeed=2


bullet=turtle.Turtle()
bullet.color("Yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)

bullet.hideturtle()

bulletspeed=20
bulletstate="ready"

def move_left():
	x = player.xcor()
	x-= playerspeed
	if x<-280:
	   x=-280


	player.setx(x)	


def move_right():
	x = player.xcor()
	x += playerspeed
	if x> 280:
	   x= 280

	player.setx(x)		

def fire_bullet():
	global bulletstate
	if bulletstate=="ready":
		bulletstate="fire"
		x=player.xcor()
		y=player.ycor()+20
		bullet.setposition(x,y)
		bullet.showturtle()


def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
    	return True
    else:
    	return False


turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")


while True:

	x=enemy.xcor()
	x+=enemyspeed
	enemy.setx(x)

	if enemy.xcor()>280:
		y=enemy.ycor()
		y-=40
		enemyspeed *=-1
		enemy.sety(y)

	if enemy.xcor()<-280:
		y=enemy.ycor()
		y-=40
		enemyspeed *=-1
		enemy.sety(y)

	if bulletstate=="fire":	
		y=bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)   


	if bullet.ycor()>275:
		bullet.hideturtle()
		bulletstate="ready"
	if isCollision(bullet, enemy):
		#Reset the bullet
		bullet.hideturtle()
		bulletstate="ready"
		bullet.setposition(0,-400)
		#Reset the enemy
		enemy.setposition(-200,250)


	if isCollision(player,enemy):
		player.hideturtle()
		enemy.hideturtle()
		print("Game Over")
       
    

d=input("Press any key")