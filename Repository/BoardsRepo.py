from Tools.allTools import initialize_list


class Board(object):
    def __init__(self):
        self.board = initialize_list()

    def get_all(self):
        return self.board

class ComputerBoard(object):
    def __init__(self):
        self.board = initialize_list()

    def get_all(self):
        return self.board

class EmptyBoard(object):
    def __init__(self):
        self.eboard = initialize_list()

    def get_all(self):
        return self.eboard