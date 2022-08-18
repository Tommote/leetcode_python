class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        p_len, s_len = len(p), len(s) 

        ret = []

        if p_len > s_len:
            return ret

        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(p_len):

            p_count[ ord(p[i])- ord('a') ] += 1
            s_count[ ord(s[i])- ord('a') ] += 1


        if s_count == p_count:
            ret.append(0)

        for i in range(1, s_len-p_len+1):

            s_count[ ord(s[i-1])-ord('a') ] -= 1

            s_count[ ord( s[i+p_len-1] ) - ord('a')] += 1

            if s_count== p_count:
                ret.append(i)

        
        return ret 

s = Solution()

print(s.findAnagrams('abab', 'ab'))