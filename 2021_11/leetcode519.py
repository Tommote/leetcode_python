import random

class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m 
        self.n = n

        self.total = m*n

        self.map = {}


    def flip(self):
        """
        :rtype: List[int]
        """

        ind = random.randint(0, self.total-1)

        self.total -= 1

        y = self.map.get(ind, ind)

        self.map[ind] = self.map.get(self.total, self.total)

        return [y//self.n , y%self.n]





    def reset(self):
        """
        :rtype: None
        """

        self.total = self.m* self.n 
        self.map.clear()


s = Solution(3,2)

print(s.flip())
print(s.flip())
print(s.flip())
print(s.flip())
print(s.flip())
print(s.flip())


