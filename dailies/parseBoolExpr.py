from typing import List


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        res = True
        stack = []
        for el in expression:
            if el == 'f' or el == 't' or el == '|' or el == '&' or el == '!' or el == '(':
                stack.append(el)
            elif el == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                operator = stack.pop()
                res = self.eval(operator, temp)
                stack.append(res)
        return stack.pop() == 't'
    
    def eval(self,operator: str, expr: List[str]) -> bool:
        if operator == '&':
            return 't' if all(el == 't' for el in expr) else 'f'
        elif operator == '|':
            return 't' if 't' in expr else 'f'
        elif operator == '!' :
            return 't' if expr[0] == 'f' else 'f'
    
expr ="&(|(f))"
sol = Solution()
print(sol.parseBoolExpr(expr))
# print(sol.eval('|', ['f', 'f']))