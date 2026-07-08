# Given the head of a linked list, remove the n-th node *from the end of the list* and return the head.
# Examples:

# head = [1,2,3,4,5], n = 2 → [1,2,3,5]
# head = [1], n = 1 → []
# head = [1,2], n = 1 → [1]

# Constraints:

# Number of nodes is sz, with 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

### Thoughts
## sliding window / 双指针two pointer
# left: the node before the node to be deleted
# right: faster than left for n steps
# once right reaches end of linked list, left should point to the node to be deleted

### TC: O(m), m is length of linked list, every node visited at most twice (left and right pointers)
### SC: O(1)

# But trace this on example 2: head = [1], n = 1.
# Your advance loop runs n + 1 = 2 times:

# Step 1: right = head.next → None
# Step 2: right = None.next → 💥 AttributeError


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_node(head, n):
    # prevent that only one node in head 
    dummy = ListNode(0)
    dummy.next = head
    left = right = dummy

    # fast move n steps first
    for _ in range(n + 1):
        right = right.next

    # move left and right togther until right reaches end of list
    while right:
        left = left.next 
        right = right.next 

    left.next = left.next.next # delete that target node

    # return head of new linked list
    return dummy.next



