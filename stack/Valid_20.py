class Solution:
    def isValid(self, s: str) -> bool:

        ch_stack = []

        left_sign = set(['(','[','{'])
        sign_dict = {')':'(',']':'[','}':'{' }

        for ch in s:

            if ch in left_sign:
                ch_stack.append(ch)
            else:

                if ch not in sign_dict:
                    return False
                
                else:

                    acco_sign = sign_dict[ch]
                    if len(ch_stack) == 0:
                        return False
                    store_sign = ch_stack.pop()

                    if acco_sign != store_sign :
                        return False
        
        return len(ch_stack)==0
                    

