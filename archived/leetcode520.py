class Solution(object):

    def detectCapitalUse(self, word:str):
        """
        :type word: str
        :rtype: bool
        """

        if word[0].islower() :
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        
        else:
            for i in range(1, len(word)-1):
                if( (word[i].isupper() and word[i+1].islower())
                    or (word[i+1].isupper() and word[i].islower())):
                    return False
        
        return True



s = Solution()

print( s.detectCapitalUse('Ua') )