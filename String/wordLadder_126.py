from typing import List
from collections import defaultdict, deque
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # build the hashmap
        N_wordlist = len(wordList)
        N_word = len(beginWord)

        self.word_dict = {beginWord:0}
        self.word_dict_1 = {0:beginWord}
        i = 1
        for word in wordList:
            self.word_dict[word] = i 
            self.word_dict_1[i] = word
            i += 1

        # bulid the graph
        all_chs = string.ascii_lowercase
        word_set = set(wordList)
        word_set.add(beginWord)
        self.word_graph = {}

        for word in self.word_dict.keys():
            if word not in self.word_graph:
                self.word_graph[word] = []
            
            for i in range(N_word):
                ori_ch = word[i]
                for j in range(26):
                    cur_ch = all_chs[j]
                    if cur_ch == ori_ch:
                        continue
                    word_temp = ''+cur_ch+word[i+1:] if i==0 else word[:i]+cur_ch+word[i+1:]
                    if word_temp in word_set:
                        self.word_graph[word].append( self.word_dict[word_temp] )
        print(self.word_graph)
        successor, found  = self.__bfs(beginWord, endWord)

        if not found:
            return []
        
        print(successor)

        self.ret = []
        path = []
        path.append(beginWord)
        self.__dfs(beginWord, endWord, path, successor)

        return self.ret
        

    def __bfs(self, beginWord, endWord):

        successor = defaultdict(set)

        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        next_floor_visited = set()

        found = False

        while len(queue) != 0:

            cur_len = len(queue)

            for _ in range(cur_len):

                cur_word = queue.popleft()

                for ind in self.word_graph[ cur_word ]:

                    next_word = self.word_dict_1[ind]
                    if next_word not in visited:
                        if next_word == endWord:
                            found = True
                        
                        if next_word not in next_floor_visited:
                            queue.append(next_word)
                            next_floor_visited.add(next_word)

                        successor[cur_word].add(next_word)
            
            if found:
                break

            visited |= next_floor_visited
            next_floor_visited.clear() 
        
        return successor, found

    def __dfs(self, beginWord, endWord, path,successor):

        if beginWord==endWord:
            self.ret.append(path)
            return

        for next_word in successor[beginWord]:

            temp_path = path.copy()
            temp_path.append(next_word)
            self.__dfs( next_word, endWord, temp_path, successor)

        

s = Solution()

# ret = s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
ret = s.findLadders(beginWord = "hot", endWord = "dog", wordList = ["hot","dog"])


print(ret)