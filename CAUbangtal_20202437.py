from bangtal import *

#about scene1
scene1 = Scene("룸1", './images/image6/배경-1.png')

door1 = Object("./images/image6/문-오른쪽-닫힘.png")
door1.locate(scene1,800,270)
door1.show()
door1_closed = True

key = Object("./images/image6/열쇠.png")
key.setScale(0.2)
key.locate(scene1, 600, 150)
key.show()

pot = Object("./images/image6/화분.png")
pot.setScale(1)
pot.locate(scene1, 550, 150)
pot.show()

memo = Object("./images/Pimages/메모1.png")
memo.setScale(0.05)
memo.locate(scene1, 200, 600)
memo.show()

#about scene2
scene2 = Scene("룸2", "./images/image6/배경-2.png")

door2 = Object("./images/image6/문-왼쪽-열림.png")
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object("./images/image6/문-오른쪽-닫힘.png")
door3.locate(scene2, 920, 270)
door3.show()
door3_closed = True
door3_locked = True

pad = Object("./images/image6/키패드.png")
pad.locate(scene2, 900, 400)
pad.setScale(1.5)
pad.show()

rock = Object("./images/Pimages/돌1.png")
rock.locate(scene2, 620, 200)
rock.setScale(0.8)
rock.show()

hammer = Object("./images/Pimages/해머2.png")
hammer.locate(scene2, 300, 50)
hammer.setScale(0.1)
hammer.show()

def door1_onMouseAction(x,y,action):
    global door1_closed
    if door1_closed == True:
        if key.inHand():
            door1.setImage("./images/image6/문-오른쪽-열림.png")
            door1_closed = False
        else:
            showMessage("열쇠가 필요할 것 같다.")
    elif door1_closed == False :
        scene2.enter()

def key_onMouseAction(x,y,action):
    key.pick()

def hammer_onMouseAction(x,y,action):
    hammer.pick()


def pot_onMouseAction(x,y,action):
    if action == MouseAction.DRAG_LEFT:
        pot.locate(scene1, 450, 150)
    elif action == MouseAction.DRAG_RIGHT:
        pot.locate(scene1, 750, 150)
    else :
        showMessage("화분을 밀 수 있을 것 같다.")

def door2_onMouseAction(x,y,action):
    scene1.enter()

def door3_onMouseAction(x,y,action):
    global door3_closed
    if door3_locked:
        showMessage("문이 잠겨있다.")

    elif door3_closed:
        door3.setImage("./images/image6/문-오른쪽-열림.png")
        showMessage("문이 열렸다")
        door3_closed = False

    else:
        endGame()

def rock_onMouseAction(x,y,action):
    if hammer.inHand():
        rock.hide()
        #rock = 620, 200
        cobble1 = Object("./images/Pimages/돌2.png")
        cobble2 = Object("./images/Pimages/돌2.png")
        cobble1.locate(scene2, 800, 250)
        cobble2.locate(scene2, 1000, 250)
        cobble1.setScale(0.2)
        cobble2.setScale(0.2)
        cobble1.show()
        cobble2.show()
    else :
        showMessage("도구가 있다면 부술 수 있을 듯 하다.")

def pad_onMouseAction(x,y,action):
    showKeypad("0485", door3)

def memo_onMouseAction(x,y,action):
    showMessage("'0485'라고 적혀있다.")

def door3_onKeypad():
    global door3_locked
    door3_locked = False
    showMessage("철컥")




pot.onMouseAction = pot_onMouseAction
door1.onMouseAction = door1_onMouseAction
key.onMouseAction = key_onMouseAction
hammer.onMouseAction = hammer_onMouseAction
door2.onMouseAction = door2_onMouseAction
door3.onMouseAction = door3_onMouseAction
rock.onMouseAction = rock_onMouseAction
pad.onMouseAction = pad_onMouseAction
memo.onMouseAction = memo_onMouseAction
door3.onKeypad = door3_onKeypad


startGame(scene1)

