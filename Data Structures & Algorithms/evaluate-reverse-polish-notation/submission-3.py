class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # treat as stack
        # when an operator is seen, treat 2 most recently seen nums as
        # the operands
        nums = []
        possible_tokens = {"+", "-", "*", "/"}
        res = None

        for token in tokens:
            if token not in possible_tokens:
                nums.append(int(token))
                res = int(token)
            else:
                # token is an operator
                op2 = nums.pop()
                op1 = nums.pop()

                if token == "+":
                    res = op1 + op2
                elif token == "-":
                    res = op1 - op2
                elif token == "*":
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                
                nums.append(res)
        return res