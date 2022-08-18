from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        L = len(strs)

        if L==1:
            return 1 

        edges = [[0 for _ in range(L)] for _ in range(L) ] 
        groups = [-1 for _ in range(L)]

        for i in range(L) :
            for j in range(i , L):
                if self._judge_sim( strs[i], strs[j] ) :
                    edges[i][j], edges[j][i] = 1, 1 

        ret = 0
        for i in range(L) :

            if groups[i]==-1:
                self._dfs(edges, groups, i, ret)
                ret += 1 

        return ret 

    def _dfs(self, edges, groups, i, ret):

        L = len(edges)
        groups[i] = ret 

        for j in range(L):

            if edges[i][j]==1 and groups[j]==-1:

                self._dfs(edges, groups, j, ret)

    def _judge_sim(self, x:str, y:str) -> bool :

        N = len(x) 
        temp_list = []

        for i in range(N):

            if x[i] != y[i] :
                temp_list.append(i) 

        if len(temp_list) != 2:
            return False 
        
        return True 

s = Solution()
print(s.numSimilarGroups(   ["omv","ovm"] ))