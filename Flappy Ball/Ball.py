import pgzrun
from random import randint

TITLE ="Flappy Ball"
WIDTH = 700
HEIGHT = 600

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)
CLR = R, G, B

GRAVITY = 2000.0

class Ball():
    def __init__ (self, initial_x, initial_y):
           self.x = initial_x
           self.y = initial_y
           self.vx = 200
           self.vy = 0
           self.radius = 40
    def draw(self):
          pos =(self.x, self.y)
          screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50,100)
ball2 = Ball(90, 200)


def draw():
      screen.clear()
      ball.draw()
      ball2.draw()



def on_key_down(key):
     #pressing a key will kick the ball upwards.
     if key == keys.SPACE:
        ball.vy = -500
     if key == keys.UP:
        ball2.vy = -300
        
def update(dt):
     # Equation of motion = v = u + at  v = final velocity, u = initial velocity, a = acceleration, t = time
     uy = ball.vy
     ball.vy = ball.vy + GRAVITY * dt 
     ball.y = ball.y + (uy + ball.vy) * 0.5 * dt
     # Detect and handle bounce
     if ball.y >= HEIGHT - ball.radius: # We have bounced
          ball.y = HEIGHT - ball.radius # Fix the position at the bottom
          ball.vy = -ball.vy * 0.9 # Inelastic collision
      # x component does not have acceleration

     ball.x = ball.x + ball.vx * dt
     if ball.x >= WIDTH - ball.radius or ball.x  <= ball.radius:
               ball.vx = -ball.vx
     

     uy = ball2.vy
     ball2.vy = ball2.vy + GRAVITY * dt 
     ball2.y = ball2.y + (uy + ball2.vy) * 0.5 * dt
     # Detect and handle bounce
     if ball2.y >= HEIGHT - ball2.radius: # We have bounced
          ball2.y = HEIGHT - ball2.radius # Fix the position at the bottom
          ball2.vy = -ball2.vy * 0.9 # Inelastic collision
      # x component does not have acceleration

     ball2.x = ball2.x + ball2.vx * dt
     if ball2.x >= WIDTH - ball2.radius or ball2.x  <= ball2.radius:
               ball2.vx = -ball2.vx







pgzrun.go()
      





      

     
     

















