
from queue import Queue

class DictionaryTreeNode(object):

    def __init__(self):
        
        self.children = [None] * 26

        self.isEnd = True

    def insert(self, word:str):

        node = self

        for ch in word:

            ch = ord(ch) - ord('a')

            if node.children[ch] is None:
                node.children[ch] = DictionaryTreeNode()
            
            node = node.children[ch]


class WordDictionary(object):

    def __init__(self):
        
        self.root = DictionaryTreeNode()


    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.root.insert(word)


    def search(self, word:str):
        """
        :type word: str
        :rtype: bool
        """
        queue = Queue()

        queue.put(self.root)

        hight = 0
        num = 1

        while not queue.empty():
            
            if hight >= word.count():
                return False
            
            ch = ord( word[hight] ) - ord('a')

            for _ in range(num):

                node = queue.get()










# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)