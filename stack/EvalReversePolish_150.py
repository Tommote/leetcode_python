from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        num_stack = []

        for chs in tokens:

            print(num_stack)

            if chs.isdigit() or (chs[0]=='-'and len(chs)>1):
                num_stack.append( int(chs) )
            else:
                
                num1 = num_stack.pop()
                num2 = num_stack.pop()

                if chs == '+':
                    num_stack.append( num1+num2 )
                elif chs == '-':
                    num_stack.append( num1-num2 )
                elif chs == '*':
                    num_stack.append( num1*num2 )
                elif chs == '/':
                    num_stack.append( int(num2/num1) )    
        
        return num_stack[0]

s = Solution()

print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(int('-11'))