#/usr/bin/python2.7
import math
def numberOfSteps(steps, m):
    coeff = 1
    nbMoves = coeff * m
    while dreamable(nbMoves, steps):
        if acheavable(steps, nbMoves):
            return nbMoves
        else:
            coeff += 1
            nbMoves = coeff * m
    return -1

def dreamable(nbMoves, steps):
    return nbMoves <= steps

def acheavable(steps, nbMoves):
    minMoves = int(math.ceil(steps / 2.0))
    return minMoves <= nbMoves

print(numberOfSteps(10, 2), 6)
print(numberOfSteps(3, 5), -1)
print(numberOfSteps(10, 1), 5)
print(acheavable(15, 7), True)
print(acheavable(16, 7), False)
print(acheavable(14, 7), True)
print(acheavable(13, 7), True)
print(acheavable(8, 7), True)
