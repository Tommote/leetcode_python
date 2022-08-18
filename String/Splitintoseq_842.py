from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
        self.ret = list()
        self.num = num

        self.backtrack(0)

        return self.ret
    

    def backtrack(self, ind):


        if ind==len(self.num):
            return len(self.ret) > 2
        
        curr = 0

        for i in range(ind, len(self.num)):

            if i>ind and self.num[ind]=='0':
                break

            curr = curr * 10 + ord(self.num[i])-ord('0')

            if curr > 2**31 -1 :
                break

            if len(self.ret)<2 or  curr == self.ret[-1]+self.ret[-2]:
                
                self.ret.append(curr)
                if self.backtrack( i+1 ):
                    return True
                else:
                    self.ret.pop()

            elif len(self.ret) > 2 and curr > self.ret[-1]+self.ret[-2] :
                break

        return False

s = Solution()

print(s.splitIntoFibonacci('123456579'))