

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        if len(s)<=1:
            return 0

        valid_arr = [0]*len(s) 

        stack_list = []


        for i in range(len(s)):

            if s[i]=='(':

                stack_list.append(i)
            
            else:

                if len(stack_list)>0 :

                    valid_arr[stack_list.pop()] = 1
                    valid_arr[i] = 1
        
        ret = 0
        temp = 0
        for i in range(valid_arr):

            if valid_arr[i]==1:
                temp += 1 
                ret = max(ret, temp)
            else:
                temp = 0
        
        return ret 
