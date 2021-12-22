 #Description:

#A poor miner is trapped in a mine and you have to help him to get out !
#Only, the mine is all dark so you have to tell him where to go.

#In this kata, you will have to implement a method solve(map, miner, exit) that has to return the path the miner must take to reach the exit as an array of moves, such as : ['up', 'down', 'right', 'left']. There are 4 possible moves, up, down, left and right, no diagonal.

#map is a 2-dimensional array of boolean values, representing squares.
#false for walls, true for open squares (where the miner can walk).
#It will never be larger than 5 x 5. It is laid out as an array of columns.
#All columns will always be the same size, though not necessarily the same size as rows (in other words, maps can be rectangular).
#The map will never contain any loop, so there will always be only one possible path. The map may contain dead-ends though.

#miner is the position of the miner at the start, as an object made of two zero-based integer properties, x and y. For example {x:0, y:0} would be the top-left corner.

#exit is the position of the exit, in the same format as miner.

#Note that the miner can't go outside the map, as it is a tunnel.
#Let's take a pretty basic example :

#map = [[True, False], [True, True]];

#solve(map, {'x':0,'y':0}, {'x':1,'y':1})
# Should return ['right', 'down']

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def solve(map, miner, exit):
    return rsolve(map, miner, exit, None, 0)

def rsolve(map, miner, exit, fromDir, nbIter):
    if miner == exit:
        return []
    else:
        path = None
        print("Miner at pos " + str(miner) +" on iter "+ str(nbIter)+ " - last direction: " + str(fromDir)) 
        # MOVE LEFT
        if miner["x"] > 0 and map[miner["x"] - 1][miner["y"]] and fromDir != RIGHT:
            print("Trying left - "  + str(nbIter))
            newMiner = dict(miner); newMiner["x"] -= 1
            path = rsolve(map, newMiner, exit, LEFT, nbIter + 1)
        if path != None:
            return [LEFT] + path
        # MOVE RIGHT
        if miner["x"] < len(map) - 1 and map[miner["x"]+1][miner["y"]] and fromDir != LEFT:
            print("Trying Right - "  + str(nbIter))
            newMiner = dict(miner); newMiner["x"] += 1
            path = rsolve(map, newMiner, exit, RIGHT, nbIter + 1)
        if path != None:
            return [RIGHT] + path
        # MOVE UP
        if miner["y"] > 0 and map[miner["x"]][miner["y"]-1] and fromDir != DOWN:
            print("Trying up - "  + str(nbIter))
            newMiner = dict(miner); newMiner["y"] -= 1
            path = rsolve(map, newMiner, exit, UP, nbIter + 1)
        if path != None:
            return [UP] + path
        # MOVE DOWN
        if miner["y"] < len(map[0]) - 1 and map[miner["x"]][miner["y"]+1] and fromDir != UP:
            print("Trying Down - "  + str(nbIter))
            newMiner = dict(miner); newMiner["y"] += 1
            path = rsolve(map, newMiner, exit, DOWN, nbIter + 1)
        if path != None:
            return [DOWN] + path
        print("Current path: " + str(path) +" - iter " + str(nbIter))
        return None

## Tests
print('- A trivial map (1x1)')
minemap = [[True]]
  
print('Should return an empty array, since we\'re already at the goal')
print(solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}), [])

print('- A pretty simple map (2x2)')
minemap = [[True, False],
    [True, True]]
   
print('Should return the only correct move')
print(solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}), ['right'])
  
print('Should return the only moves necessary')
print(solve(minemap, {'x':0,'y':0}, {'x':1,'y':1}), ['right', 'down'])

print('- A linear map(1x4)')
minemap = [[True], [True], [True], [True]]
  
print('Should return a chain of moves to the right')
print(solve(minemap, {'x':0,'y':0}, {'x':3,'y':0}), ['right', 'right', 'right'])
  
print('Should return a chain of moves to the left')
print(solve(minemap, {'x':3,'y':0}, {'x':0,'y':0}), ['left', 'left', 'left'])

print('Should walk around an obstacle (3x3 map)')
minemap = [[True, True, True],
           [False, False, True],
           [True, True, True]]
  
print('Should return the right sequence of moves')
print(solve(minemap, {'x':0,'y':0}, {'x':2,'y':0}), ['down', 'down', 'right', 'right', 'up', 'up'])

print('With a deadEnd (3x4 map)')
minemap = [[True, True, True],
           [True, False, True],
           [True, False, True],
           [False, False, True],
           [True, True, True]]
  
print('Should return the right sequence of moves')
print(solve(minemap, {'x':0,'y':0}, {'x':4,'y':0}), ['down', 'down', 'right', 'right', 'right', 'right', 'up', 'up'])
