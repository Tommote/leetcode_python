from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        

        if len(words)==0 or len(s)==0:
            return []
        num_word = len(words[0])
        num_s = len(s)
        if num_s < num_word*len(words):
            return []

        word_dict = {}
        ret = []

        for word in words:
            
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        
        for i in range( num_s ):

            temp_dict = word_dict.copy()
            flag = True

            for j in range(i+num_word, i+num_word*len(words)+1, num_word):

                if j > num_s:
                    return ret 

                substring = s[j-num_word:j]
                if substring in temp_dict and temp_dict[substring]>0:
                    temp_dict[substring] -= 1
                else:
                    flag = False
                    break
            
            if flag and self.check_dict(temp_dict):
                ret.append(i)

        return ret 


    def check_dict(self, mydict):

        for w in mydict:
            if mydict[w]!=0:
                return False

        return True 


s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword",
["word","good","best","good"]))