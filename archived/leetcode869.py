class Solution(object):

    def __init__(self):
        super().__init__()

        self.cache = []

        temp = 1

        while temp<=10e9:
            
            self.cache.append( self.preprocess( temp ) )
            
            temp = temp * 2





    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return self.preprocess(n) in self.cache

    def preprocess(self, n):

        n = sorted(str(n))
        s = ''.join( i for i in n )
        return s 


s = Solution()

print(s.reorderedPowerOf2(46))