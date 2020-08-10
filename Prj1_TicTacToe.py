#@@@ 2016104142 컴퓨터공학과 이광원 - AIHW1.py @@@

#user의 보드, ai의 보드, 탐색 카운터 기록을 list로 선언
user, ai, searches, search = [], [], [], -1
#초기 게임보드 선언
board = list(range(1,10))
#user를 MAX Player(첫 차례)로 설정
c_Player = True

#player가 승리 조건을 가지고 있는지 확인
def check_winner(player):
    #틱택토 승리조건
    winCases = [[1,2,3], [1,4,7], [1,5,9], [2,5,8], 
        [3,5,7], [3,6,9], [4,5,6], [7,8,9]]
    for case in winCases:
        check = 0
        #리스트 비교
        for i in range(3):
            if case[i] in player:
                check += 1
        if check == 3:  #승리조건에 부합하는 경우
            return True
    return False
#게임의 결과 분석, 탐색한 노드 수 계산
def evaluation():
    global search
    search += 1
    if check_winner(user):
        return 1    #user 승리
    elif check_winner(ai):
        return -1   #ai 승리
    else:
        return 0    #비김
#현재 게임 보드 출력
def print_board():
    for i in range(3):
        for j in range(3):
            item = i*3+j+1
            if item in board:   #빈 box
                print("[ ]", end =" ")
            elif item in user:  #user의 box
                print("[X]", end =" ")
            else:   #ai의 box
                print("[O]", end =" ")
        print("")
#틱택노 게임의 미니맥스 알고리즘
def minimax(player):
    pos = -1
    #게임이 종료된 경우
    if len(board) == 0 or check_winner(user) or check_winner(ai):
        return -1, evaluation()
    if player:  #Max Player
        value = -100    #음의 무한대로 시작
        for box in board:
            move(board, user, box)
            x, score = minimax(False)   #Min Player로 전환
            move(user, board, box)
            if score > value:   #value와 위치 결정
                value = score
                pos = box
    else:       #Min Player
        value = +100    #양의 무한대로 시작
        for box in board:
            move(board, ai, box)
            x, score = minimax(True)    #Max Player로 전환
            move(ai, board, box)
            if score < value:   #value와 위치 결정
                value = score
                pos = box
    return pos, value
#각 Player의 차례 실행, 결과 확인 및 출력
def turn(player):
    if player : #user의 차례
        n = int(input("Make a move:")) #input으로 Box 선택
        move(board, user, n)
        print_board()
        return check_winner(user)
    else:       #ai의 차례
        n, x = minimax(False) #미니맥스 알고리즘으로 Box 선택
        #탐색한 노드 수 출력
        print("AI made a move. Number of nodes searched:", search)
        move(board, ai, n)
        print_board()   #결과 출력
        return check_winner(ai)
#l1에서 l2로 box 소유권 이동
def move(l1, l2, num):
    l1.remove(num)
    l2.append(num)
    l2.sort() #비교를 위해 list 정렬
#메인 프로그램
print_board() #초기 게임보드 출력
while 1:
    search = 0 #탐색 횟수 초기화
    if len(board) == 0: #승자 없이 게임 종료
        print("Result: Draw")
        break
    #Player 차례 실행, 승자가 있는지 확인
    if turn(c_Player):
        if c_Player:    #user 승리
            print("Result: You Win")
            break
        else:           #ai 승리 
            print("Result: AI Win")
            break
    #승자가 없으면 다음 player로 전환
    else:
        if c_Player:    #Max → Min 전환
            c_Player = False
        else:           #Min → Max 전환
            searches.append(search) #탐색횟수 기록
            c_Player = True
#프로세스 내 총 탐색 횟수 출력
print("Total number of nodes searched:", sum(searches))
input() #종료 대기