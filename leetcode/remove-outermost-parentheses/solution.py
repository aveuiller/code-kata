class Solution:
    OPEN_PAR = "("
    CLOSING_PAR = ")"

    def removeOuterParentheses(self, s: str) -> str:
        open_level = deque()
        solution = ""
        for i, char in enumerate(s):
            if char == self.OPEN_PAR:
                open_level.append(i)
            elif char == self.CLOSING_PAR:
                if len(open_level) > 1:
                    open_level.pop()
                elif len(open_level) == 1:
                    solution += s[open_level.pop() + 1 : i]
                else:
                    raise Exception("Should not happen")

        return solution
