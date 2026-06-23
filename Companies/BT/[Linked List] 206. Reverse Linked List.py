# (Easy) Reverse Linked List

### Question: Given the head of a singly linked list, reverse the list and return the new head.

### Iterative reversal, O(n) time, O(1) space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current: 
            next_node = current.next # save the remainder 
            current.next = prev # KEY STEP: flip this node's link backward
            prev = current # reverse node: current to prev
            current = next_node # connect next node as current

        return prev


# So of the four lines, only one does the actual reversal:
# current.next = prev   # the real work: point this node backward
# The other three are pure bookkeeping that exist only to keep that one line correct on every iteration — keep prev holding the right predecessor, keep moving forward, and don't lose the trail.

# And the order isn't arbitrary — the four lines form a dependency chain, where each line reads a value the next line is about to overwrite:

# current.next = prev is about to destroy current.next, so next_node = current.next must grab it first.
# prev = current is about to overwrite prev, so current.next = prev must use the old prev before that.
# current = next_node is about to overwrite current, so prev = current must capture current into prev before that.



### Relationships with RNN:
# RNN:       h_t   = f(h_{t-1}, x_t)
# Why RNNs are inherently sequential. Remember the loop was a strict dependency chain — you can't do step t until step t-1 finishes, because h_t reads h_{t-1}. 
# That serial dependency is the RNN's defining limitation: you can't parallelize across the time axis the way a transformer can (attention computes all positions at once because nothing is threaded through a carried state). 
# The thing that made the pointer-ordering matter is the same thing that made RNNs slow to train and ultimately got them replaced.

# Why direction of traversal matters — BPTT. The forward pass carries state left to right. 
# Backprop-through-time carries gradients the other way: grad_t = g(grad_{t+1}, …), a fold running right to left over the same unrolled chain. 
# So "traverse the chain in the reverse direction, accumulating something as you go" — the move at the heart of reverseList — is structurally what the backward pass does. 
# And because that backward fold multiplies a long product of Jacobians down the chain, you get vanishing/exploding gradients。