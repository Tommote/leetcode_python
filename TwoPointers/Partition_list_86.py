# Definition for singly-linked list.




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:


        new_head = ListNode()
        head = ListNode(0,head)

        p_new, p_old = new_head, head.next 
        last_old = head 

        while p_old is not None:

            if p_old.val  < x :
                p_new.next = p_old
                p_new = p_new.next

                last_old.next = p_old.next
                p_old = p_old.next
            
            else:
                last_old = p_old
                p_old = p_old.next
        
        p_new.next = head.next

        return new_head.next



                
