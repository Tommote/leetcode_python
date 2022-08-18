class Solution2:
    def countArrangement(self, n: int) -> int:

        self.ret = 0 
        if n==1:
            return 1
        
        self.n = n
        self.nums = [i for i in range(1, n+1)] 
        self.arrangement = []
        self.visited = [False]*self.n

        self._backtrack(0)

        return self.ret

    def _backtrack(self, nn):

        if nn == self.n :

            for i in range(self.n):
                if self.arrangement[i]%(i+1) != 0 and (i+1)%self.arrangement[i] != 0:
                    return
            
            self.ret += 1
        

        for i in range(self.n):
            
            if (not self.visited[i] and 
                    (self.nums[i]%(i+1) == 0 or (i+1)%self.nums[i] == 0 )):
                
                self.arrangement.append(self.nums[i])
                self.visited[i] = True 

                self._backtrack(nn+1)

                self.arrangement.pop()
                self.visited[i] = False


class Solution:
    def countArrangement(self, n: int) -> int:

        N = 1<<n 
        dp = [0]*N 
        dp[0] = 1

        for mask in range(1, N):

            num = bin(mask).count('1')

            for i in range(n):

                if ((1<<i)&mask)!=0 and ( (i+1)%num==0 or num%(i+1)==0 ):
                    dp[mask] += dp[ mask^(1<<i) ]
            
            # print(dp)
        return dp[N-1]




s = Solution()
print(s.countArrangement(4))

# m = 5 
# print(bin(m).count('1'))