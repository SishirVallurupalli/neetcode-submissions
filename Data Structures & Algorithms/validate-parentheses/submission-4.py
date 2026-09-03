class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                arr.append(c)
            if c == ')' or c == '}' or c == ']':
                if len(arr) == 0:
                    return False
            if c == ')':
                if arr.pop() != '(':
                    return False
            elif c == '}':
                if arr.pop() != '{':
                    return False
            elif c == ']':
                n = arr.pop()
                print(n)
                if n != '[':
                    return False
        return len(arr) == 0  
