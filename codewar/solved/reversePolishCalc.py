#/usr/bin/python2.7

#Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
#
#For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
#
#Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.
#
#Empty expression should evaluate to 0.
#
#Valid operations are +, -, *, /.
#
#You may assume that there won't be exceptional situations (like stack underflow or division by zero).
#
import re

class Operation(object):
    def __init__(self, leftOperand, operator, rightOperand):
        self.left = float(leftOperand)
        self.right = float(rightOperand)
        self.operator = operator

    def __str__(self):
        return self.left.__str__() + self.right.__str__() + self.operator.__str__()

    def result(self):
        # TODO: There must be a better way...
        if (self.operator == "+"):
            return self.left + self.right
        elif (self.operator == "-"):
            return self.left - self.right
        elif (self.operator == "*"):
            return self.left * self.right
        elif (self.operator == "/"):
            return self.left / self.right
        else:
            return -1

DIGIT_REGEX="-?\d+(\.\d+)?"
OPERATOR_REGEX="[+\-*/]"
        
def calc(expr):
    result = re.search(DIGIT_REGEX+"?$", expr)
    if result:
        value = float(result.group())
        return int(value) if value.is_integer() else value 
    operationMatch = re.search("("+DIGIT_REGEX+" "+DIGIT_REGEX+" "+OPERATOR_REGEX+")", expr)
    if not operationMatch:
        return 0
    operation = operationMatch.group()
    operationElements = operation.split(" ")
    ope = Operation(operationElements[0], operationElements[2], operationElements[1])
    return calc(expr.replace(operation, str(ope.result())))

print(calc(""), 0, "Should work with empty string")
print(calc("1 2 3"), 3, "Should parse numbers")
print(calc("1 2 3.5"), 3.5, "Should parse float numbers")
print(calc("1 3 +"), 4, "Should support addition")
print(calc("1 3 *"), 3, "Should support multiplication")
print(calc("1 3 -"), -2, "Should support subtraction")
print(calc("4 2 /"), 2, "Should support division")

print(calc("5 1 2 + 4 * + 3 -"), 14, "Should support multiple operations")
