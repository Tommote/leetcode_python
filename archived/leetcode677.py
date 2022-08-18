
class TreeNode(object):

    def __init__(self):
        
        self.val = 0
        self.edge = [ None for i in range(26) ]

class MapSum(object):

    def __init__(self):

        self.root = TreeNode()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """

        temp_l = self.root

        for ch in key:

            next_l = temp_l.edge[ ord(ch) - ord('a') ]

            if next_l is None:
                temp_l.edge[ ord(ch) - ord('a') ] = TreeNode()
                temp_l = temp_l.edge[ ord(ch) - ord('a') ]
            else:
                temp_l = next_l

        temp_l.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        temp_l = self.root

        for ch in prefix:

            next_l = temp_l.edge[ ord(ch) - ord('a') ]

            if next_l is None:
                return 0
            else:
                temp_l = next_l
    
        return self._dfs(temp_l)

    def _dfs(self, node):

        if node is None:
            return 0
        
        res = node.val

        for subNode in node.edge:

            res +=  self._dfs(subNode)
        
        return res




obj = MapSum()

obj.insert('apple',3)
print(obj.sum('ap'))

obj.insert('app',2)

print(obj.sum('ap'))