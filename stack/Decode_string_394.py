class Solution:
    def decodeString(self, s: str) -> str:

        sign_loc = {}

        ch_stack = []

        for i in range(len(s)):

            ch = s[i]
            if ch == '[' :
                ch_stack.append( i )
            elif ch == ']':
                sign_loc[ ch_stack.pop() ] = i 
        
        return self._decodeSub(s, 0, len(s)-1, sign_loc)

    def _decodeSub(self, s:str, start, end, sign_loc):

        ret = ''
        i = start
        while i <= end:

            ch = s[i]

            if ch.isdigit():
                num = ch

                j=i+1
                while j<=end and s[j].isdigit():
                    num += s[j]
                    j += 1
                
                ret = ret + self._decodeSub(s, j+1, sign_loc[j]-1, sign_loc)* int(num)

                i = sign_loc[j]
                 
            else:
                ret = ret + ch

            i += 1
        return ret



s = Solution()

print( s.decodeString(  'abc3[cd]xyz' ))