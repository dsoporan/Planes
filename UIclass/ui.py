import random

from Controller.BoardsController import Controller
from Repository.BoardsRepo import Board, EmptyBoard, ComputerBoard


def menu():
    print("")
    print("1. Play GAME !\n")
    print("2. Exit GAME !\n")

class UI(object):
    def __init__(self):
        self.board = Board().get_all()
        self.eboard = EmptyBoard().get_all()
        self.cboard = ComputerBoard().get_all()

    def start(self):
        cont = Controller(self.board, self.eboard, self.cboard)
        menu()
        n = int(input("Command:"))
        planes  = 0
        if n == 1:
            cont.printing_list(self.eboard)
            while planes < 2:
                print("\nAdding plane:\n")
                print("Coordinates of Head:")
                x = int(input("row:"))
                y = int(input("column"))
                if x < 1 or x > 8:
                    return
                if y < 1 or y > 8:
                    return

                print("Coordinates of Left Wing:")
                lwx = int(input("row:"))
                lwy = int(input("column"))
                if lwx < 1 or lwx > 8:
                    return
                if lwy < 1 or lwy > 8:
                    return

                print("Coordinates of Right Wing:")
                rwx = int(input("row:"))
                rwy = int(input("column"))
                if rwx < 1 or rwx > 8:
                    return
                if rwy < 1 or rwy > 8:
                    return

                lis = []
                lis.append(x)
                lis.append(y)
                lis.append(lwx)
                lis.append(lwy)
                lis.append(rwx)
                lis.append(rwy)

                poz = cont.check_plane_empty(lis, self.board)
                if poz <= 0:
                    print("Plane not added")
                    return
                cont.adding_plane(lis, poz, self.board)
                planes += 1
                cont.printing_list(self.board)

            cont.computer_planes()
            cont.printing_list(self.cboard)
            print('\n' * 25)
            cont.printing_list(self.board)
            print("\n")
            cont.printing_list(self.eboard)
            print("\n" * 5, "Player Done!")
            print("Computer Done!")
            npHead = 0
            ncHead = 0
            ncHit = 0
            lHx = 0
            lHy = 0
            while npHead < 2 and ncHead < 2:
                print("\nPlayer TURN !\n\n")
                print("HIT: ")
                hx = int(input("Row: "))
                hy = int(input("Column: "))
                if self.cboard[hx][hy] == "x":
                    self.eboard[hx][hy] = "*"
                elif self.cboard[hx][hy] == "_":
                    self.eboard[hx][hy] = "O"
                elif self.cboard[hx][hy] == "X":
                    self.eboard[hx][hy] = "H"
                    npHead += 1
                print("\n\n")
                cont.printing_list(self.board)
                print("\n\n")
                cont.printing_list(self.eboard)

                print("\nComputer TURN !")
                if ncHit == 0 or lHy == 0:
                    cx = random.randrange(1,8)
                    cy = random.randrange(1,8)
                else:
                    r = random.randrange(1,4)
                    if r == 1:
                        if lHx + 1 <= 8 and (self.board[lHx + 1][lHy] != "O" and self.board[lHx + 1][lHy] != "H"):
                            cx = lHx + 1
                            cy = lHy
                        elif lHx - 1 >= 1 and (self.board[lHx - 1][lHy] != "O" and self.board[lHx - 1][lHy] != "H"):
                            cx = lHx - 1
                            cy = lHy
                        elif lHy + 1 <= 8 and (self.board[lHx][lHy + 1] != "O" and self.board[lHx][lHy + 1] != "H"):
                            cy = lHy + 1
                            cx = lHx
                        elif lHy - 1 >= 1 and (self.board[lHx][lHy - 1] != "O" and self.board[lHx][lHy - 1] != "H"):
                            cy = lHy - 1
                            cx = lHx
                        else:
                            cx = random.randrange(1, 8)
                            cy = random.randrange(1, 8)

                    elif r == 2:
                        if lHx - 1 >= 1 and (self.board[lHx - 1][lHy] != "O" and self.board[lHx - 1][lHy] != "H"):
                            cx = lHx - 1
                            cy = lHy
                        elif lHy + 1 <= 8 and (self.board[lHx][lHy + 1] != "O" and self.board[lHx][lHy + 1] != "H"):
                            cy = lHy + 1
                            cx = lHx
                        elif lHy - 1 >= 1 and (self.board[lHx][lHy - 1] != "O" and self.board[lHx][lHy - 1] != "H"):
                            cy = lHy - 1
                            cx = lHx
                        elif lHx + 1 <= 8 and (self.board[lHx + 1][lHy] != "O" and self.board[lHx + 1][lHy] != "H"):
                            cx = lHx + 1
                            cy = lHy
                        else:
                            cx = random.randrange(1, 8)
                            cy = random.randrange(1, 8)
                    elif r == 3:
                        if lHy + 1 <= 8 and (self.board[lHx][lHy + 1] != "O" and self.board[lHx][lHy + 1] != "H"):
                            cy = lHy + 1
                            cx = lHx
                        elif lHy - 1 >= 1 and (self.board[lHx][lHy - 1] != "O" and self.board[lHx][lHy - 1] != "H"):
                            cy = lHy - 1
                            cx = lHx
                        elif lHx + 1 <= 8 and (self.board[lHx + 1][lHy] != "O" and self.board[lHx + 1][lHy] != "H"):
                            cx = lHx + 1
                            cy = lHy
                        elif lHx - 1 >= 1 and (self.board[lHx - 1][lHy] != "O" and self.board[lHx - 1][lHy] != "H"):
                            cx = lHx - 1
                            cy = lHy
                        else:
                            cx = random.randrange(1, 8)
                            cy = random.randrange(1, 8)
                    else:
                        if lHy - 1 >= 1 and (self.board[lHx][lHy - 1] != "O" and self.board[lHx][lHy - 1] != "H"):
                            cy = lHy - 1
                            cx = lHx
                        elif lHx + 1 <= 8 and (self.board[lHx + 1][lHy] != "O" and self.board[lHx + 1][lHy] != "H"):
                            cx = lHx + 1
                            cy = lHy
                        elif lHx - 1 >= 1 and (self.board[lHx - 1][lHy] != "O" and self.board[lHx - 1][lHy] != "H"):
                            cx = lHx - 1
                            cy = lHy
                        elif lHy + 1 <= 8 and (self.board[lHx][lHy + 1] != "O" and self.board[lHx][lHy + 1] != "H"):
                            cy = lHy + 1
                            cx = lHx
                        else:
                            cx = random.randrange(1, 8)
                            cy = random.randrange(1, 8)

                if self.board[cx][cy] == "x":
                    self.board[cx][cy] = "H"
                    ncHit = 1
                    lHx = cx
                    lHy = cy
                elif self.board[cx][cy] == "_":
                    self.board[cx][cy] = "O"
                elif self.board[cx][cy] == "X":
                    self.board[cx][cy] = "D"
                    ncHead += 1
                    ncHit = 1
                print("\n\n")
                cont.printing_list(self.board)


            if npHead == 2:
                print("Player WINS!")
                print("\n\n")
                cont.printing_list(self.board)
                print("\n\n")
                cont.printing_list(self.cboard)
                return
            elif ncHead == 2:
                print("Computer WINS!")
                print("\n\n")
                cont.printing_list(self.board)
                print("\n\n")
                cont.printing_list(self.cboard)
                return

        elif n == 2:
            return

UI().start()
