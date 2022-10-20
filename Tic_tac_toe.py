#global variables
    #----instructions----
print("  --: Welcome to Tick Tac Toe :--  \n")

#board List
b_li =['-','-','-','-','-','-','-','-','-']

move = 0
player = 1
winer = 'none'

def board_intrxn():
    print("Following are the locations of the board. ")
    print(" 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 ")

def board():
    print(b_li[0], "|" ,b_li[1], "|" ,b_li[2])
    print(b_li[3], "|" ,b_li[4], "|" ,b_li[5])
    print(b_li[6], "|" ,b_li[7], "|" ,b_li[8])

def invalid():
    global move
    if b_li[move] != '-':
        print("\n You can't Go there! \n Play a right move.")
        mov()

def hwin():
    if b_li[0] == b_li[1] and b_li[2]:
        print(b_li[0]," is winner.")
    elif b_li[3] == b_li[4] and b_li[5]:
        print(b_li[3]," is winner.")
    elif b_li[6] == b_li[7] and b_li[8]:
        print(b_li[6]," is winner.")
    
def vwin():
    if b_li[0] == b_li[3] and b_li[6]:
        print(b_li[0]," is winner.")
    elif b_li[1] == b_li[4] and b_li[7]:
        print(b_li[1]," is winner.")
    elif b_li[2] == b_li[5] and b_li[8]:
        print(b_li[2]," is winner.")
    

def diagwin():
    if b_li[0] == b_li[5] and b_li[8]:
        print(b_li[5]," is winner.")
    elif b_li[2] == b_li[5] and b_li[6]:
        print(b_li[5]," is winner.")
    

def winner():
    hwin()
    vwin()
    diagwin()

def mov():
    board_intrxn()
    board()
    global move
    global player
    global winner
    if player == 1:
        print("X's move.")
        move = int(input(" Enter a no. to go there. ")) - 1
        invalid()
        b_li.insert(move, 'X')
        board()
        winner()
        player=2
        mov()
        
    elif player == 2:
        print("O's move")
        move = int(input(" Enter a no. to go there. ")) - 1
        b_li.insert(move, 'O')
        board()
        winner()
        player=1
        mov()

def game():
    mov()
    


game()
