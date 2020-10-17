from bangtal import *
import time
import random
from time import *

table = Scene("CAU-RD Game", "./images/Cardgame_images/BG_grass720.png")



deck = []
hand_ai = []
hand_player = []
top_card = (0, 0)
able = 1 # able 1 = ok / 0 = not ok
draw_count = 0
acetwocount = 0

turn = 0  # turn 0 = player, 1 = Ai

#--------------------------------------------------button start---------------------------------------------------------
button_img_path = "./images/Cardgame_images/put_button.png"

button0 = Object(button_img_path)
button1 = Object(button_img_path)
button2 = Object(button_img_path)
button3 = Object(button_img_path)
button4 = Object(button_img_path)
button5 = Object(button_img_path)
button6 = Object(button_img_path)
button7 = Object(button_img_path)
button8 = Object(button_img_path)
button9 = Object(button_img_path)
buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9]

button_draw = Object("./images/Cardgame_images/playing_cards/back_blue.png")
button_draw.locate(table, 1170, 290)
button_draw.show()

button_start = Object("./images/Cardgame_images/StartButton.png")
button_start.locate(table, 320, 176)
button_start.show()

YouLose = Object("./images/Cardgame_images/YouLose.png")
YouLose.locate(table, 320, 176)

YouWin = Object("./images/Cardgame_images/YouWin.png")
YouWin.locate(table, 320, 178)

YouDraw = Object("./images/Cardgame_images/YouDraw.png")
YouDraw.locate(table, 320, 176)

def display_buttons(table):
    global  button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttons, button_img_path


    space = 10
    y = 173
    print("buttons displayed")
    for i in range(0, 10, 1):
        buttons[i].locate(table, space * (i + 1) + 100 * i, y)
        buttons[i].show()

def button0_onMouseAction(x, y, action):
    print("button 1")
    if len(hand_player) > 0 :
        print("Ok")
        if able_check(hand_player[0]):
            put_card(hand_player.pop(0))
        else:
            showMessage("그 카드는 낼 수 없다")

def button1_onMouseAction(x, y, action):
    print("button 1")
    if len(hand_player) > 1 :
        print("Ok")
        if able_check(hand_player[1]):
            put_card(hand_player.pop(1))
        else:
            showMessage("그 카드는 낼 수 없다")

def button2_onMouseAction(x, y, action):
    print("button 2")
    if len(hand_player) > 2 :
        print("Ok")
        if able_check(hand_player[2]):
            put_card(hand_player.pop(2))
        else:
            showMessage("그 카드는 낼 수 없다")

def button3_onMouseAction(x, y, action):
    print("button 3")
    if len(hand_player) > 3 :
        print("Ok")
        if able_check(hand_player[3]):
            put_card(hand_player.pop(3))
        else:
            showMessage("그 카드는 낼 수 없다")

def button4_onMouseAction(x, y, action):
    print("button 4")
    if len(hand_player) > 4 :
        print("Ok")
        if able_check(hand_player[4]):
            put_card(hand_player.pop(4))
        else:
            showMessage("그 카드는 낼 수 없다")

def button5_onMouseAction(x, y, action):
    print("button 5")
    if len(hand_player) > 5 :
        print("Ok")
        if able_check(hand_player[5]):
            put_card(hand_player.pop(5))
        else:
            showMessage("그 카드는 낼 수 없다")

def button6_onMouseAction(x, y, action):
    print("button 6")
    if len(hand_player) > 6 :
        print("Ok")
        if able_check(hand_player[6]):
            put_card(hand_player.pop(6))
        else:
            showMessage("그 카드는 낼 수 없다")

def button7_onMouseAction(x, y, action):
    print("button 7")
    if len(hand_player) > 7 :
        print("Ok")
        if able_check(hand_player[7]):
            put_card(hand_player.pop(7))
        else:
            showMessage("그 카드는 낼 수 없다")

def button8_onMouseAction(x, y, action):
    print("button 8")
    if len(hand_player) > 8 :
        print("Ok")
        if able_check(hand_player[8]):
            put_card(hand_player.pop(8))
        else:
            showMessage("그 카드는 낼 수 없다")

def button9_onMouseAction(x, y, action):
    if len(hand_player) > 9 :
        print("10장이면 게임이 끝나야 하는데?")


def button_draw_onMouseAction(x, y, action):
    print("DRAW fucntion")
    if turn == 0:
        if draw_count > 0 :
            draw(hand_player, draw_count)
        else:
            draw(hand_player, 1)

def button_start_onMouseClick(x, y, action):
    #game start button
    global deck

    make_deck(deck)
    hand_set(deck)
    display_hand_player(table)
    display_hand_ai(table)
    display_buttons(table)
    display_top(table, deck.pop(0))
    button_start.hide()

button0.onMouseAction = button0_onMouseAction
button1.onMouseAction = button1_onMouseAction
button2.onMouseAction = button2_onMouseAction
button3.onMouseAction = button3_onMouseAction
button4.onMouseAction = button4_onMouseAction
button5.onMouseAction = button5_onMouseAction
button6.onMouseAction = button6_onMouseAction
button7.onMouseAction = button7_onMouseAction
button8.onMouseAction = button8_onMouseAction
button9.onMouseAction = button9_onMouseAction
button_draw.onMouseAction = button_draw_onMouseAction
button_start.onMouseAction = button_start_onMouseClick

#--------------------------------------------------button end  ---------------------------------------------------------

#-----------------------------------------------display functions-------------------------------------------------------

def display_hand_player(table):
    print("display hand player")
    print("hand player = ", hand_player)

    space = 10
    y = 10
    bg = Object("./images/Cardgame_images/BG_grass_player.png")
    bg.locate(table, 0, 0)
    bg.show()

    for i in range(0, len(hand_player), 1):
        img_path = "./images/Cardgame_images/playing_cards/" + hand_player[i][0] + hand_player[i][1] + ".png"
        card = Object(img_path)
        card.locate(table, space * (i + 1) + 100 * i, y)
        card.show()

def display_hand_ai(table):
    print("display hand ai")
    print("hand ai = ", hand_ai)

    space = 10
    y = 520
    bg = Object("./images/Cardgame_images/BG_grass_ai.png")
    bg.locate(table, 0, 510)
    bg.show()
    for i in range(0, len(hand_ai), 1):
        img_path = "./images/Cardgame_images/playing_cards/back_blue.png"
        card = Object(img_path)
        card.locate(table, space * (i + 1) + 100 * i, y)
        card.show()

def display_top(table, card_info):
    # type 0 = start base / 1 = from player hand / 2 = from ai hand
    # table = scene / card_info = tuple info
    print("display top")
    global deck
    global top_card

    card_x = 590
    card_y = 290
    top_card = card_info
    print("top card = ", top_card)


    img_path = "./images/Cardgame_images/playing_cards/" + card_info[0] + card_info[1] + ".png"
    card = Object(img_path)
    card.locate(table, card_x, card_y)
    card.show()

#-----------------------------------------------display functions-------------------------------------------------------

def make_deck(deck):
    print("make deck")
    symbol = ["C", "D", "H", "S"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

    for i in range(0, 52, 1):
        deck.append((num[(i % 13)], symbol[(i % 4)]))
    random.shuffle(deck)
    print(deck)

def hand_set(deck):
    print("hand set")
    for i in range (0, 5, 1):
        hand_player.append(deck.pop(0))
        hand_ai.append(deck.pop(0))
    print("Player : ", hand_player)
    print("Ai     : ", hand_ai)

def draw(hand, count):
    # cardnum = number of draws (ex - if cardnum = 2, draw 2 cards)
    print("draw")
    global turn
    global deck
    global draw_count
    global acetwocount

    if count == 0 :
        count = 1

    for i in range(0, count, 1):
        hand.append(deck.pop(0))

    display_hand_player(table)
    display_hand_ai(table)
    display_buttons(table)

    text = str(len(deck)) + "장의 카드가 덱에 남았습니다."
    showMessage(text)

    draw_count = 0

    if turn == 0:
        turn = 1
        ai_turn(top_card)
    else:
        turn = 0
    acetwocount = 1
    winlose()

def able_check(card_info):
    if turn == 0:
        print("player able check\n")
    if turn == 1:
        print("Ai able check\n")

    top_number = top_card[0]
    top_symbol = top_card[1]
    print("top num = ", top_number, "/ top symbol = ", top_symbol, "/ card info = ", card_info)

    if top_number == '2':
        if (card_info[0] == '2') or ((card_info[0] == '1') and (card_info[1] == top_symbol)):
            return 1
        else:
            return 0
    elif top_number == '1':
        if card_info[0] == '1':
            return 1
        else:
            return 0
    elif (card_info[0] == top_number) or (card_info[1] == top_symbol):
        return 1
    else:
        return 0

def ai_turn(top_card):
    global turn
    global hand_ai
    putcount = 0

    if turn == 1:
        for i in range(len(hand_ai) - 1, -1, -1):
            if able_check(hand_ai[i]):
                print("ai able checked : ", hand_ai[i])
                put_card(hand_ai.pop(i))
                putcount += 1
                break
        if putcount == 0:
            draw(hand_ai, draw_count)
    else:
        print("\nError : ai_turn while turn == 0\n")
    turn = 0
    display_hand_ai(table)

def put_card(card_info):
    #card_info have to be hand.pop(x)
    global turn
    global top_card
    global draw_count
    global acetwocount
    putcount = 1

    print("PUT - Player hand = ", hand_player)
    print("PUT - AI hand     = ", hand_ai)
    if able_check(card_info):
        if turn == 0:
            # player turn
            top_card = card_info
            for i in range(len(hand_player)-1, -1, -1):
                # 배열 뒤부터 같은 수 찾기 -> 한번에 Put
                if card_info[0] == hand_player[i][0]:
                    top_card = hand_player.pop(i)
                    print("Top_card in put_card = ", top_card)
                    putcount += 1
            display_top(table, top_card)
            winlose()

        else:
            # AI turn
            if able_check(card_info):
                top_card = card_info
                display_top(table, card_info)
                winlose()

        if card_info[0] == '2':
            draw_count += 2 * putcount
        elif card_info[0] == '1':
            draw_count += 3 * putcount

        display_hand_player(table)
        acetwocount = 0

        if turn == 0:
            turn = 1
            print("turn changed ( 0 -> 1 )\n")
            ai_turn(top_card)
        elif turn == 1:
            turn = 0
            print("turn changed ( 1 -> 0 )\n")




def winlose():
    print("win lose check")
    if len(hand_ai) >= 10 or len(hand_player) == 0:
        youwin = Object("./images/Cardgame_images/YouWin.png")
        youwin.locate(table, 320, 176)
        youwin.show()
        showMessage("5초 후 게임이 종료됩니다")
        sleep(5)
        endGame()
    elif len(hand_player) >= 10 or len(hand_ai) == 0:
        youlose = Object("./images/Cardgame_images/YouLose.png")
        youlose.locate(table, 320, 176)
        youlose.show()
        showMessage("5초 후 게임이 종료됩니다")
        sleep(5)
        endGame()

startGame(table)
