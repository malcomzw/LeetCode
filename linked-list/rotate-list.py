# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #edge cases
        if not head or not head.next or k ==0:
            return head 
       
        #step1 . calculate the length of the list 
        length = 1
        tail = head 
        while tail.next :
            tail= tail.next 
            length += 1 

        #find effective rotations 
        k %= length
        if k == 0:
            return head #no rotation needed 
        
        #make the list circular 
        tail.next = head #connect head to tail 

        #find the new tail 
        tailSteps = length -k 
        new_tail = head 
        for _ in range(tailSteps -1 ):
            new_tail = new_tail.next 
        
        #break the link 
        new_head = new_tail.next 
        new_tail.next = None 

        return new_head 
