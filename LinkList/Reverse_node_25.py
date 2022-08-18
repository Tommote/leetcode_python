# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        if head is None or head.next is None or k==1:
            return head 
        
        dummy_head = ListNode()
        dummy_head.next = head

        i = 1

        p_group_start = dummy_head
        p_group_end = dummy_head

        p_start = head 

        while p_start:
            print('sssssssss', p_start.val)
            if i == k :
                print('dsfsdf',p_start.val,p_group_end.val)
                p_group_end = self._reverseOneGroup( p_group_end, p_start )
                i = 0
                p_start = p_group_end
            i += 1
            p_start = p_start.next

        return dummy_head.next

    def _reverseOneGroup(self, p_group_start, p_group_end):

        temp_p = p_group_start.next

        p_curr = p_group_start.next

        p_group_start.next = p_group_end

        

        while p_curr is not p_group_end:
            print('ddddd',p_curr.val)
            p_store = p_curr.next

            p_curr.next = p_group_end.next
            p_group_end.next = p_curr

            p_curr = p_store

        return temp_p
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

ll = s.reverseKGroup(l1, 2)
# ll = l1
print('ddddddddddddddddddddddddddddd')
while ll:
    print(ll.val)
    ll = ll.next