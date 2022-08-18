from collections import defaultdict, deque
import string
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        if len(s)<=1:
            return s 

        ch_dict = {}
        max_ch = -1

        for ch in s:
            if ch not in ch_dict:
                ch_dict[ch] = 0
             
            ch_dict[ch] += 1
            max_ch = max(max_ch, ch_dict[ch])
        
        if not max_ch <= (len(s)+1)//2 :
            return ''
        
        ch_list = sorted(ch_dict.items(), key=lambda x:x[1] , reverse=True)

        ch_p_1, ch_p_2 = 0, 1
        ch_p_1_len , ch_p_2_len = ch_list[0][1], ch_list[1][1]

        ret = ['0']*len(s) 
        i = 0
        while i < len(ret):
            
            if i%2==0:
                if ch_p_1 < len(ch_list) and ch_p_1_len > 0:
                    ret[i]=ch_list[ch_p_1][0]
                    ch_p_1_len -= 1
                    i+=1
                elif ch_p_1_len == 0 :
                    ch_p_1 += 2
                    if ch_p_1 < len(ch_list):
                        ch_p_1_len = ch_list[ch_p_1][1]  
                    else: 
                        if ch_p_1_len==0 and ch_p_2_len==0:
                            break
            
            else:
                if ch_p_2 < len(ch_list) and ch_p_2_len > 0:
                    ret[i]=ch_list[ch_p_2][0]
                    ch_p_2_len -= 1
                    i+=1
                elif ch_p_2_len == 0 :
                    ch_p_2 += 2
                    if ch_p_2 < len(ch_list):
                        ch_p_2_len = ch_list[ch_p_2][1]  
                    else: 
                        if ch_p_1_len==0 and ch_p_2_len==0:
                            break

        return ''.join(ret)


s = Solution()
ret = s.reorganizeString('aabdsbaadbababbbbbaae')
print(ret)