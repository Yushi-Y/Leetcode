# Middle of the Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    if not head:
        return None
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr




# Linked List Cycle II
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head: ListNode) -> ListNode:
    # First, check if there is a cycle in the list
    # if there is a cycle, the slow pointer and faster pointer will meet
    slow_ptr = head
    fast_ptr = head
    has_cycle = False

    # The 'and' condition ensures that the loop terminates in both cases with and without a cycle
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            has_cycle = True
            break
    
    # If there is no cycle, return -1
    if not has_cycle:
        return -1
    
    # If there is a cycle, find the node where the cycle begins
    ptr1 = head
    ptr2 = fast_ptr # this is the node where slow_ptr and fast_ptr meet
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1.val
