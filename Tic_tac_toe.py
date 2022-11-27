    #----instructions----
print("  --: Welcome to Tick Tac Toe :--  \n")

#board List
b_li =['-','-','-','-','-','-','-','-','-']

move = 0
player = 1
winner = 'none'

def board():
    print(b_li[0], "|" ,b_li[1], "|" ,b_li[2],"          1 | 2 | 3 ")
    print(b_li[3], "|" ,b_li[4], "|" ,b_li[5],"          4 | 5 | 6 ")
    print(b_li[6], "|" ,b_li[7], "|" ,b_li[8],"          7 | 8 | 9 ")

def invalid():
    global move
    if b_li[move] != '-':
        print("\n You can't Go there! \n Play a right move.")
        mov()

def winer():
    hwin()
    vwin()
    diagwin()

def hwin():
    if b_li[0] == b_li[1] == b_li[2] != '-':
        print(b_li[0]," is winner.")
        winner= b_li[0]
    elif b_li[3] == b_li[4] == b_li[5] != '-':
        print(b_li[3]," is winner.")
        winner= b_li[3]
    elif b_li[6] == b_li[7] == b_li[8] != '-':
        print(b_li[6]," is winner.")
        winner= b_li[6]
    else:
        winner= 'none'
    
def vwin():
    if b_li[0] == b_li[3] == b_li[6] != '-':
        print(b_li[0],"is winner.")
        winner= b_li[0]
    elif b_li[1] == b_li[4] == b_li[7] != '-':
        print(b_li[1]," is winner.")
        winner= b_li[1]
    elif b_li[2] == b_li[5] == b_li[8] != '-':
        print(b_li[2]," is winner.")
        winner= b_li[2]
    else:
        winner= 'none'

def diagwin():
    if b_li[0] == b_li[5] == b_li[8] != '-':
        print(b_li[5]," is winner.")
        winner= b_li[5]
    elif b_li[2] == b_li[5] == b_li[6] != '-':
        print(b_li[5]," is winner.")
        winner= b_li[5]
    else:
        winner= 'none'

def mov():
    board()
    global move
    global player
    if player == 1:
        print("X's move.")
        move = int(input(" Enter a no. to go there. ")) - 1
        invalid()
        b_li.insert(move, 'X')
        winer()
        player=2
        
    else:
        print("O's move")
        move = int(input(" Enter a no. to go there. ")) - 1
        invalid()
        b_li.insert(move, 'O')
        winer()
        player=1
    

def game():
    global winner
    while winner == 'none':
        mov()
game()
print(winner)
    


