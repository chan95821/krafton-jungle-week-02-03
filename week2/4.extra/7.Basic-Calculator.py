import re
class Solution:
    def get_num(self, input:str, s):
        if input[s].isdecimal():
            idx = s
            while idx < len(input):
                if input[idx].isdecimal():
                    idx += 1
                else: break
            return True, int(input[s:idx]), idx
        else:
            return False, None, None

    def calculate(self, s: str) -> int:
        s = "".join(filter(lambda e : not e.isspace(), s))
        items = list(filter(None, re.split(r"([+\-()])", s))) # TODO - regex split시 빈 문자열 추가되는 이유 조사 

        print(items)
        idx = 0
        operands = [] #두 스택은 짝 이뤄야 한다 
        operators = []
        for idx, val in enumerate(items):
            if val.isdecimal():
                if idx == 0 or items[idx -1] == '(':
                    operators.append('+')
                operands.append(int(val))
            elif val == '(':
                if idx == 0 or items[idx -1] == '(':
                    operators.append('+')
                operands.append(val)
            elif val == ')':
                result = 0
                while operands[-1] != '(':
                    cur = operands.pop()
                    curop = operators.pop()
                    if curop == '-':
                        cur *= -1
                    result += cur
                operands.pop()
                operands.append(result) # operands의 '('를 result로 대체하니, 짝 operator는 그대로 있어야 함 
            elif val == '+':
                operators.append(val)
            elif val == '-':
                operators.append(val)

    
    #  괄호 안은 모두 처리한  - 괄호가 없다 

        for idx, operand in enumerate(operands):
            if operators[idx] == '-':
                operands[idx] = operands[idx] * -1
        return sum(operands)

           
            