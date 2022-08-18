class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []

        for ch in s:

            if ch=='(':
                stack.append('(')
            else:

                temp = 0
                while stack[-1] != '(':
                    temp += stack.pop()

                stack.pop()
                if temp==0 :
                    stack.append( 1 )
                else:
                    stack.append( 2*temp )

        return sum(stack)

s = Solution()

print( s.scoreOfParentheses( '()()' ) )