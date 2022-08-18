from typing import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        
        N = len(s)
        c = Counter(s)
        ll = c.most_common()
        # print(ll)
        max_n = ll[0][1]

        if 2*max_n-1 > N:
            return ''
        

        ret = ''

        left , right = [0, ll[0][1]], [1, ll[1][1]]
        flag = False
        visited = [0,1]
        while N :
            print(left, right, ret)
            if flag:
                curr = right
            else:
                curr = left

            ret += ll[curr[0]][0]
            curr[1] -= 1

            if curr[1]==0:
                while curr[0] in visited:
                    curr[0] += 1

                visited.append(curr[0])
                if curr[0] < len(ll):
                    curr[1] = ll[curr[0]][1]

            N -= 1
            flag = not flag 
        
        return ret 

s = Solution()
print(s.reorganizeString("aabbcc"))