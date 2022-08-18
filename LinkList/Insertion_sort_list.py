# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:


        p_start = head

        new_head = ListNode(-1e9)
        p_sorted_start = new_head
        p_sorted_end = ListNode(1e9)

        p_sorted_start.next = p_sorted_end

        

        while p_start :


            
            p_temp = p_sorted_start

            p_store = p_start.next

            while p_temp.next:

                if p_start.val > p_temp.next.val:

                    p_temp =   p_temp.next
                
                else:
                    break
            
            p_start.next = p_temp.next
            p_temp.next=p_start

            p_start = p_store

        p = p_sorted_start
        while p:
            if p.next is p_sorted_end:
                p.next = None
                break
            p = p.next

        return new_head.next


s = Solution()

l1 = ListNode(33)
l2 = ListNode(43)
l3 = ListNode(2)

l1.next = l2 
l2.next = l3 

ll = s.insertionSortList(l1)

while ll:
    print(ll.val)
    ll = ll.next





