import time, random
import picodisplay as display 

width = display.get_width()
height = display.get_height()
maxballs = 20
ballcount = maxballs
display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display.init(display_buffer)

display.set_backlight(1.0)


class Ball:
    def __init__(self, x, y, r, dx, dy, pen):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.pen = pen
        
class Bat:
    def __init__(self, y):
        self.y = y
        
class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = False
        

        

# initialise shapes
balls = []
for i in range(0, maxballs):
    #r = random.randint(0, 10) + 3
    r = 7
    balls.append(
        Ball(
            random.randint(0,width),
            random.randint(0,height),
            random.randint(0,10) + 5,
            random.randint(0,255) / 128,
            random.randint(0,255) / 128,
            display.create_pen(random.randint(75, 200), random.randint(75, 200), random.randint(75, 200))          
        )
    )
bat = Bat(1)
missile = Missile(width-20,0)
#display.set_led(0,150,0)



while True:
    display.set_pen(40, 40, 40)
    display.clear()
    
    #while ballcount>0:
    print(ballcount)       
    for ball in balls:
        ball.x += ball.dx
        ball.y += ball.dy

        if ball.x < 0 or ball.x > width:
            ball.dx *= -1

        if ball.y < 0 or ball.y > height:
            ball.dy *= -1
                
        if missile.active:
            if(ball.x > missile.x - ball.r and ball.x < missile.x + ball.r) and (ball.y > missile.y - ball.r and ball.y < missile.y + ball.r):
                missile.active=False
                display.set_pen(255,255,255)
                display.circle(int(ball.x), int(ball.y), int(ball.r)+5)
                ball.dx = 0
                ball.dy = 0
                ball.x = 400
                ball.y = 400
                ballcount = ballcount-1
                print(ballcount)#maxballs = maxballs-1

        display.set_pen(ball.pen)
        display.circle(int(ball.x), int(ball.y), int(ball.r))
        
    if display.is_pressed(display.BUTTON_Y) and bat.y < height- 25:
        bat.y = bat.y +1
    if display.is_pressed(display.BUTTON_X) and bat.y > 0:
        bat.y = bat.y -1
    display.set_pen(100,100,100)
    display.rectangle(width-10,bat.y,10,20)
        
    if missile.active:
      display.rectangle(missile.x,missile.y, 20, 5)
      if missile.x>-10:
          missile.x -=4
      else:
          missile.active=False
    if display.is_pressed(display.BUTTON_A):
        if not missile.active:
            missile.x=width-20
            missile.y=bat.y+10
        missile.active=True
           
    if display.is_pressed(display.BUTTON_B):
        balls = []
        ballcount=maxballs
        for i in range(0, maxballs):
            balls.append(
                Ball(
                random.randint(0,width),
                random.randint(0,height),
                random.randint(0,10) + 5,
                random.randint(0,255) / 128,
                random.randint(0,255) / 128,
                display.create_pen(random.randint(75, 200), random.randint(75, 200), random.randint(75, 200))           
        )
    )    
    display.update()
    
    #time.sleep(0.01)
