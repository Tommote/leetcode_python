# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):

        self.curr = root
        self.node_stack = []


    def next(self) -> int:

        while self.curr :
            self.node_stack.append(self.curr)
            self.curr = self.curr.left
        
        self.curr = self.node_stack.pop()

        ret = self.curr.val

        self.curr = self.curr.right

        return ret


    def hasNext(self) -> bool:

        return not (self.curr is None and len(self.node_stack)==0 )


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()