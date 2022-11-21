import turtle
ablak=turtle.Screen()
ablak.bgcolor("lightgreen")
Teknőske=turtle.Turtle()
Teknőske.shape("turtle")
Teknőske.color("brown")
Teknőske.speed(1)

import 
    
#Abbreviations:


cont = turtle.logic.getCurrentController()
player = cont.owner
keyboard = turtle.logic.keyboard


iAct = turtle.logic.KX_INPUT_ACTIVE


pvel = player.linearVelocity


wkey = keyboard.events[turtle.events.WKEY]
skey = keyboard.events[turtle.events.SKEY]
akey = keyboard.events[turtle.events.AKEY]
dkey = keyboard.events[turtle.events.DKEY]


#Base values:
#This is the base speed for character movement. Change only this and the whole script will remain proportional:


bs = 10


wmove = bs
smove = -0.4*bs
amove = -0.8*bs
dmove = 0.8*bs


awdmove = 0.6*bs
asdmove = 0.3*bs


#Always do this:


player.setLinearVelocity((0, 0, 0), True)
print(pvel)


#Defining the groundMove function:
def groundMove():
    
    #Main Directions:
    if iAct == wkey:
        player.setLinearVelocity((0, wmove, 0), True)
        
    if iAct == skey:
        player.setLinearVelocity((0, smove, 0), True)
        
    if iAct == akey:
        player.setLinearVelocity((amove, 0, 0), True)
        
    if iAct == dkey:
        player.setLinearVelocity((dmove, 0, 0), True)
        
    #Diagonal directions:
    if iAct == wkey and dkey:
        player.setLinearVelocity((awdmove, awdmove, 0), True)
        
    if iAct == wkey and akey:
        player.setLinearVelocity((-1 * awdmove, awdmove, 0), True)
        
    if iAct == skey and dkey:
        player.setLinearVelocity((asdmove, -1 * asdmove, 0), True)
        
    if iAct == skey and akey:
        player.setLinearVelocity((-1 * asdmove, -1 * asdmove, 0), True)
         
groundMove()