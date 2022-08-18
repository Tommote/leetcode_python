class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        self.tiles = sorted(tiles)
        self.N = len(tiles)

        
        self.ret = 0
        self.isVisited = [False]*self.N

        self._dfs(0)

        return self.ret - 1

    def _dfs(self, i):
        self.ret += 1

            
        print(self.isVisited)
        for i in range(self.N):
            if self.isVisited[i]:
                continue
            if i>0 and self.tiles[i-1]==self.tiles[i] and not self.isVisited[i-1]:
                continue

            self.isVisited[i]=True
            self._dfs(i+1)
            self.isVisited[i]=False

s = Solution()
print(s.numTilePossibilities('AAB'))