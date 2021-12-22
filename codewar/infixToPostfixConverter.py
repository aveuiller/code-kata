import re

class Operation(object):
    def __init__(self, leftOperand, operator, rightOperand):
        self.left = leftOperand
        self.right = rightOperand
        self.operator = operator

    def __str__(self):
        return self.left.__str__() + self.right.__str__() + self.operator.__str__()

OPERATORS = ["+", "-", "*", "/", "^"]
WEAK_OP = ["+", "-"]

NUMBER = "-?\d+(\.\d+)?"

OPERATOR = "[\-+*/^]"

OPERAND = "[" + NUMBER + "]"
OPERATION =  "\(?\s*" + OPERAND + "\s*" + OPERATOR + "\s*" +OPERAND + "\s*\)?"

def to_postfix(entry):
    operation = analyse_operation(entry)
    return operation

def analyse_operation(entry):
    matches = re.findall(OPERATION, entry)
    for match in matches:
        print(match)
    #return Operation("2", "+", Operation("7", "*", "5"))
    #return Operation(3, "*", Operation(3, "/", Operation("7", "+", "1"))) # False
    #return Operation(Operation(3, "*", 3), "/", Operation("7", "+", "1"))

    #return Operation(5, "+", Operation(Operation(Operation(6, "-", 2), "*", 9), "+", Operation(3, "^", Operation(7, "-", 1))))
    return Operation(
        Operation(5, "+", Operation(Operation(6, "-", 2), "*", 9)),
        "+",
        Operation(3, "^", Operation(7, "-", 1))
    )

def next_weak_operation(entry):
    ## Need this kind of method in overlapping mode.
    # re.findall("\d+[+-]{1}\d+", "2+5*4+3")
    return entry.rfind("+-")

#print(to_postfix("2+7*5")) # Should return "275*+"
# to_postfix("3*3/(7+1)") # Should return "33*71+/"
print(to_postfix("5+(6-2)*9+3^(7-1)")) # Should return "562-9*+371-^+"


2+(7*5)
((3*3)/(7+1))
5+((6-2)*9)+(3^(7-1))

