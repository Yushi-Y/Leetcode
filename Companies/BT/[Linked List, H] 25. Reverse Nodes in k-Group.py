### Question
# Given the head of a linked list, reverse the nodes k at a time and return the modified list. 
# If the number of nodes isn't a multiple of k, leave the leftover tail as-is. You may only rearrange the nodes themselves — not swap their values.
# Example:
# Input:  1 -> 2 -> 3 -> 4 -> 5,  k = 2
# Output: 2 -> 1 -> 4 -> 3 -> 5

# Input:  1 -> 2 -> 3 -> 4 -> 5,  k = 3
# Output: 3 -> 2 -> 1 -> 4 -> 5


### Thoughts
# for each group of size k, "reverse"
# connect the reversed groups
# left over nodes, leave them

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # helper function to reverse a group of k nodes
        def reverse(start, end):
            # curr, prev, next
            # in a while loop, curr.next = prev - reverse step
            # loop stops until curr == end
            curr = start
            prev = end 
            while curr != end:
                next = curr.next # storing the next node
                curr.next = prev # reverse step
                prev = curr # 后移一步prev 和 curr，继续做reverse step in loop
                curr = next
            return prev # the head of new reversed group
        
        # 怎么把每个反转块接到前一块? 这就是 dummy head 出场的地方。维护一个 group_prev 指针 = 「上一组反转后的尾节点」(开头时就是 dummy)。
        dummy = ListNode(0, head)
        group_prev = dummy # tail of last reversed group

        while True:
            # ① 从 group_prev 往前走 k 步,找第 k 个节点 kth
            #    如果走的过程中 kth 变成 None → return dummy.next - whatever nodes are left
            kth_node = group_prev # store group_prev
            for _ in range(k): # move k steps
                kth_node = kth_node.next
                if not kth_node: # empty
                    return dummy.next # less than k node left
            
            # ② group_end = kth.next       # group 后面那个节点(exclusive 边界)
            #    start     = group_prev.next # 当前 group 的第一个节点
            group_next = kth_node.next # group 后面那个节点(exclusive 边界),不参与反转
            start = group_prev.next # start of the new group
            new_head = reverse(start, group_next) # 确保反转新组start到end（不包含end边界的所有node）


            # ④ 重接前一块:group_prev.next = ???
            group_prev.next = new_head # 上一组尾巴接到新组头

            # ⑤ 推进 group_prev 到 ???   (想一下:反转后,哪个节点变成了这一组的尾巴?)
            group_prev = start # start在reverse了之后，现在是当前反转组的尾巴，把group prev指向它，这样下一轮反转时，上一组的尾巴就正确了

       
### 每个节点被 reverse 访问一次,加上找 kth 时每组又走一遍 k 步 —— 但整体每个节点的访问是常数次,所以 O(n) time, O(1) space(只用了几个指针,没有递归栈）

        




