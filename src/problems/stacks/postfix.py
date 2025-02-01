class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["*", "+", "-", "/"]
        for i in tokens:
            if i not in operations:
                stack.append(int(i))
                continue
            b = stack.pop(-1)
            a = stack.pop(-1)
            if i == "*":
                stack.append(a * b)
            if i == "+":
                stack.append(a + b)
            if i == "-":
                stack.append(a - b)
            if i == "/":
                stack.append(int(a / b))
        return stack[0]
