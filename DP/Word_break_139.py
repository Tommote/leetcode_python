from typing import List

class dict_tree_node:
    def __init__(self, is_Leaf) :
        self.val = [None]*26
        self.isLeaf = is_Leaf

class dict_tree:
    def __init__(self):
        
        self.root = dict_tree_node(False)
    
    def insert_word(self, word:str):
        
        self._dfs_insert(word, self.root, 0) 
    
    def judge_include_word(self, word:str):

        if len(word)==0:
            return True

        return self._dfs(word, self.root, 0)

    def _dfs_insert(self, word:str, curr_node:dict_tree_node, curr_ind:int):
        if curr_ind==len(word)-1:
            if curr_node.val[ ord(word[-1])-ord('a')] is None :
                curr_node.val[ ord(word[-1])-ord('a')] = dict_tree_node(True)
            else:
                curr_node.val[ ord(word[-1])-ord('a')].isLeaf = True
        else:
            temp_ch = word[curr_ind]
            if curr_node.val[ ord(temp_ch)-ord('a')] is None :
                curr_node.val[ ord(temp_ch)-ord('a')] = dict_tree_node(False)
            
            self._dfs_insert(word, curr_node.val[ ord(temp_ch)-ord('a')], curr_ind+1)


    def _dfs(self, word:str, curr_node:dict_tree_node, curr_ind:int):
        if curr_ind==len(word)-1:
            if curr_node.val[ ord(word[-1])-ord('a')] is None :
                return False
            else:
                node = curr_node.val[ ord(word[-1])-ord('a')]
                return node.isLeaf
        else:        
            temp_ch = word[curr_ind]
            if curr_node.val[ ord(temp_ch)-ord('a')] is None :
                return False
            
            return self._dfs(word, curr_node.val[ ord(temp_ch)-ord('a')], curr_ind+1)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dt = dict_tree()

        for t in wordDict:
            dt.insert_word(t)
        
        dp_arr = [False]*len(s)

        for i in range(len(s)):

            if dt.judge_include_word(s[:i+1]) :
                dp_arr[i] = True
            else:

                for j in range(i):
                    if dp_arr[j] and dt.judge_include_word(s[j+1:i+1]):
                        dp_arr[i] = True
                        break
        # print(dp_arr)
        return dp_arr[-1]

                

s = Solution()
print(s.wordBreak(s = "cars", wordDict = ["car","ca","rs"]))

# dt = dict_tree()
# dt.insert_word("car")
# dt.insert_word("ca")
# print(dt.judge_include_word("ca"))