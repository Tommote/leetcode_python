

from functools import reduce


class Node:

    def __init__(self) -> None:
        self.arr = [None]*26
        self.is_end = False



class WordDictionary:

    def __init__(self):

        self.root = Node()


    def addWord(self, word: str) -> None:

        self._dfs_add_word(self.root, word, 0) 

    def _dfs_add_word(self, node: Node,word:str, i:int):

        if i==len(word):
            return
        num = ord(word[i])-ord('a')
        if node.arr[num] is None:
            node.arr[num] = Node()
        if i==len(word)-1:
            node.is_end=True
        else:
            self._dfs_add_word(node.arr[num], word, i+1)

    def search(self, word: str) -> bool:

        return self._dfs_search_word(self.root, word, 0) 

    def _dfs_search_word(self, node: Node,word:str, i:int):

        if node is None:
            return False

        if i==len(word)-1 and node.is_end==True :
            return True
        
        if i==len(word):
            return False

        ret = False

        if word[i]=='.':
            for x in node.arr:
                ret = ret or self._dfs_search_word(x,word, i+1 )
        else:
            num = ord(word[i])-ord('a')
            # print(num, word[i])
            if node.arr[num] is None:
                ret = False
            else:
                ret = self._dfs_search_word(node.arr[num], word, i+1)

        return ret 



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
wordDictionary = WordDictionary();
wordDictionary.addWord("a");
wordDictionary.addWord("a");
print(wordDictionary.search("."));
print(wordDictionary.search("a"));
print(wordDictionary.search("aa")); # return True
print(wordDictionary.search("a"));
print(wordDictionary.search(".a")); # return True
print(wordDictionary.search("a.")); # return True
