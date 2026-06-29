# LeetCode 23 — Merge k Sorted Lists
# You're given an array of k linked lists, each sorted in ascending order. Merge them all into one sorted linked list and return its head.

# Example 1
# Input:  lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,5,6]


### Thoughts
# 核心想法是,每条链表内部已经有序,所以每条链表当前的最小值就是它的头节点。
# 把 K 个头节点放进堆里,堆顶永远是全局最小的那个节点 - 自动维护。
# 取出堆顶接到结果链表上,再把它的 next(如果存在)推回堆里,重复直到堆空。

# 堆 - 存最小元素
# 从每个list里取出最小节点放入堆
# while 堆 not empty：
# 从堆里取出最小节点（自动维护），放入结果链表
# 如果取出的节点后跟着下一个节点，把下一个节点也放入堆
# 持续while loop直到堆为空

### TC: N 是所有链表加起来的总节点数,K 是链表条数。每个节点都会进堆一次、出堆一次,堆的大小始终不超过 K,所以单次 push/pop 是 O(log K),总共 N 个节点就是 O(N log K)。
# SC: O(K),堆里最多同时存 K 个节点。

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            if node: # not empty
                heapq.heappush(heap, (node.val, node))

        # create output list
        dummy = ListNode(0)

        while heap: # not empty - go through every element in all lists
            val, node = heapq.heappop(heap) # pop the smallest element
            dummy.next = node # add this node to output list
            
            if node.next: # if have next element, put into heap
                heapq.heappush(heap, (node.next.val, node.next)) 

        return dummy.next # the whole merged list





