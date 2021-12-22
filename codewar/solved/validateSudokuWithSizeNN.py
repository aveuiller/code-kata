import math
class Sudoku(object):
    def __init__(self, data):
        self.content = data

    def is_valid(self):
        result = True
        if not self.are_dimension_valid():
            return False
        self.dimension = len(self.content)
        self.squareDim = int(math.sqrt(self.dimension))
        for row in self.content:
            result = result and self.is_line_valid(row)
        for col in zip(*self.content):
            result = result and self.is_line_valid(col)
        for i in range(0, self.dimension-1):
            result = result and self.check_square(i)
        return result

    def are_dimension_valid(self):
        nbRows = math.sqrt(len(self.content))
        if not nbRows.is_integer():
            return False
        for col in self.content:
            if not math.sqrt(len(col)) == nbRows: return False
        return True
        
    def is_line_valid(self, line):
        found = []
        for ele in line:
            if self.is_value_valid(ele) and ele not in found:
                found.append(ele)
            else:
                return False 
        return True

    def is_value_valid(self, ele):
        return type(ele) is int and ele > 0 and ele <= self.dimension

    def check_square(self, index):
        inlinedSquare = []
        rowLower = int((index / self.squareDim) * self.squareDim)
        rowUpper = int(rowLower + self.squareDim)
        colLower = int((index % self.squareDim) * self.squareDim)
        colUpper = int(colLower + self.squareDim)
        
        for row in self.content[rowLower:rowUpper]:
            inlinedSquare += row[colLower:colUpper]
        return self.is_line_valid(inlinedSquare)


sudoOk = Sudoku([
    [ 1, 2, 3, 4],
    [ 3, 4, 1, 2],
    [ 2, 1, 4, 3 ],
    [ 4, 3, 2, 1],
    ])
print(sudoOk.is_valid(), True)

sudoKoSize = Sudoku([
    [1, 2],
    [2, 1]
    ])
print(sudoKoSize.is_valid(), False)

sudoKoLine = Sudoku([ 
    [ 1, 2, 3, 3],
    [ 3, 4, 1, 2],
    [ 2, 1, 4, 4 ],
    [ 4, 3, 2, 1],
    ])
print(sudoKoLine.is_valid(), False)

sudoKoRow = Sudoku([ 
    [ 1, 2, 3, 4],
    [ 3, 4, 1, 2],
    [ 2, 1, 4, 4 ],
    [ 2, 3, 4, 1],
    ])
print(sudoKoRow.is_valid(), False)

sudoKoLimit = Sudoku([ 
    [ 1, 2, 3, 42],
    [ 2, 3, 1, 2],
    [ 2, 1, 4, 4 ],
    [ 3, 4, 2, 1],
    ])
print(sudoKoLimit.is_valid(), False)

goodSudoku1 = Sudoku([
    [7,8,4, 1,5,9, 3,2,6],
    [5,3,9, 6,7,2, 8,4,1],
    [6,1,2, 4,3,8, 7,5,9],

    [9,2,8, 7,1,5, 4,6,3],
    [3,5,7, 8,4,6, 1,9,2],
    [4,6,1, 9,2,3, 5,8,7],

    [8,7,6, 3,9,4, 2,1,5],
    [2,4,3, 5,6,1, 9,7,8],
    [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
    [1,4, 2,3],
    [3,2, 4,1],

    [4,1, 3,2],
    [2,3, 1,4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
    [0,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],

    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],

    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9]
])

badSudoku2 = Sudoku([
    [1,2,3,4,5],
    [1,2,3,4],
    [1,2,3,4],  
    [1]
])

print(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
print(goodSudoku2.is_valid(), True, 'Testing valid 4x4')

print(badSudoku1.is_valid(), False, 'Values in wrong order')
print(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')
