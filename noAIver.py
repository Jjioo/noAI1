
import random

from termcolor import colored
class TicTacTow:

    def __init__(self, board: dict):
        self.board = board
        self.player = colored('X','red')
        self.bot = colored('O','green')
    def printBoard(self, board) -> None:
        print(board[1] + '|' + board[2] + '|' + board[3])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[7] + '|' + board[8] + '|' + board[9])
        print(colored("-----",'yellow'))
    def spaceIsFree(self, position: int) -> bool:
        if self.board[position] == ' ':
            return True
        return False

    def insertLetter(self, letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard(self.board)

            if (self.checkDraw()):
                print('draw!!')
                exit(0)

            if (self.checkWin()):
                if letter == 'X':
                    print('bot win !!')
                    exit(0)
                else:
                    print('you win !!')
                    exit(0)
            return

        else:
            print('cant insert here !!')
        position = int(input("enter position! :"))
        self.insertLetter(letter, position)

    def insertLetterBot(self, letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard(self.board)

            if (self.checkDraw()):
                print('draw!!')
                exit(0)

            if (self.checkWin()):
                if letter == 'X':
                    print('bot win !!')
                    exit(0)
                else:
                    print('you win !!')
                    exit(0)
            return

        else:
            print('cant insert here !!')
        position = random.randint(1,9)
        self.insertLetterBot(letter, position)

    def checkDraw(self)->bool:
        for key in self.board.keys():
            if self.board[key]==' ':
                return False
        else:

             return True

    def checkWin(self)->bool:
        if (self.board[1] == self.board[2] and self.board[1] == self.board[3] and self.board[1] != ' '):
            return True
        elif (self.board[4] == self.board[5] and self.board[4] == self.board[6] and self.board[4] != ' '):
            return True
        elif (self.board[7] == self.board[8] and self.board[7] == self.board[9] and self.board[7] != ' '):
            return True
        elif (self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[1] != ' '):
            return True
        elif (self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[2] != ' '):
            return True
        elif (self.board[3] == self.board[6] and self.board[3] == self.board[9] and self.board[3] != ' '):
            return True
        elif (self.board[1] == self.board[5] and self.board[1] == self.board[9] and self.board[1] != ' '):
            return True
        elif (self.board[7] == self.board[5] and self.board[7] == self.board[3] and self.board[7] != ' '):
            return True
        else:
            return False


    def playerMove(self):
        position = int(input("enter position for 'X'! :"))
        self.insertLetter(self.player,position)
        return
    def compMove(self):
        position = random.randint(1,9)
        self.insertLetterBot(self.bot,position)
        return


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '
         }

board1 = {1: '1', 2: '2', 3: '3',
         4: '4', 5: '5', 6: '6',
         7: '7', 8: '8', 9: '9'
         }
t = TicTacTow(board=board)
t1 = TicTacTow(board=board1)

t.printBoard(board1)
while not t.checkWin():
    t.compMove()
    t.playerMove()
