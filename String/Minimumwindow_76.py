class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_num, t_num = len(s), len(t)

        if s_num < t_num:

            return '';
        
        ch_dict = {}

        for ch in t:
            if ch in ch_dict:
                ch_dict[ch] += 1
            else:
                ch_dict[ch] = 1
        
        min_ret = s_num+1
        min_i = -1

        i,j = 0,0
        temp_dict = {s[0]:1}

        while i <= j:

            if not self.check_dict(temp_dict, ch_dict):
                
                j += 1
                if j == s_num:
                    break
                if s[j] in temp_dict:
                    temp_dict[s[j]] += 1
                else:
                    temp_dict[s[j]] = 1

            else:
                if min_ret > j-i+1:
                    min_ret = j-i+1
                    min_i = i 
                
                temp_dict[s[i]] -= 1 
                i += 1

        
        return ''if min_i == -1 else s[min_i:min_i+min_ret]
                
    
    def check_dict(self, dict_s:dict, dict_t:dict):

        for ch in dict_t.keys():
            if ch not in dict_s or dict_s[ch] < dict_t[ch]:
                return False
        
        return True

s = Solution()

print(s.minWindow("aaaaaaaaaaaabbbbbcdd" , "abcdd"))
# print(s.minWindow("aaaaa" , "aaaaa"))
