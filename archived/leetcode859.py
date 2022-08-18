from typing import Counter


class Solution(object):
    def buddyStrings(self, s:str, goal:str):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):

            return False

        diff_num = 0
        diff = []
        for i in range(len(s)):

            temp = ascii(s[i]) - ascii[goal[i]]

            if temp != 0:
                diff_num += 1
            
                diff.append((s[i], goal[i]))

        
        if diff_num == 0:

            if self._contain_repeat_ch(s):
                return True
            else:
                return False
        
        elif diff_num == 2:

            return diff[0][1]==diff[1][0] and diff[0][0]==diff[1][1]
        
        else:
            return False
    

    def _contain_repeat_ch(sef, s:str):

        c = Counter(s)

        for key,val in c.items():

            if val > 1:

                return True

        return False 