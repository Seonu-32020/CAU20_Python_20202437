from bangtal import *

bg = Scene("Othello", "./Images/background.png")

boardlist = []  # 이미지
gameboard = []  # 숫자배열

turn = 1   # 1 = black, 2 = white
index_x = 0
index_y = 0
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def game_board_init():
    global boardlist
    global gameboard

    boardlist = [[0]*8 for i in range(8)]
    t = 8//2
    boardlist[t][t] = 2
    boardlist[t][t-1] = 1
    boardlist[t-1][t-1] = 2
    boardlist[t-1][t] = 1

    gameboard = [[0]*8 for i in range(8)]
    t = 8 // 2
    gameboard[t][t] = 2
    gameboard[t][t - 1] = 1
    gameboard[t - 1][t - 1] = 2
    gameboard[t - 1][t] = 1

    ## 0 = blank / 1 = black / 2 = white / 3 = black poss / 4 = white poss

def stone_onMouseAction():
    print("a")

def display_game_board():
    global boardlist
    x = 40
    y = 40
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            # stone = boardlist[i][j]
            if boardlist[i][j] == 0 or gameboard[i][j] == 0:
                boardlist[i][j] = Object("./Images/blank.png")
            elif boardlist[i][j] == 1 or gameboard[i][j] == 1:
                boardlist[i][j] = Object("./Images/black.png")
            elif boardlist[i][j] == 2 or gameboard[i][j] == 2:
                boardlist[i][j] = Object("./Images/white.png")
            boardlist[i][j].locate(bg, 40 + 80 * j, 600 - 80 * i)
            boardlist[i][j].show()


game_board_init()
display_game_board()
print(boardlist)

def find_index(Object, x, y, action):
    global index_x
    global index_y
    global turn

    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            if Object == boardlist[i][j]:
                print(i,j)
                index_x, index_y = i, j

    if gameboard[index_x][index_y] == 0:
        if turn == 1 :
            #gameboard[index_x][index_y] = 1
            board_put(index_x, index_y, 1)
            display_game_board()
            display_points()
            return

        elif turn == 2:
            #gameboard[index_x][index_y] = 2
            board_put(index_x, index_y, 2)
            display_game_board()
            display_points()
            return


def check_pos(x, y, color):
    global gameboard
    N = 7
    # 이동이 벽을넘어가면
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    # 돌이없으면
    if gameboard[x][y] == 0:
        return 0
    # 자기돌이라면
    if gameboard[x][y] == color:
        return 2
    # 상대돌이라면
    return 1

def board_put(x, y, color):
    global gameboard, dx, dy, turn
    l = 0

    for i in range(8):
        # 어디방향으로 이동할지 설정한다.
        d_x = dx[i]
        d_y = dy[i]
        # 상대방 돌을 내돌로 바꾸는 리스트 생성
        change_list = []
        # 반복문을 통해 체크한다.
        while True:
            # 이동할 경로를 체크한다.
            a = check_pos(x + d_x, y + d_y, color)
            # 리턴이 0일때이며, 돌이없거나 벽이동을 못할때이다 -> 반복문 종료
            if a == 0:
                break
            # 나와 같은색상의 돌을 만났을때이다.
            if a == 2:
                # 지금까지 저장했던 상대방돌을을 내돌로 바꾼다.
                # 반복문을 중지한다.
                for c_x, c_y in change_list:
                    gameboard[c_x][c_y] = color
                break
            #상대방의 돌을 만났을때이다.
            #리스트에 상대방 돌정보를 저장한다.
            if a == 1:
                change_list.append([x + d_x, y + d_y])
                l = len(change_list)
            #반복이 진행될때마다 한칸씩 진행한다.
            d_x += dx[i]
            d_y += dy[i]

    #놓은 돌을 처리한다.
    gameboard[x][y] = color
    if color == 1:
        turn = 2
    elif color == 2:
        turn = 1

def display_points():
    global gameboard, boardlist
    b = gameboard.count(1)
    w = gameboard.count(2)

    print(b, w)

Object.onMouseActionDefault = find_index


startGame(bg)