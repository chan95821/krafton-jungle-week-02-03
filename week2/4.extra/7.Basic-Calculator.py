class Solution:
    def calculate(self, s: str) -> int:
        s = filter(lambda e : not e.isspace(), s)

        def rec_calc(s, idx):
            l_operand = None
            i = idx
            r_overand = None
            operator = ''
            while i < len(s)
                ch = s[i]
                if not ch.isnum():
                    if ch == ')':
                        return res
                    elif ch == '(':
                        l_operand = rec_calc(s, i + 1)
                        while ch != ')'
                            i += 1
                            ch = s[i]
                        i+=1
                    elif ch == '+':
                        operator = ch
                    elif ch == '-':
                        operator = ch
                else:
                    start = i
                    while i < len(s) and s[i].isnum():
                        i += 1
                    operand(int(s[start:i]))
                        
                        