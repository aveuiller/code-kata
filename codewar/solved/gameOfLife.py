def htmlize(array):
    s = []
    for row in array:
        s.append('\t')
        for cell in row:
            s.append('1' if cell else '0')
        s.append('\n')
    return ''.join(s)


class Cell(object):
    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.isAlive = status

    def next_gen(self, cells):
        nbNeighbours = self.compute_neighbours(cells)
        print("Found neighbours: " + str(nbNeighbours))
        self.isAlive = self.living_status(nbNeighbours)
        return self.isAlive

    def compute_neighbours(self, cells):
        nbNeighbours = 0
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                if(self.is_valid_neighbour(cells, x, y)):
                    nbNeighbours += 1
        return nbNeighbours

    def is_valid_neighbour(self, cells, x, y):
        return not self.is_self(x, y) and self.is_inside(cells, x, y) and cells[x][y]
    
    def is_inside(self, cells, x, y):
        return x >= 0 and x < len(cells) and y >= 0 and y < len(cells[0]) 
    
    def is_self(self, x, y):
        return x == self.x and y == self.y
    
    def living_status(self, nbNeighbours):
        return 1 if (self.should_stay_alive(nbNeighbours) or self.should_be_born(nbNeighbours)) else 0
                             
    def should_stay_alive(self, nbNeighbours):
        return self.isAlive and (nbNeighbours == 2 or nbNeighbours == 3)

    def should_be_born(self, nbNeighbours):
        return not self.isAlive and nbNeighbours == 3
        
def next_gen(cells): 
    newCells = list()
    for x in range(0, len(cells)):
        newCells.append([0]*len(cells[x]))
    x = 0
    for row in cells:
        print('\n')
        y = 0
        for state in row:
            print('\n')
            print("Checking:", (x, y))
            print("old cells state: \n" + htmlize(cells))
            print("new cells state:  \n" + htmlize(newCells))
            newCells[x][y] = Cell(x, y, state).next_gen(cells)
            print("Alive: " + str(newCells[x][y]))
            y += 1
        x += 1
    return newCells

start = [[1,0,0],
        [0,1,1],
        [1,1,0]]
end   = [[0,1,0],
        [0,0,1],
        [1,1,1]]

print('Glider\n' + htmlize(start))
resp = next_gen(start)
print("Result: " + str(resp == end))
print('Got: \n' + htmlize(resp) + 'Expected: \n' + htmlize(end))
