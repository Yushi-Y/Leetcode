# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        # Initialize a dummy head node as a basis for the merged listnode
        dummy = ListNode(0)
        # Add a pointer to the dummy node
        pointer = dummy
        
        # Add the smallest element of both listnodes to the merged listnode
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else: 
                pointer.next = l2
                l2 = l2.next

        # Move the pointer to the current value 
            pointer = pointer.next

        # For remaining elements in a list
        if l1:
            pointer.next = l1
        
        if l2:
            pointer.next = l2

        # Return the merged list by excluding the dummy node
        return dummy.next




# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current: 
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

