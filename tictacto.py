import pprint
import time 

theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " ", }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('' + '-' + ' ' + '-' + ' ' + '-' )
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('' + '-' + ' ' + '-' + ' ' + '-' )
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
print("Lets play a game of Tic-Tac-Toe")

picker  = True


while(picker):
    print("Would you like to be X's or O's")
    global human 
    human = input()
    global computer
    computer = ""
    if human ==  "x" or human == "X":
        computer = "O"
        picker = False
    elif human == "o" or human == "O":
        computer = "X"
        picker = False
    else:
        picker = True

print("You have chosen " + human + ". The computer will be " + computer + "...")

time.sleep(2)

print("The board is now cleared. Lets begin! Moves are top-")

theBoard["top-L"] = human


printBoard(theBoard)

def humanMove(move):
    print("Your turn")
    theBoard[move] = human


humanMove(theBoard)
    
      
#human is asked for input to be X or O, computer is whatever human didnt
#pick  CHECK

#3 fucntions - computer turn, human turn, check win

# computer turn is generated by random number between 1 and 3 for vertical
# and then 1 thru 3 for hoizontal - (first number being the spot vertically,
#second number being the spot horizontally, aka numbers 1 and 2 would generate
# an O or X in the middle area

#human turn is generated by asking user for input on that turn, then comparing
# that input to the key in theBoard dictionary, if user types in top-R,
#O or X is then placed in that area by giving that key (which the use typed in)
# the value of X or O

#computer then goes and runs function again
# after 5 fucntion calls back and forth (computer, human, computer, human, computer)
# the check win fucntion then runs (does not run prior to 5 turns because
#the minimum amount of turns required to win is 5, regardless of who goes first
#then, after every turn after the first 5 turns, checkWin function is ran 
#meaning, function call would  be something like:

#----sequence of functions----
#computer()
#printBoard(theBoard)
#human()
#printBoard(theBoard)
#computer()
#printBoard(theBoard)
#human()
#printBoard(theBoard)
#computer()
#printBoard(theBoard)
#checkwin
#human()
#printBoard(theBoard)
#checkwin
#computer()
#printBoard(theBoard)
#checkwin
#human()
#printBoard(theBoard)
#checkwin
#computer()
#printBoard(theBoard)
#checkwin
#break/end 

#check win fucntion checks all the possible rows and columns  and diagnal
#ways to win. if the vaules for the keys top-L  top-M  top-R match all match,
# aka all 3 are either all X or all O, that respective player wins
#meaning, there are 8 possible ways to win, so there would be 8 if / elif
#statements. if one of those conditions is true, game loop breaks and
#player wins

#if last checkwin fucntion is ran and no conditions are satified and all
#values for each k have something
#game is a draw and asked if wanted to restart 




