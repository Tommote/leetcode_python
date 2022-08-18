class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp_d = {}

        N = len(s)
        max_n = 0

        last_n = -1

        for i in range(N):
            
            if s[i] not in temp_d:
                temp_d[s[i]]=i 
                last_loc = -1
            else:
                last_loc = temp_d[s[i]]
                temp_d[s[i]] = i
            
            if last_n==-1:
                last_n = 1
                max_n = 1
                continue

            temp_n = last_n + 1 if last_loc==-1 or last_loc<i-last_n else i-last_loc

            last_n = temp_n
            max_n = max(max_n, last_n)

        return max_n

s = Solution()
print(s.lengthOfLongestSubstring(''))