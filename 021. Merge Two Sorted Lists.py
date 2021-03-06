# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # dummy is a fixed pointer, pointing to the beginning of the list which is ListNode(0) 
        dummy = cur = ListNode(0) 
        
        # traversal l1 and l2 
        while l1 and l2:
            if l1.val < l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
                
            # why cur=cur.next 
            # Becasue cur always points to the tail of the list
            cur=cur.next
            
        # if l1=[1,2,3] l2=[5,6,7] then in the while loop only l1 is inserted.
        # So we have to insert l2 in this case
        cur.next=l1 or l2
        return dummy.next

# cur, l1, l2, dummy are all pointers 
# Time complexity = O(m+n)
# Space complexity = O(1) 
    # we did not creat any new list, etc. we only swap the same list. 

# A great explaination: https://www.youtube.com/watch?v=GfRQvf7MB3k


