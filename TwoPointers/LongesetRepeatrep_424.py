class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        N = len(s)

        if N <= 1:
            return N

        ch_dict = {}

        left, right = 0, 1 

        max_ch = s[0]
        ch_dict[s[0]] = 1
        ret = 1

        while right<N :

            if right<N :
                ch_dict[s[right]] = ch_dict.pop(s[right], 0) + 1

                if ch_dict[s[right]]>ch_dict[max_ch]:
                    max_ch = s[right]
            
                if right-left+1 - ch_dict[max_ch] <= k:
                    ret = max(right-left+1, ret)
                    right += 1
                else:
                    
                    ch_dict[s[left]] = ch_dict.pop(s[left], 0) - 1

                    if s[left]==max_ch:
                        max_ch = self.find_max_ch(ch_dict)
                    
                    left += 1
                    right += 1
        
        return ret 
    

    def find_max_ch(self, ch_dict:dict):
        
        max_ch = ''
        for ch , num in ch_dict.items():

            if max_ch=='' or num > ch_dict[max_ch]:

                max_ch = ch 
        

        return max_ch

s = Solution()

print(s.characterReplacement('AABABBA', 1))


    