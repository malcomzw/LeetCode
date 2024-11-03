# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #base case, if it contains one node or none 
        if not head or not head.next :
            return 

        #find the middle of the linked list 
        fast, slow = head , head 
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
            
        #REVERSE THE HALF OF THE LINKED LIST 
        prev , curr = None , slow.next 
        slow.next = None 
        while curr:
            next_temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_temp 
        # prev is now the head of the linkedlist second half 
        #MERGE THE 2 HALVES ALTERNATELY 
        first, second = head , prev
        while second :
            tmp1 , tmp2 = first.next , second.next
            first.next = second 
            second.next = tmp1
            first , second = tmp1, tmp2