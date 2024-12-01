# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node 
        dummy = ListNode(0, head)

        #pointers 
        prev, curr = dummy , head 

        #iterate while we have atleast 2 nodes
        while curr and curr.next :
            nxtPair = curr.next.next 
            second = curr.next 

            #reverse the current pointers 
            second.next = curr 
            curr.next = nxtPair 
            prev.next = second 

            prev = curr 
            curr = nxtPair 
        return dummy.next