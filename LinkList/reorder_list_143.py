# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node_list = []

        p_head = head
        while p_head :
            node_list.append(p_head)
            p_head = p_head.next


        dummy_head = ListNode()

        mid_n = len(node_list)//2
        N = len(node_list)
        p_head = dummy_head
        
        for i in range(mid_n):

            p_head.next = node_list[i]
            p_head = p_head.next

            p_head.next = node_list[N-i-1]
            p_head = p_head.next
        
        if N%2==0 :
            p_head.next = None 
        else:
            p_head.next = node_list[mid_n]
            node_list[mid_n].next = None



s = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2 
l2.next = l3 
l3.next = l4
l4.next = l5

ll = s.reorderList(l1)
ll = l1
print('ddddddddddddddddddddddddddddd')
while ll:
    print(ll.val)
    ll = ll.next