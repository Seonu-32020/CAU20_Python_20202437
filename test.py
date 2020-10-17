from bangtal import *

x = 300
y = 300


scene = Scene("S", "./images/Cardgame_images/BG_grass720.png")



bt1 = Object("./images/Cardgame_images/playing_cards/1S.png")
bt1.locate(scene, 10, 10)
bt1.show()

bt2 = Object("./images/Cardgame_images/playing_cards/13D.png")
bt2.locate(scene, 10, 200)
bt2.show()

ob1 = Object("./images/Cardgame_images/playing_cards/10S.png")
ob1.locate(scene, x, y)


ob2 = Object("./images/Cardgame_images/playing_cards/10D.png")
ob2.locate(scene, x, y)


def bt1_onMouseAction(x, y, action):
    ob1.hide()
    ob1.show()
    print("changed bt1 - S")

def bt2_onMouseAction(x, y, action):
    ob2.hide()
    ob2.show()
    print("changed bt2 - D")


bt1.onMouseAction = bt1_onMouseAction
bt2.onMouseAction = bt2_onMouseAction




startGame(scene)