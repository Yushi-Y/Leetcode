# LeetCode 146 — LRU Cache (Medium)
# Full description:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:

# LRUCache(int capacity) — Initialize the LRU cache with positive size capacity.
# int get(int key) — Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) — Update the value of the key if it exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.
# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.

# Type of question: Design problem.
# Topic tags (LeetCode's own): Hash Table, Linked List, Design, Doubly-Linked List.
# The core tension: you need two things at once that no single common structure gives you —

# O(1) lookup by key (which points you toward one data structure), and
# O(1) tracking + reordering of "recency" so you can find and evict the least-recently-used item instantly (which points toward a different one).


### Thoughts
# 想象你桌上只能放 2 本书（这就是 capacity = 2）。书架很远，每次去拿书很慢，所以你想把"最常用"的书留在桌上。
# 规则是：当桌子满了，又要放新书时，你扔掉最久没碰过的那本（Least Recently Used = 最近最少使用）。
# 举个例子（capacity = 2）：
# put(1, 1)   桌上: [书1]
# put(2, 2)   桌上: [书1, 书2]   （满了）

# get(1)      你拿起书1看了一下 → 书1 变成"刚用过"
#             桌上顺序: [书2, 书1]   （书2 现在是最久没碰的）

# put(3, 3)   桌子满了，要放书3
#             → 扔掉最久没碰的"书2"
#             桌上: [书1, 书3]

# get(2)      书2 已经被扔了 → 返回 -1（找不到）
# 两个核心操作：

# get(key)：如果书在桌上，返回它的值，并且把它标记成"刚用过"。
# put(key, value)：放一本书。如果桌子满了，先扔掉最久没用的。

# 为什么这题难？
# 题目要求 get 和 put 都是 O(1)。也就是说：

# 你要能瞬间找到某本书 →（你已经答对了）hashmap
# 你还要能瞬间知道"哪本书最久没碰"，并且每次用完一本书就瞬间把它挪到"最新"的位置。

# 第 2 点 hashmap 做不到，因为它没有"顺序"概念。所以需要再配一个能维护顺序的结构。

### Hashmap + Double linked list
#. 链表负责"顺序"（谁新谁旧）。
# 链表从左到右就是从"最久没用"到"最近用过"。head 那端最旧，tail 那端最新。
# 三个操作怎么都做到 O(1)：
# get(key)：hashmap 跳到节点 → 拿到 value → 把这个节点摘下来挪到 head（标记成刚用过）。摘除靠双向链表的 prev/next，O(1)。
# put(key, value) 新增：建节点，挂到 tail，hashmap 里加 key → 节点。
# 容量满了要淘汰：直接删 head 旁边那个最旧节点，同时用它的 key 去 hashmap 里把那条记录也删掉（所以节点里要存 key，不只是 value，这点很多人会漏）。

### 为什么用双链表不是单链表
# 核心原因：LRU 里每次 get/put 都要把链表中间的某个节点摘出来，挪到 tail。 而"摘除一个节点"这个动作，单向链表做不到 O(1)。
# 具体看"删除中间节点 B"要做什么：
# 删除前:   A  →  B  →  C
# 删除后:   A  ───────→  C        (让 A.next 指向 C，跳过 B)
# 要完成这一步，你需要改 A 的 next 指针，让它指向 C。也就是说你必须知道 B 的前一个节点 A 是谁。
# 现在对比两种链表：
# 双向链表 —— B 自己存了 prev，所以：
# A = B.prev          # 直接拿到，O(1)
# C = B.next          # 直接拿到，O(1)
# A.next = C
# C.prev = A          # 摘除完成，全程 O(1)
# 单向链表 —— B 只有 next，不知道 A 是谁。想找到 A，只能从 head 开始一个个走，直到找到"那个 next 指向 B 的节点"：
# p = head
# while p.next != B:   # 最坏要走到链表末尾
#     p = p.next
# # 这一圈就是 O(n)，破坏了题目要求
# 而且别忘了：你是通过 hashmap 直接跳到 B 这个节点的（不是从 head 顺着走过来的），所以你天然就"空降"在 B 身上，手里没有 A。单向链表这时候就抓瞎了 —— 这正是为什么必须用双向。
# 一句话总结：hashmap 让你 O(1) 跳到任意节点，但"跳到之后还能 O(1) 摘除它"必须靠 prev 指针 —— 这就是双向链表存在的理由。
# class 


### TC: O(1), SC: O(capacity)
# node in double linked list - O(1) insert/remove 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
       # set up cache and double linked list basic structure
       self.capacity = capacity
       self.cache = {} # hashmap: key -> node
       self.head = Node(0, 0)
       self.tail = Node(0, 0)
       self.head.next = self.tail
       self.tail.prev = self.head

    def _remove(self, node):
        # remove node from double linked list
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _move_head(self, node):
        # move node to right after the head of double linked list (most recently used)
        node.prev = self.head
        node.next = self.head.next
        # order cannot change, as self.head.next need to be the actual next first, before reassigning to the node
        self.head.next.prev = node
        self.head.next = node

        

    def get(self, key):
       # if key in cache, move node to head, return value, 
       # else return None
        if key in self.cache:
            node = self.cache[key]
            # remove from list
            self._remove(node)
            # move it to the head (most recent)
            self._move_head(node)
            return node.value
        return -1
       
    
    def put(self, key, value):
        # if key in cache, update value, move to head; 
        # else, add new node to cache and head
        # if over capacity, remove tail.prev from list, remove it from cache

        if key in self.cache:
            node = self.cache[key]
            node.value = value
             # remove from list
            self._remove(node)
            # move it to the head (most recent)
            self._move_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            # move it to the head (most recent)
            self._move_head(node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                # remove LRU from list
                self._remove(lru_node)
                del self.cache[lru_node.key]




### Follow up: how to use LRU to KV Cache in LLM reasoning?
# Storage granularity — yes, mainstream stores every token. During autoregressive decoding, each generated token's K and V vectors are appended to the cache (per layer, per KV-head) so history doesn't get recomputed. 
# Within a single sequence, the baseline is to keep every token up to the current position. That's why it's expensive — KV cache often exceeds model weights in memory for long contexts. Optimizations split into two kinds: ones that shrink the per-token cost while still storing every token (GQA/MQA, KV quantization), and ones that don't store every token (StreamingLLM, H2O) — but those trade quality and aren't the general default yet.
# Where LRU comes in — cross-request prefix caching, not within a sequence. You generally can't evict tokens inside one sequence, since later attention still needs all the history. 
# LRU shows up when KV is reused across requests — prefix caching (vLLM's automatic prefix caching, SGLang's RadixAttention). Many requests share a prefix: the same system prompt, few-shot examples, RAG documents, or earlier conversation turns. Compute that prefix's KV once, reuse it for every request that matches. GPU memory is finite, so a full cache needs an eviction policy, and LRU is the natural fit.
# The LeetCode problem maps almost 1:1: the hashmap key becomes a content hash of a token block (the prefix hash); the doubly linked list becomes the recency ordering for eviction; get is a prefix-cache lookup that lets a request skip that chunk of prefill on a hit; put/eviction reclaims the least-recently-used KV blocks when memory runs out. 
# In practice pure LRU gets modified: reference counting (blocks in active use can't be evicted until refcount hits zero), cost-aware eviction (longer prefixes are more expensive to recompute, so eviction weights by length/cost rather than pure recency), and tree-based tie-breaking (RadixAttention prefers evicting leaves and keeping shared roots).


# What a node/block actually stores is the KV tensors (the computed key and value vectors) for a contiguous span of tokens — e.g. vLLM uses fixed 16-token blocks. That's the value: the heavy payload, the whole reason to cache, since it's what you'd otherwise recompute.


