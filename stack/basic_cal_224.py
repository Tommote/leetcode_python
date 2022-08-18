class Solution:
    def __init__(self):
        self.priority = {}
        self.priority['('] = 0
        self.priority['+'] = 1
        self.priority['-'] = 1
        self.priority['*'] = 2
        self.priority['/'] = 2

    def cal_sign(self,num1, num2, sign):
        # num1 , num2 = int(num1),int(num2)
        if sign=='+':
            return num1+num2
        elif sign=='-':
            return num2-num1 
        elif sign=='*':
            return num1*num2 
        elif sign=='/':
            return num2/num1
        else:
            Exception('dfssaf'+sign)

    def calculate(self, s: str) -> int:
        
        s = s.replace(' ','')

        temp_s = []
        flag = False
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == ' ':
                i += 1
                continue
            if ch ==')' or ch in self.priority:
                if ch=='-':
                    if i==0 or s[i-1] in self.priority:
                        if s[i+1]=='(':
                            temp_s.append(0)
                            temp_s.append(ch)
                            i+=1
                            continue
                        flag = True
                        i += 1
                        continue
                temp_s.append(ch)
                i += 1
            else:
                temp_num = ''
                while  i<len(s) and s[i].isdigit():
                    temp_num += s[i]
                    i += 1
                if flag:
                    temp_s.append(-1*int(temp_num))
                    flag = False
                else:
                    temp_s.append(int(temp_num))
        
        print(temp_s)
        s = temp_s
        out_str = []

        stack_sign = []
        i = 0
        while i<len(s):
            ch = s[i]
            if ch == ' ':
                pass 
            elif ch == '(':
                stack_sign.append(ch)
            elif ch == ')':
                
                while len(stack_sign)>0 and stack_sign[-1]!='(':
                    out_str.append(stack_sign.pop())
                if stack_sign[-1]=='(':
                    stack_sign.pop()
            elif ch not in self.priority:
                out_str.append(ch)
            else:
                while len(stack_sign)>0 and \
                    self.priority[ch] <= self.priority[stack_sign[-1]]:
                    out_str.append(stack_sign.pop())
                stack_sign.append(ch)
            i += 1
        
        while len(stack_sign)>0:
            out_str.append(stack_sign.pop())
        print(out_str)
        cal_stack = []
        for ch in out_str:
            if ch not in self.priority:
                cal_stack.append(ch)
            else:
                
                cal_stack.append( 
                    self.cal_sign( cal_stack.pop(), cal_stack.pop(),ch ) )


        return cal_stack[-1]

s = Solution()
print(s.calculate("1-(5)"))



