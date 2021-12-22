#Your task, is to create a NxN spiral with a given size.
#
#For example, spiral with size 5 should look like this:
#
#    00000
#    ....0
#    000.0
#    0...0
#    00000
#
#    and with the size 10:
#
#        0000000000
#        .........0
#        00000000.0
#        0......0.0
#        0.0000.0.0
#        0.0..0.0.0
#        0.0....0.0
#        0.000000.0
#        0........0
#        0000000000
#
#        Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:
#
#            [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
#
#            Because of the edge-cases for tiny spirals, the size will be at least 5.
#
#            General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
#
 
class Spiral(object):
    def __init__(self, size):
        self.size = size
        self.spiral = []
        for i in range(size):
            self.spiral.append([0] * size)
        self.iter = 0
        
    def left(coord):
        (x, y) = coord
        return (x, y - 1)

    def right(coord):
        (x, y) = coord
        return (x, y + 1)

    def up(coord):
        (x, y) = coord
        return (x - 1, y)

    def down(coord):
        (x, y) = coord
        return (x + 1, y)

    DIRS = [right, down, left, up]

    def generate(self):
	if self.size == 0:
       	    return self.spiral
        return self.spiralize_iter(0, 0, self.DIRS[0])
#        return self.spiralize_rec(0, 0, self.DIRS[0])
        
    def spiralize_rec(self, x, y, prevDir):
        """
        Recursive implementation, 
        limited to 981 recursions by python (i.e. a size of 43).
        """
        self.spiral[x][y] = 1
        newDir = self.choose_direction(x, y, prevDir)
        if newDir is None:
            return self.spiral
        (newX, newY) = newDir((x, y))
        self.iter += 1
        return self.spiralize_rec(newX, newY, newDir)

            
    def spiralize_iter(self, xinit, yinit, firstDir):
        """
        Iterative implementation,
        IMO far less sexy than the recursive one,
        but can be unlimited in number of iteration.
        """
        direction = firstDir
        (x, y) = (xinit, yinit)
        (nextX, nextY) = direction((xinit, yinit))
        while direction is not None:
            self.spiral[x][y] = 1
            self.iter += 1
            (nextX, nextY) = direction((x, y))
            direction = self.choose_direction(nextX, nextY, direction)
            (x, y) = (nextX, nextY)
        if (self.is_inside(x,y)):
            self.spiral[x][y] = 1
        return self.spiral
    
    def choose_direction(self, x, y, prevDir):
        index = self.DIRS.index(prevDir)
        for direction in self.DIRS[index:] + self.DIRS[:index]:
            nextCoords = direction((x, y))
            if self.is_inside_and_inactive(nextCoords) and self.no_active_around(nextCoords, direction):
                return direction
        return None

    def no_active_around(self, coord, direction):
        index = self.DIRS.index(direction)
        directionToIgnore = (index + 2) % len(self.DIRS)
        isFine = True
        for i in range(len(self.DIRS)):
            if i != directionToIgnore:
                isFine = isFine and self.is_outside_or_inactive(self.DIRS[i](coord))
        return isFine
    
    def is_outside_or_inactive(self, coord):
        (x,y) = coord
        return not (self.is_inside(x, y) and self.spiral[x][y])

    def is_inside_and_inactive(self, coord):
        (x,y) = coord
        return self.is_inside(x, y) and not self.spiral[x][y]
    
    def is_inside(self, x, y):
        return (x >= 0 and x < self.size) and (y >= 0 and y < self.size) 

    def __str__(self):
        s = []
        for row in self.spiral:
            s.append('\t')
            for cell in row:
                s.append('*' if cell else '0')
            s.append('\n')
        return ''.join(s)
        
def spiralize(size):
    spiral = Spiral(size)
#    print("Init: \n" + str(spiral))
    spiral.generate()
    print("Generated (nbIter: "+str(spiral.iter)+"): \n" + str(spiral))
    return spiral.spiral

        

print("Is fine: " + str(spiralize(0) == [
    []
]))                

print("Is fine: " + str(spiralize(1) == [
    [1]
]))

print("Is fine: " + str(spiralize(2) == [
    [1,1],
    [0,1]
]))
print("Is fine: " + str(spiralize(3) == [
    [1,1,1],
    [0,0,1],
    [1,1,1]
]))
print("Is fine: " + str(spiralize(5) == [
    [1,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]))
print("Is fine: " + str(spiralize(8) == [
    [1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]
]))

spiralize(43)
spiralize(44)
