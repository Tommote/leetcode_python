# Definition for singly-linked list.
from typing import List
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        new_head = ListNode()

        p_head = new_head
        p_list = PriorityQueue()

        for p in lists:
            if p :
                p_list.put( (p.val, p) )

        while not p_list.empty():

            min_p = p_list.get()[1]
            p_head.next = min_p
            p_head = p_head.next

            if min_p.next:
                p_list.put((min_p.next.val, min_p.next))

        return new_head.next



s = Solution()

l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(2)

l1.next = l3 

ll = s.mergeKLists([ l1, l2 ])

while ll:
    print(ll.val)
    ll = ll.next