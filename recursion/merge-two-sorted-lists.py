# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node taht will be start  of the newlist 
        dummy = ListNode(-1) 
        current = dummy 
        
        #step2 , traverse both lists checking the nodes in both if valid 
        while list1 and list2 :
            #check the conditions of which node to pick first 
            if list1.val <= list2.val :
                current.next = list1
                list1 = list1.next 
            else :
                current.next = list2
                list2 = list2.next 
            current = current.next
        #case handle , if one of the lists is empty 
        if list1:
            current.next = list1
        else:
            current.next = list2 
        
        return dummy.next