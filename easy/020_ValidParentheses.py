class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')':'(','}':'{',']':'['
        }
        stack = []
        if len(s)%2 != 0:
            return False
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack.pop(-1) != parentheses[i]:
                    return False
        return  not bool(stack)
    