from bangtal import *
import time

#monitor = 1280 * 720

count = 0
startcheck = 0

ranklist = open('./Slidegame/Rank.txt', 'a')



scene1 = Scene("slide puzzle", "./images/SlidegameImages/IMGcut/cuttedimageOriginal.jpg")

puz0 = Object("./images/SlidegameImages/numpuz/puz0.png")
puz1 = Object("./images/SlidegameImages/IMGcut/cuttedimage1.jpg")
puz2 = Object("./images/SlidegameImages/IMGcut/cuttedimage2.jpg")
puz3 = Object("./images/SlidegameImages/IMGcut/cuttedimage3.jpg")
puz4 = Object("./images/SlidegameImages/IMGcut/cuttedimage4.jpg")
puz5 = Object("./images/SlidegameImages/IMGcut/cuttedimage5.jpg")
puz6 = Object("./images/SlidegameImages/IMGcut/cuttedimage6.jpg")
puz7 = Object("./images/SlidegameImages/IMGcut/cuttedimage7.jpg")
puz8 = Object("./images/SlidegameImages/IMGcut/cuttedimage8.jpg")
puz9 = Object("./images/SlidegameImages/IMGcut/cuttedimage9.jpg")
puz10 = Object("./images/SlidegameImages/IMGcut/cuttedimage10.jpg")
puz11 = Object("./images/SlidegameImages/IMGcut/cuttedimage11.jpg")
puz12 = Object("./images/SlidegameImages/IMGcut/cuttedimage12.jpg")
puz13 = Object("./images/SlidegameImages/IMGcut/cuttedimage13.jpg")
puz14 = Object("./images/SlidegameImages/IMGcut/cuttedimage14.jpg")
puz15 = Object("./images/SlidegameImages/IMGcut/cuttedimage15.jpg")

clear = Object("./images/SlidegameImages/numpuz/Clear_Button.png")
clear.locate(scene1, 1170, 500)
clear.show()

end = Object("./images/SlidegameImages/numpuz/End_Button.png")
end.locate(scene1, 1170, 400)
end.show()

start = Object("./images/SlidegameImages/numpuz/Start_Button.png")
start.locate(scene1, 10, 500)
start.show()

reset = Object("./images/SlidegameImages/numpuz/Rank_Reset.png")
reset.locate(scene1, 1060, 500)
reset.show()

puzanswer = [[puz0, puz1, puz2, puz3],
             [puz4, puz5, puz6, puz7],
             [puz8, puz9, puz10, puz11],
             [puz12, puz13, puz14, puz15]]

puzpiece = [[puz4, puz12, puz2, puz3],
            [puz5, puz1, puz6, puz7],
            [puz13, puz0, puz9, puz14],
            [puz8, puz11, puz15, puz10]]

puz0.x, puz0.y = 100, 100
puz0.locate(scene1, puz0.x, puz0.y)
puz0.setScale(0.5)
puz0.show()

puz1.x, puz1.y = 100, 200
puz1.locate(scene1, puz1.x, puz1.y)
puz1.setScale(1)
puz1.show()

puz2.x, puz2.y = 200, 300
puz2.locate(scene1, puz2.x, puz2.y)
puz2.setScale(1)
puz2.show()

puz3.x, puz3.y = 300, 300
puz3.locate(scene1, puz3.x, puz3.y)
puz3.setScale(1)
puz3.show()

puz4.x, puz4.y = 0, 300
puz4.locate(scene1, puz4.x, puz4.y)
puz4.setScale(1)
puz4.show()

puz5.x, puz5.y = 0, 200
puz5.locate(scene1, puz5.x, puz5.y)
puz5.setScale(1)
puz5.show()

puz6.x, puz6.y = 200, 200
puz6.locate(scene1, puz6.x, puz6.y)
puz6.setScale(1)
puz6.show()

puz7.x, puz7.y = 300, 200
puz7.locate(scene1, puz7.x, puz7.y)
puz7.setScale(1)
puz7.show()

puz8.x, puz8.y = 0, 0
puz8.locate(scene1, puz8.x, puz8.y)
puz8.setScale(1)
puz8.show()

puz9.x, puz9.y = 200, 100
puz9.locate(scene1, puz9.x, puz9.y)
puz9.setScale(1)
puz9.show()

puz10.x, puz10.y = 300, 0
puz10.locate(scene1, puz10.x, puz10.y)
puz10.setScale(1)
puz10.show()

puz11.x, puz11.y = 100, 0
puz11.locate(scene1, puz11.x, puz11.y)
puz11.setScale(1)
puz11.show()

puz12.x, puz12.y = 100, 300
puz12.locate(scene1, puz12.x, puz12.y)
puz12.setScale(1)
puz12.show()

puz13.x, puz13.y = 0, 100
puz13.locate(scene1, puz13.x, puz13.y)
puz13.setScale(1)
puz13.show()

puz14.x, puz14.y = 300, 100
puz14.locate(scene1, puz14.x, puz14.y)
puz14.setScale(1)
puz14.show()

puz15.x, puz15.y = 200, 0
puz15.locate(scene1, puz15.x, puz15.y)
puz15.setScale(1)
puz15.show()

def find():
    x = 0
    y = 0

    for i in range(4):
        for k in range(4):
            if puzpiece[y][x] == puz0 :
                return x, y
            else :
                x += 1
        x = 0
        y += 1


def claer_onMouseAction(x, y, action):
    global count
    global oldtime
    global startcheck
    global ranklist

    if startcheck == 1:
        if puzpiece == puzanswer:
            now = time.localtime()
            nowtime = 3600 * int(now.tm_hour) + 60 * int(now.tm_min) + int(now.tm_sec)

            timepass = nowtime - oldtime

            nowmin = int(timepass/60)
            nowsec = int(timepass%60)
            ranktext = str(timepass) + ","
            ranklist.write(ranktext)
            ranklist.close()

            ranklist = open("./Slidegame/Rank.txt", 'r')
            rank = ranklist.read().split(",")
            rank.sort()
            rank.pop(0)

            rank = list(map(int, rank))
            rank.sort()

            print(rank)

            if timepass == rank[0]:
                Message = str(count) + "번만에 성공!\n" + str(nowmin) + "분 " + str(nowsec) + "초 경과! 신기록 갱신!"

            else:
                Message = str(count) + "번만에 성공!\n" + str(nowmin) + "분 " + str(nowsec) + "초 경과!"

            showMessage(Message)

        else :
            showMessage("퍼즐을 완성해주세요! 하얀 조각이 가장 왼쪽 위에 있어야만 합니다!")




    else :
        showMessage("게임시작을 클릭한 후 퍼즐을 맞춰주세요")

def end_onMouseAction(x, y, action):
    endGame()

def reset_onMouseAction(x, y, action):
    rankl = open('./Slidegame/Rank.txt', 'w')
    rankl.close()

    endGame()

def start_onMouseAction(x, y, action):
    global startcheck
    global old
    global oldtime

    if startcheck == 0:
        showMessage("타이머 작동 시작\n 하얀 조각이 가장 왼쪽 위에 있어야 합니다")
        old = time.localtime()
        oldtime = 3600 * int(old.tm_hour) + 60 * int(old.tm_min) + int(old.tm_sec)
    startcheck = 1

def puz0_onMouseAction(x, y, action):
    puzx, puzy = find()
    global count

    if startcheck == 0:
        showMessage("게임 시작 버튼을 먼저 눌러주세요")

    elif action == MouseAction.DRAG_RIGHT:
        if puzx < 3 :

            count += 1
            puzpiece[puzy][puzx].x += 100
            puzpiece[puzy][puzx].locate(scene1, puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)
            #print("puz0 = ", puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)

            puzpiece[puzy][puzx + 1].x = puzpiece[puzy][puzx + 1].x - 100
            puzpiece[puzy][puzx + 1].locate(scene1, puzpiece[puzy][puzx + 1].x, puzpiece[puzy][puzx + 1].y)
            #print("puzr = ", puzpiece[puzy][puzx + 1].x, puzpiece[puzy][puzx + 1].y)


            puzpiece[puzy][puzx], puzpiece[puzy][puzx + 1] = puzpiece[puzy][puzx + 1], puzpiece[puzy][puzx]

    elif action == MouseAction.DRAG_LEFT:
        if puzx > 0 :

            count += 1
            puzpiece[puzy][puzx].x -= 100
            puzpiece[puzy][puzx].locate(scene1, puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)
            #print("puz0 = ", puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)

            puzpiece[puzy][puzx - 1].x += 100
            puzpiece[puzy][puzx - 1].locate(scene1, puzpiece[puzy][puzx- 1].x, puzpiece[puzy][puzx - 1].y)
            #print("puzl = ", puzpiece[puzy][puzx - 1].x, puzpiece[puzy][puzx - 1].y)



            puzpiece[puzy][puzx], puzpiece[puzy][puzx - 1] = puzpiece[puzy][puzx - 1], puzpiece[puzy][puzx]

    elif action == MouseAction.DRAG_UP:
        if puzy > 0 :

            count += 1
            puzpiece[puzy][puzx].y += 100
            puzpiece[puzy][puzx].locate(scene1, puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)
           # print("puz0 = ", puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)

            puzpiece[puzy - 1][puzx].y -= 100
            puzpiece[puzy - 1][puzx].locate(scene1, puzpiece[puzy - 1][puzx].x, puzpiece[puzy - 1][puzx].y)
           # print("puzu = ", puzpiece[puzy - 1][puzx].x, puzpiece[puzy - 1][puzx].y)


            puzpiece[puzy][puzx], puzpiece[puzy - 1][puzx] = puzpiece[puzy - 1][puzx], puzpiece[puzy][puzx]

    elif action == MouseAction.DRAG_DOWN:
        #print("doww on")
        if puzy < 3 :

            count += 1
            puzpiece[puzy][puzx].y -= 100
            puzpiece[puzy][puzx].locate(scene1, puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)
            #print("puz0 = ", puzpiece[puzy][puzx].x, puzpiece[puzy][puzx].y)

            puzpiece[puzy + 1][puzx].y += 100
            puzpiece[puzy + 1][puzx].locate(scene1, puzpiece[puzy + 1][puzx].x, puzpiece[puzy + 1][puzx].y)
            #print("puzd = ", puzpiece[puzy + 1][puzx].x, puzpiece[puzy + 1][puzx].y)



            puzpiece[puzy][puzx], puzpiece[puzy + 1][puzx] = puzpiece[puzy + 1][puzx], puzpiece[puzy][puzx]

    else:
        showMessage("드래그해서 퍼즐을 밀어보자\n하얀 조각은 가장 왼쪽 위에 있어야 한다")




puz0.onMouseAction = puz0_onMouseAction
start.onMouseAction = start_onMouseAction
clear.onMouseAction = claer_onMouseAction
end.onMouseAction = end_onMouseAction
reset.onMouseAction = reset_onMouseAction

startGame(scene1)