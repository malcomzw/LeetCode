# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # initialize the 2 pointers and find the mid of the linked list
        fast , slow = head , head 

        #move the pointers 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        #step 2 recerse the second half of the linked list 
        prev = None
        # Start from `slow` and reverse the pointers
        while slow:
            temp = slow.next    # Store the next node temporarily
            slow.next = prev    # Reverse the link
            prev = slow         # Move `prev` forward
            slow = temp         # Move `slow` to the next node
            
        #STEP3 - compare the first half and the second reversed half 
        left, right = head, prev 
        while right :
            if left.val != right.val :
                return False 
            left = left.next
            right = right.next 
             
        return True 
