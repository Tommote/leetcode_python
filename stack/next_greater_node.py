# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        m_stack = []
        
        temp_head = []
        while head :
            temp_head.append(head.val)
            head = head.next
        N = len(temp_head)
        ret = [0] * N
        for i in range(N-1, -1, -1):

            while len(m_stack)>0 and m_stack[-1] < temp_head[i]:
                m_stack.pop()

            if len(m_stack)>0:
                ret[i] = m_stack[-1]
            m_stack.append[temp_head[i]]
        
        return ret 
s = Solution()
print(s.nextLargerNodes( [2,1,5] ))