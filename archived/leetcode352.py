from sortedcontainers import SortedDict

class SummaryRanges(object):

    def __init__(self):

        self.sd = SortedDict() 


    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        pass 


s = SortedDict([[1,2], [3,4],[2,5]])

print(s)
