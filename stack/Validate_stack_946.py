from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        

        num_stack = []
        num_j = 0

        for num_i in pushed:

            num_stack.append(num_i)


            while len(num_stack)>0 and len(popped)>num_j and num_stack[-1]==popped[num_j]:

                num_j += 1
                num_stack.pop()
            
        
        return len(num_stack)==0


