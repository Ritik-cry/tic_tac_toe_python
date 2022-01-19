# Creating 2 Player Tic Tac Toe game

def display_board(b):
    print('  |   |')
    print(b[1]+' | '+b[2]+' | '+b[3]) 
    print('--|---|--')
    print(b[4]+' | '+b[5]+' | '+b[6])
    print('--|---|--')
    print(b[7]+' | '+b[8]+' | '+b[9])
    print('  |   |')

def place_marker(b,m):
    while True:
        pos=int(input("Choose position(1-9): "))
        if b[pos]==' ':
            b[pos]=m
            break
        else:
            print('Enter empty slots')

def game_result(b,m):
    win=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for i in win:
        if (b[i[0]],b[i[1]],b[i[2]])==(m,m,m):
            return True
    return False        

def details():
    Player1=input("Enter first player name: ")
    Player2=input("Enter second player name: ")
    print(f"{Player1} will choose 'X' ")
    print(f"{Player2} will choose 'O' ")
    return (Player1,Player2)

def game():
    turn=0
    p1,p2=details()
    for i in range(9):
        display_board(board)
        if turn%2==0:
            print(f"{p1} turn ('X')")
            place_marker(board,'X')
            res=game_result(board,'X')
            if res:
                display_board(board)
                print(f"***{p1} win***")
                break
            else:
                turn+=1
        else:
            print(f"{p2} turn ('O')")
            place_marker(board,'O')
            res=game_result(board,'O')
            if res:
                display_board(board)
                print(f"***{p2} win***")
                break
            else:
                turn+=1
    else:
        display_board(board)
        print("It's a tie")


board=[' ']*10
game()
