#/usr/bin/python2.7

#Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.
#
#The rules of the game are:
# 1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# 2. Any live cell with more than three live neighbours dies, as if by overcrowding.
# 3. Any live cell with two or three live neighbours lives on to the next generation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell.

# Each cell's neighborhood is the 8 cells immediately around it.
# The universe is infinite in both the x and y dimensions and all cells are initially dead -
# except for those specified in the arguments.
# The return value should be a 2d array cropped around all of the living cells.
# (If there are no living cells, then return [[]].)
#
# For illustration purposes, 0 and 1 will be represented as 1 and 0 blocks respectively.
# You can take advantage of the htmlize function to get a text representation of the universe: eg:
#    print htmlize(cells)
def htmlize(array):
    s = []
    for row in array:
        s.append('\t')
        for cell in row:
            s.append('1' if cell else '0')
        s.append('\n')
    return ''.join(s)

class Cell(object):
    DEAD = 0
    ALIVE = 1

    def __init__(self, status):
        self.isAlive = status

    def next_gen(self, nbNeighbours):
        self.isAlive = self.next_living_status(nbNeighbours)
        return self.isAlive
    
    def next_living_status(self, nbNeighbours):
        return 1 if (self.should_stay_alive(nbNeighbours) or self.should_be_born(nbNeighbours)) else 0
                             
    def should_stay_alive(self, nbNeighbours):
        return self.isAlive and (nbNeighbours == 2 or nbNeighbours == 3)

    def should_be_born(self, nbNeighbours):
        return not self.isAlive and nbNeighbours == 3

    def __str__(self):
        return str(self.isAlive)

class Board(list):
    def column(self, i):
        return [row[i] for row in self]

    def trim(self):
        while not self[0].count(Cell.ALIVE):
            self.pop(0)
        while not self[-1].count(Cell.ALIVE):
            self.pop(-1)
        while not self.column(0).count(Cell.ALIVE):
            [row.pop(0) for row in self]
        while not self.column(-1).count(Cell.ALIVE):
            [row.pop(-1) for row in self]
        return self
    
class GameOfLife(object):    
    def __init__(self, cells):
        self.set_board(Board(cells))

    def set_board(self, newBoard):
        self.board = newBoard
        self.xmax = len(newBoard)
        self.ymax = len(newBoard[0])
        
    def next_n_gen(self, generations):
        if not generations:
            return self.board
        newBoard = Board()
        for x in range(-1, self.xmax + 1):
            newBoard.append(self.gen_nth_row(x))
        self.set_board(newBoard.trim())
        return self.next_n_gen(generations-1)
            
    def gen_nth_row(self, n):
        row = []
        for y in range(-1, self.ymax + 1):
            nbNeighbours = self.compute_neighbours(n, y)
            cell = Cell(self.board[n][y]) if self.is_inside(n, y) else Cell(Cell.DEAD)
            row.append(cell.next_gen(nbNeighbours))
        return row
        
    def compute_neighbours(self, x, y):
        nbNeighbours = 0
        for testedX in range(x - 1, x + 2):
            for testedY in range(y - 1, y + 2):
                if(self.is_valid_neighbour(x, y, testedX, testedY)):
                    nbNeighbours += 1
        return nbNeighbours

    def is_valid_neighbour(self, originX, originY, neighbourX, neighbourY):
        return not self.is_origin_cell(originX, originY, neighbourX, neighbourY) and self.is_inside(neighbourX, neighbourY) and self.board[neighbourX][neighbourY]

    def is_inside(self, x, y):
        return  x >= 0 and x < self.xmax and y >= 0 and y < self.ymax 

    def is_origin_cell(self, originX, originY, neighbourX, neighbourY):
        return  originX == neighbourX and originY == neighbourY
    
def get_generation(cells, generations):
    return GameOfLife(cells).next_n_gen(generations)

##########    

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
print('Glider\n' + htmlize(start))


print('Glider 1')
end1   = [[0,1,0],
          [0,0,1],
          [1,1,1]]

resp = get_generation(start, 1)
print("Result: " + str(resp == end1))
print('Got: \n' + htmlize(resp) + 'Expected: \n' + htmlize(end1))

print('Glider 2')
end2   = [[1,0,1],
          [0,1,1],
          [0,1,0]]

resp = get_generation(start, 2)
print("Result: " + str(resp == end2))
print('Got: \n' + htmlize(resp) + 'Expected: \n' + htmlize(end2))
