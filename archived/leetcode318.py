class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        matrix =  [ self.str2code(x) for x in words ]

        for i in range(len(words)) :
            for j in range(i, len(words)) :

                if matrix[i] & matrix[j] == 0:
                    ret = max( ret, len(words[i])*len(words[j]) )
            
        return ret

    def str2code(self, str):

        code = 0

        for ch in str:

            code = code | (1<<(ord(ch)-ord('a')))
        
        return code 


s = Solution()

words = ["abcw","baz","foo","bar","xtfn","abcdef"]

print(s.maxProduct(words))