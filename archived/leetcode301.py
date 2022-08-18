class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ans = []

        temp_set = set([s])

        while(True):

            for ss in temp_set:
                if( self.isValid(ss) ):
                    ans.append(ss)
            
            if len(ans)>0:
                return ans
            
            nextSet = set()
            for ss in temp_set:
                for i in range( len(ss) ):
                    
                    if i>0 and ss[i-1]==ss[i]:
                        continue

                    if ss[i] == '(' or ss[i] == ')':

                        nextSet.add(  ss[:i]+ss[i+1:] )
            
            temp_set = nextSet

        return ans





    def isValid(self, s:str):

        count = 0

        for ch in s:

            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        

        return count==0
