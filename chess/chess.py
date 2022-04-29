

class Gamestate():

    board = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR'],
    ]

    def __init__(self):
        
        

        self.whiteToMove = True
        self.moveLog = []

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = '--'
        self.board[move.endrow][move.endcol] = move.piecemove
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

class Move():

    rankstorows = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

    rowstoranks = {v: k for k, v in rankstorows.items()}

    filestocols = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}

    colstofiles = {v: k for k, v in filestocols.items()}


    def __init__(self, strsq, endsq, board):
        self.startrow = strsq[0]
        self.startcol = strsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemove = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]



    def getchessnotaion(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.colstofiles[c] + self.rowstoranks[r]