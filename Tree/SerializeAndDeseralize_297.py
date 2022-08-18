import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return '' 
        
        ret = '' 

        queue_list = queue.Queue(-1)
        queue_list.put(root)

        while not queue_list.empty() :

            curr_node = queue_list.get() 

            if curr_node is None :
                ret += 'null '
                continue 

            ret += str(curr_node.val) + ' '
            queue_list.put(curr_node.left)
            queue_list.put(curr_node.right)
        
        return ret 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.strip().split(' ')

        if data[0] == '' :
            return None 
        
        queue_lsit = queue.Queue()
        root = TreeNode( int(data[0]) )
        queue_lsit.put( root )
        curr_p = 1 

        while curr_p<len(data) :

            temp_node_left , temp_node_right = self._build_node(data[curr_p]) , self._build_node(data[curr_p+1]) 

            curr_node = queue_lsit.get()

            curr_node.left = temp_node_left
            curr_node.right = temp_node_right  

            if temp_node_left :
                queue_lsit.put(temp_node_left)
            if temp_node_right:
                queue_lsit.put(temp_node_right)
            curr_p += 2
        return root 

    def _build_node(self, data_item):

        if data_item=='null':
            return None 
        else:
            return TreeNode(int( data_item ))

r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)
r5 = TreeNode(5)

r1.left = r2 
r1.right = r3 
r3.left = r4 
r3.right = r5 

s = Codec()
t = s.serialize(r1)
print(t)
root = s.deserialize(t) 
print(s.serialize(root ))
# print(t.strip().split(' '))