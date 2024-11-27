# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #EDGE CASE - if there is no range to traverse 
        if not head or left == right :
            return head 
        #create a dummy node to handle the hrad 
        dummy = ListNode(0)
        dummy.next = head 

        #traverse to the node just before the reversal starts 
        prev = dummy 
        for _ in range(left -1 ):
            prev = prev.next 

        #prev points to the node just before the left position 
        curr = prev.next 

        #STEP 3 - reverse the sublist between left and right 
        prev_sublist =  None # for reversing the sublist 
        for _ in range(right - left + 1):
            #save the next node 
            next_node = curr.next 
            #reverse the curr node pointer 
            curr.next = prev_sublist 
            #move the previous sublist and current forward 
            prev_sublist = curr
            curr = next_node 
        
        #STEP 4 # RECONNECT THE REVERSED SUBLIST 
        prev.next.next = curr 
        prev.next =  prev_sublist 

        return dummy.next
        