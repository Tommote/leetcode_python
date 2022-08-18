
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        N = 31
        res = 0
        flag = False

        for i in range(N, -1, -1):

            if (num&(1<<i) ) != 0:

                if not flag:
                    flag = True 
                    continue

            if flag and (num&(1<<i) ) == 0:

                res = res + ( 1<<i )
            
        
        return res



if __name__ == '__main__':

    s = Solution()

    print(s.findComplement(0b110001))
