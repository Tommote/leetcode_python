from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        if len(nums)==2:
            return abs(nums[0]-nums[1])
        min_val , max_val = min(nums) , max(nums) 

        d = max( (max_val-min_val)//len(nums) - 1 , 1 )

        box_num = (max_val-min_val)//d + 2

        boxs = [ [-1, -1] for _ in range(box_num) ]


        for num in nums :
            # print(boxs,d, num, min_val)
            # ind = min(num//d , len(boxs)-1) 
            ind = (num-min_val)//d
            if boxs[ind][0]==-1:
                boxs[ind][0], boxs[ind][1] = num, num 
            else:
                boxs[ind][0] = min( boxs[ind][0], num )
                boxs[ind][1] = max( boxs[ind][1], num )
        
        # print(boxs)
        
        last_box_ind = -1
        ret = -1
        for i in range(0, len(boxs)) :

            if boxs[i][0]==-1:
                continue 
            elif i>0 and last_box_ind != -1:
                ret = max( ret,  boxs[i][0]-boxs[last_box_ind][1])
            last_box_ind = i

        return ret 

s = Solution()
print( s.maximumGap([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]) ) 
