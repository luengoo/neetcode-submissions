class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        p = "+"
        m = "-"
        d = "/"
        x = "*"
        signs = ["+", "-", "*", "/"]
        for token in tokens:
            if len(stack) == 0:
                stack.append(int(token))
            else:
                if token not in signs:
                    stack.append(int(token))
                else:
                    one = stack.pop()
                    two = stack.pop()
                    if token == p:
                        stack.append(two + one)
                    elif token == m:
                        stack.append(two - one)
                    elif token == d:
                        stack.append(int(two / one))
                    elif token == x:
                        stack.append(two * one)
        return stack[0]