# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        return self._sort( head ) 

    def _find_mind(self, head):
        
        p_fast , p_slow = head , head

        if p_fast.next.next is None:
            p_fast = p_fast.next
        else:
            while p_fast and  p_fast.next:
                p_fast = p_fast.next.next
                p_slow = p_slow.next
        
        head_left, head_right = head , p_slow.next

        p_slow.next = None

        return head_left, head_right

    def _merge(self,head_left,head_right ):
        
        new_head = ListNode()
        ret = new_head
        while head_left or head_right:

            if head_right and head_left:

                if head_left.val > head_right.val:
                    new_head.next = head_left
                    head_left = head_left.next
                else:
                    new_head.next = head_right
                    head_right = head_right.next

            elif head_right :
                new_head.next = head_right
                head_right = head_right.next
            else:
                new_head.next = head_left
                head_left = head_left.next
            new_head = new_head.next
            
        
        return ret.next


    def _sort(self, head:ListNode):

        if head is None or head.next is None:

            return head 

        
        # find the mid 
        head_left, head_right = self._find_mind(head)
        head_left,head_right = self._sort( head_left ), self._sort(head_right)


        return self._merge(head_left, head_right)


s = Solution()

l1 = ListNode(23)
l2 = ListNode(17)
l3 = ListNode(10)
l4 = ListNode(111)
l5 = ListNode(12)

l1.next = l2
l2.next = l3 
l3.next = l4
l4.next = l5

ll1 = s.sortList(l1)

while ll1 :
    print(ll1.val)
    ll1 = ll1.next
print(1111111)
# while ll2 :
#     print(ll2.val)
#     ll2 = ll2.next