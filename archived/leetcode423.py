class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        num_ord = [
            
            0,
            6,
            4,
            5,
            7,
            
            2,
            3,
            1,
            9,
            8,
        ]

        num_chs_unqi = {
            
            0:'z',
            6:'x',
            4:'u',
            5:'f',
            7:'v',
            
            2:'w',
            3:'r',
            1:'o',
            9:'n',
            8:'e',
        }

        num_chs = {
            
            0:'zero',
            6:'six',
            4:'four',
            5:'five',
            7:'seven',
            
            2:'two',
            3:'three',
            1:'one',
            9:'nine',
            8:'eight',
        }

        num_hash = { i:self._counter(num_chs[i]) for i in num_chs.keys() }

        ret_num = [0 for _ in range(10) ]

        ss_nums = self._counter(s)

        for key in num_ord:

            num = 1 if key != 9 else 2
            
            ss_nums, num_ch = self._counter_sub( ss_nums, num_hash[key], num_chs_unqi[key], num )
            
            ret_num[key] = num_ch

        ret_str = ''
        for i in range(len(ret_num)):
            

            ret_str += str(i)*ret_num[i] 
        
        return ret_str

    
    def _counter(self, s):

        res = [0 for _ in range(26)]

        for ch in s:

            res[ord(ch)-ord('a')] += 1

        return res 

    def _counter_sub(self, ori_s, num_s, unqi_ch, num=1):

        num_ch = ori_s[ ord(unqi_ch)-ord('a') ]//num 

        ret_s = ori_s

        # print(ori_s)
        # print(num_ch)

        for i in range(len(num_s)):

            ret_s[i] = ori_s[i] - num_s[i]*num_ch
            
        
        return ret_s, num_ch


s = Solution()

print( s.originalDigits("ninenineoneone") )