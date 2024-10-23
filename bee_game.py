import pgzrun 

WIDTH = 600
HEIGHT = 500

bee= Actor("bee")
bee.pos = 100,100
flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("background",(0,0))
    
    bee.draw()
    flower.draw()

def update():
    if keyboard.left:
        bee.x= bee.x-2
    if keyboard.right:
        bee.x= bee.x+2
    if keyboard.up:
        bee.y= bee.y-2
    if keyboard.down:
        bee.y= bee.y+2
        
pgzrun.go()  