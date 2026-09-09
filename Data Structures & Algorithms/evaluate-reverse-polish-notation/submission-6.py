import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        all_operators = {
            "+": operator.add, 
            "-": operator.sub, 
            "*": operator.mul, 
            "/": operator.truediv
        }

        operands = []

        for token in tokens:
            if token not in all_operators:
                operands.append(int(token))
                continue
                
            # else, token is an operator

            num2 = operands.pop()
            num1 = operands.pop()

            res = int(all_operators[token](num1, num2))
            
            operands.append(res)
        
        return operands[0]



