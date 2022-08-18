# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd_head = ListNode()
        even_head = ListNode()

        i=1

        p_head = head
        p_odd = odd_head
        p_even = even_head

        while p_head is not None:

            if i%2 == 0 :
                p_even.next = p_head
                p_even = p_even.next
            else:
                p_odd.next = p_head
                p_odd = p_odd.next
            
            i += 1
            p_head = p_head.next
        
        p_odd.next = even_head.next
        p_even.next = None
        return odd_head.next

s = Solution()

l1 = ListNode(3)
l2 = ListNode(7)
l3 = ListNode(10)
l4 = ListNode(11)
l5 = ListNode(12)

l1.next = l2
l2.next = l3 
l3.next = l4
l4.next = l5

ll = s.oddEvenList(l1)

while ll :
    print(ll.val)
    ll = ll.next