class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        sign_stack = []

        ret = 0

        for ch in s:

            if ch == '(':
                sign_stack.append(ch)

            else:
                if len(sign_stack)==0 :
                    ret += 1
                else:
                    sign_stack.pop()

        return len(sign_stack)+ret 

s = Solution()

print(s.minAddToMakeValid('()'))