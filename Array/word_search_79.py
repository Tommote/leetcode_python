from typing import List


class Solution:


    def exist(self, board: List[List[str]], word: str) -> bool:

        self.N, self.H, self.W = len(word), len(board), len(board[0])

        self.board, self.word = board, word
        
        self.road = [[False]*self.W for _ in range(self.H)]
        self.direction = [-1,0,1,0,-1]

        for x in range(self.H):
            for y in range(self.W):

                if board[x][y] == word[0]:
                    self.road[x][y] = True
                    if self.search(1, x, y):
                        return True
                    self.road[x][y] = False
        
        return False

    
    def search(self, i , x , y):

        """
        """
        if i == self.N :
            return True
        
        for k in range(4):

            new_x , new_y = x + self.direction[k], y + self.direction[k+1]

            if (new_x>=0 and new_y>=0 and new_x<self.H and new_y<self.W 
                and not self.road[new_x][new_y] and self.board[new_x][new_y]==self.word[i] ):

                self.road[new_x][new_y] = True

                if self.search(i+1, new_x, new_y):
                    return True

                self.road[new_x][new_y] = False
        
        return False

s = Solution()
print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], 'AAB'))
        
