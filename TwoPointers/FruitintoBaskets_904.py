from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits)<=2:
            return len(fruits)
        

        ch_dict = dict()

        left,ret = 0, 0

        for i, x in enumerate(fruits):

            if x not in ch_dict:
                ch_dict[x] = 1
            else:
                ch_dict[x] += 1
            
            while len(ch_dict)>2 :

                ch_dict[fruits[left]] -= 1

                if ch_dict[fruits[left]]==0 :
                    ch_dict.pop( fruits[left])
                
                left += 1
            
            ret = max(i-left+1, ret)
        
        return ret

s = Solution()

print(s.totalFruit( [3] ))

            
