import random


class Controller(object):
    def __init__(self, board, eboard, cboard):
        self.board = board
        self.eboard = eboard
        self.cboard = cboard

    def printing_list(self, l):
        for i in l:
            print(*i)

    def check_plane_empty(self, lis, map):
        # HEAD CHECKING
        if map[lis[0]][lis[1]] != "_":
            return 0

        if lis[2] == lis[4]:
            if lis[3] > lis[5]:
                if lis[3] - lis[5] == 4:
                    # FACE DOWN
                    # HEAD CHECKING
                    if lis[1] * 2 != lis[3] + lis[5]:
                        return 0
                    if lis[0] != lis[2] + 1:
                        return 0
                    # WINGS CHECKING
                    if map[lis[2]][lis[3]] != "_":
                        return 0
                    if map[lis[2]][lis[3] - 1] != "_":
                        return 0
                    if map[lis[2]][lis[3] - 2] != "_":
                        return 0
                    if map[lis[2]][lis[3] - 3] != "_":
                        return 0
                    if map[lis[4]][lis[5]] != "_":
                        return 0
                    # BODY ANT TAIL CHECKING
                    if lis[2] - 2 >= 1 and lis[3] - 3 >= 1:
                        if map[lis[2] - 1][lis[3] - 2] != "_":
                            return 0
                        if map[lis[2] - 2][lis[3] - 1] != "_":
                            return 0
                        if map[lis[2] - 2][lis[3] - 2] != "_":
                            return 0
                        if map[lis[2] - 2][lis[3] - 3] != "_":
                            return 0
                    else:
                        return -1
                    return 1
                else:
                    return -1
            else:
                if lis[5] - lis[3] == 4:
                    # FACE UP
                    # HEAD CHECKING
                    if lis[1] * 2 != lis[3] + lis[5]:
                        return 0
                    if lis[0] != lis[2] - 1:
                        return 0
                    # WINGS CHECKING
                    if map[lis[2]][lis[3]] != "_":
                        return 0
                    if map[lis[2]][lis[3] + 1] != "_":
                        return 0
                    if map[lis[2]][lis[3] + 2] != "_":
                        return 0
                    if map[lis[2]][lis[3] + 3] != "_":
                        return 0
                    if map[lis[4]][lis[5]] != "_":
                        return 0
                    # BODY ANT TAIL CHECKING
                    if lis[2] + 2 <= 8 and lis[3] + 3 <= 8:
                        if map[lis[2] + 1][lis[3] + 2] != "_":
                            return 0
                        if map[lis[2] + 2][lis[3] + 1] != "_":
                            return 0
                        if map[lis[2] + 2][lis[3] + 2] != "_":
                            return 0
                        if map[lis[2] + 2][lis[3] + 3] != "_":
                            return 0
                    else:
                        return -1
                    return 2
        else:
            if lis[3] == lis[5]:
                if lis[2] > lis[4]:
                    if lis[2] - lis[4] == 4:
                        # FACE LEFT
                        # HEAD CHECKING
                        if lis[0] * 2 != lis[2] + lis[4]:
                            return 0
                        if lis[1] != lis[3] - 1:
                            return 0
                        # WINGS CHECKING
                        if map[lis[2]][lis[3]] != "_":
                            return 0
                        if map[lis[2] - 1][lis[3]] != "_":
                            return 0
                        if map[lis[2] - 2][lis[3]] != "_":
                            return 0
                        if map[lis[2] - 3][lis[3]] != "_":
                            return 0
                        if map[lis[4]][lis[5]] != "_":
                            return 0
                        # BODY AND TAIL CHECKING
                        if lis[2] - 3 >= 1 and lis[3] + 2 <= 8:
                            if map[lis[2] - 2][lis[3] + 1] != "_":
                                return 0
                            if map[lis[2] - 1][lis[3] + 2] != "_":
                                return 0
                            if map[lis[2] - 2][lis[3] + 2] != "_":
                                return 0
                            if map[lis[2] - 3][lis[3] + 2] != "_":
                                return 0
                        else:
                            return -1
                        return 3
                    else:
                        return -1
                else:
                    if lis[4] - lis[2] == 4:
                        # FACE RIGHT
                        # HEAD CHECKING
                        if lis[0] * 2 != lis[2] + lis[4]:
                            return 0
                        if lis[1] != lis[3] + 1:
                            return 0
                        # WINGS CHECKING
                        if map[lis[2]][lis[3]] != "_":
                            return 0
                        if map[lis[2] + 1][lis[3]] != "_":
                            return 0
                        if map[lis[2] + 2][lis[3]] != "_":
                            return 0
                        if map[lis[2] + 3][lis[3]] != "_":
                            return 0
                        if map[lis[4]][lis[5]] != "_":
                            return 0
                        # BODY ANT TAIL CHECKING
                        if lis[2] - 2 >= 1 and lis[2] + 3 <= 8 and lis[3] - 2 >= 1:
                            if map[lis[2] - 2][lis[3] - 1] != "_":
                                return 0
                            if map[lis[2] + 1][lis[3] - 2] != "_":
                                return 0
                            if map[lis[2] + 2][lis[3] - 2] != "_":
                                return 0
                            if map[lis[2] + 3][lis[3] - 2] != "_":
                                return 0
                        else:
                            return -1
                        return 4
                    else:
                        return -1
        return -1
    def adding_plane(self, lis, poz, map):
        if poz == 1:
            # FACE DOWN
            # Head
            map[lis[0]][lis[1]] = "X"
            # Wings
            map[lis[2]][lis[3]] = "x"
            map[lis[2]][lis[3] - 1] = "x"
            map[lis[2]][lis[3] - 2] = "x"
            map[lis[2]][lis[3] - 3] = "x"
            map[lis[4]][lis[5]] = "x"
            # BODY ANT TAIL CHECKING
            map[lis[2] - 1][lis[3] - 2] = "x"
            map[lis[2] - 2][lis[3] - 1] = "x"
            map[lis[2] - 2][lis[3] - 2] = "x"
            map[lis[2] - 2][lis[3] - 3] = "x"
        elif poz == 2:
            # FACE UP
            # Head
            map[lis[0]][lis[1]] = "X"
            # WINGS
            map[lis[2]][lis[3]] = "x"
            map[lis[2]][lis[3] + 1] = "x"
            map[lis[2]][lis[3] + 2] = "x"
            map[lis[2]][lis[3] + 3] = "x"
            map[lis[4]][lis[5]] = "x"
            # BODY ANT TAIL CHECKING
            map[lis[2] + 1][lis[3] + 2] = "x"
            map[lis[2] + 2][lis[3] + 1] = "x"
            map[lis[2] + 2][lis[3] + 2] = "x"
            map[lis[2] + 2][lis[3] + 3] = "x"
        elif poz == 3:
            # FACE LEFT
            # Head
            map[lis[0]][lis[1]] = "X"
            # Wings
            map[lis[2]][lis[3]] = "x"
            map[lis[2] - 1][lis[3]] = "x"
            map[lis[2] - 2][lis[3]] = "x"
            map[lis[2] - 3][lis[3]] = "x"
            map[lis[4]][lis[5]] = "x"
            # BODY AND TAIL CHECKING
            map[lis[2] - 2][lis[3] + 1] = "x"
            map[lis[2] - 1][lis[3] + 2] = "x"
            map[lis[2] - 2][lis[3] + 2] = "x"
            map[lis[2] - 3][lis[3] + 2] = "x"
        elif poz == 4:
            # FACE RIGHT
            # Head
            map[lis[0]][lis[1]] = "X"
            # Wings
            map[lis[2]][lis[3]] = "x"
            map[lis[2] + 1][lis[3]] = "x"
            map[lis[2] + 2][lis[3]] = "x"
            map[lis[2] + 3][lis[3]] = "x"
            map[lis[4]][lis[5]] = "x"
            # BODY ANT TAIL CHECKING
            map[lis[2] + 2][lis[3] - 1] = "x"
            map[lis[2] + 1][lis[3] - 2] = "x"
            map[lis[2] + 2][lis[3] - 2] = "x"
            map[lis[2] + 3][lis[3] - 2] = "x"

    def computer_planes(self):
        planes = 0
        while planes < 2:
            x = random.randrange(1,8)
            y = random.randrange(1,8)
            poz = random.randrange(1,4)

            lis = []
            lis.append(x)
            lis.append(y)
            if poz == 1:
                if x - 1 >= 1 and y + 2 <= 8 and y - 2 >= 1:
                    lis.append(x - 1)
                    lis.append(y + 2)
                    lis.append(x - 1)
                    lis.append(y - 2)
                else:
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
            elif poz == 2:
                if x + 1 <= 1 and y + 2 <= 8 and y - 2 >= 1:
                    lis.append(x + 1)
                    lis.append(y - 2)
                    lis.append(x + 1)
                    lis.append(y + 2)
                else:
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
            elif poz == 3:
                if x - 2 >= 1 and x + 2 <= 8 and y + 1 <= 8:
                    lis.append(x + 2)
                    lis.append(y + 1)
                    lis.append(x - 2)
                    lis.append(y + 1)
                else:
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
            else:
                if x - 2 >= 1 and x + 2 <= 8 and y - 1 >= 1:
                    lis.append(x - 2)
                    lis.append(y - 1)
                    lis.append(x + 2)
                    lis.append(y - 1)
                else:
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)
                    lis.append(1)

            if self.check_plane_empty(lis, self.cboard) > 0:
                self.adding_plane(lis, poz, self.cboard)
                planes += 1



