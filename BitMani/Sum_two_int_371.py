class Solution:
    def getSum(self, a: int, b: int) -> int:

        self.MAX_BIT = 32
        a , b = self._int2list(a), self._int2list(b)
        # print(a,b)
        return self._list2int( self._add_via_xor_for_pos(a,b) )


    def _add_via_xor_for_pos(self, a, b):

        ret = [0]* self.MAX_BIT

        flag = False

        for i in range(self.MAX_BIT-1, -1, -1):

            if a[i]==0 and b[i]==0:
                if flag:
                    ret[i] = 1
                    flag = False
            elif a[i]==1 and b[i]==1:
                if flag:
                    ret[i] = 1
                flag = True
            else:
                if not flag:
                    ret[i] = 1
        return ret 
    def _int2list(self, x):
        ret = []
        if x>=0:
            ret_temp = bin(x)[2:]
            ret = [0]*self.MAX_BIT
        else:
            ret_temp = bin(-x)[2:]
            ret = [1]*self.MAX_BIT
        
        j = self.MAX_BIT-1
        for i in range(len(ret_temp)-1, -1, -1):
            
            if ret_temp[i]=='1':
                if x>=0:
                    ret[j] = 1
                else:
                    ret[j] = 0
            j -= 1
        
        # print(x,ret_temp,ret)
        if x < 0 :
            temp_1 = [0]*self.MAX_BIT
            temp_1[-1] = 1
            ret = self._add_via_xor_for_pos(ret, temp_1)
            ret[0] = 1
        
        return ret 
    
    def _list2int(self, x):
        
        head = '0b'

        if x[0]==1:
            head = '-0b'
            not_x = [ 0 if x[i]==1 else 1 for i in range(0, self.MAX_BIT) ]
            temp_1 = [0]*self.MAX_BIT
            temp_1[-1] = 1
            x = self._add_via_xor_for_pos(not_x, temp_1)

        for i  in range(1, self.MAX_BIT):
            if x[i]==0:
                head += '0'
            else:
                head += '1'
        
        return int(head, base=0)

s = Solution()
print(s.getSum(-8,20))

# x = s._int2list(-111010100)
# print(x, len(x))
# print(s._list2int())
        
        


