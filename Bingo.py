#Each player takes turns to guess one number and all players cross the number out on the board
#When a row, column, or diagonal is fully crossed it counts as 1 when a player totals 5 then the player is the winner.

import random
class Board:
    def __init__(self):
        self.position = {}
        self.playBoard = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]
        self.bingo = {
            "row" : [0,0,0,0,0],
            "col" : [0,0,0,0,0],
            "diagonal" : [0,0]
        }
        self.createBoard()
        
    def createBoard(self): #used to create the game board and stores the position of each cell in the dictionary
        choices = [i for i in range(1,26)] #choices are numbers 1-26
        for i in range(5):
            for j in range(5):
                choice = random.choice(choices) #randomly selects a number in the range 1-5
                self.playBoard[i][j] = choice #i,j indicate coordinates in the board
                choices.pop(choices.index(choice))
                self.position[choice] = (i,j) #assigns the coordinate i,j the value choices
    
    def updateBoard(self, val): #Used to update the board when a player guesses a number; calls the player and a value
        x,y = self.position[val] #value input is assigned to x,y coordinates
        self.playBoard[x][y] = 'X' #value at x,y is replaced with 'X'
        self.updateBingo(x,y)
    
    def updateBingo(self, x, y): #used to update a dictionary to update Bingo#
        self.bingo["row"][x] += 1 #if row x has an 'X', add one
        self.bingo["col"][y] += 1 #if row y has an 'X', add one
        if x==y==2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x==y: #else if
            self.bingo["diagonal"][0] += 1
        elif x+y == 4:
            self.bingo["diagonal"][1] += 1
    
    def checkBingo(self): #check to see if a player got bingo or not#
        return 5 in self.bingo["row"] or 5 in self.bingo["col"] or 5 in self.bingo["diagonal"]
        #check if the total of each value is 5, if it's 5, there's a bingo
    
#create new class to update player's board with new number
class Player(Board): 
    def __init__(self, name):
        self.name = name
        self.board = Board()
    
    def updatePlayerBoard(self, val):
        self.board.updateBoard(val)
    
    def checkBingo(self): #checks if the player got bingo
        return self.board.checkBingo()
    
#Game class to implement game functionalities
class Game:
    def displayBoard(self, player1, player2): #prints player's board each turn
        board1 = player1.board.playBoard
        board2 = player2.board.playBoard
        size = 20
        p1len = len(player1.name)
        print(player1.name+" "*(size-p1len+1)+player2.name)
        for i in range(5):
            for j in board1[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print("      ",end="")
            for j in board2[i]:
                if j=='X':
                    print(f" {j}",end=" ")
                elif j>9:
                    print(j,end=" ")
                else:
                    print(f"0{j}",end=" ")
            print()
        print()

#create game instance with two players
game = Game()
player1 = Player(name="player1")
player2 = Player(name="player2")

#Gameplay logic
game.displayBoard(player1, player2)
while True:
    val = int(input(f"{player1.name}'s turn : ")) #Each player inputs a number
    player1.updatePlayerBoard(val)
    player2.updatePlayerBoard(val)
    game.displayBoard(player1,player2)
    if player1.checkBingo() and player2.checkBingo():
        print("DRAW")
        break
    if player1.checkBingo():
        print(f"{player1.name} WON")
        break
    if player2.checkBingo():
        print(f"{player2.name} WON")
        break
    
    val = int(input(f"{player1.name}'s turn : "))
    player1.updatePlayerBoard(val)
    player2.updatePlayerBoard(val)
    game.displayBoard(player1,player2)
    if player1.checkBingo() and player2.checkBingo():
        print("DRAW")
        break
    if player1.checkBingo():
        print(f"{player1.name} WON")
        break
    if player2.checkBingo():
        print(f"{player2.name} WON")
        break
