from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        self.N = len(s)
        self.ret = []
        self.segs = [0]*4

        self.s = s

        if self.N < 4 or self.N > 12 :
            return []

        self.dfs(0,0)

        return self.ret

    
    def dfs(self, seg_id, seg_start):

        if seg_id==4:
            if seg_start==self.N:

                self.ret.append( "{}.{}.{}.{}".format(self.segs[0],self.segs[1],self.segs[2],self.segs[3]) )
        
            else:
                return
        
        if seg_start==self.N:

            return
        

        if self.s[seg_start] == '0':
            self.segs[seg_id] = 0
            self.dfs( seg_id+1, seg_start+1 )
        else:

            addr = 0

            for seg_end in range(seg_start, self.N):

                addr = addr *10 + ord( self.s[seg_end] ) - ord('0')

                if addr > 0 and addr <=255:

                    self.segs[seg_id] = addr 
                    self.dfs(seg_id+1, seg_end+1)
                
                else:
                    break