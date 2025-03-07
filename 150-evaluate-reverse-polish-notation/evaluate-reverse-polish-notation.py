class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:

            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(int(i))
              
            elif len(stack) >= 2:
        
                val1 = stack.pop()
                val2 = stack.pop()

                if i == "+":
                    add = int(val2) + int(val1)
                    stack.append(add)
                elif i == "-":
                    sub = int(val2) - int(val1)
                    stack.append(sub)
                elif i == "*":
                    mul = int(val2) * int(val1)
                    stack.append(mul)
                elif i == "/":
                    div = int(val2) / int(val1)
                    stack.append(int(div))            
        
        return stack[0]       




        