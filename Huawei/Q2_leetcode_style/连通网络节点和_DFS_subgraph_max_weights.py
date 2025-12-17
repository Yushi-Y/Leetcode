# Define DFS to recursively explore a complete subgraph and return the max weight node and total weight
# Parse weights, adjacencys, and id maps from nodes
# Perform DFS at every unvisited node
# Finally print the path with maximum total weight


import sys


# Start at node u
#  ├── visit all its neighbors
#  │    ├── visit their neighbors
#  │    │    └── and so on...
#  └── stop when no new node to visit

def dfs(start_idx, adj, weights, visited):
    """Return (max_total_weight, node_idx_with_max_weight)"""
    visited[start_idx] = True
    total_weight = weights[start_idx]
    max_idx = start_idx

    neighbor_idxs = adj[start_idx]
    for neighbor_idx in neighbor_idxs:
        if not visited[neighbor_idx]:
            new_weight, new_max_idx = dfs(neighbor_idx, adj, weights, visited)
            total_weight += new_weight
            if weights[new_max_idx] > weights[max_idx]:
                max_idx = new_max_idx

    return total_weight, max_idx



if __name__ == "__main__":
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        sys.exit(0)

    n = int(lines[0])
    m = int(lines[1+n])

    nodes = []
    weights = []
    id_map = {}
    adj = [[] for _ in range(n)]

    for i in range(1, n+1):
        node, weight = lines[i].split()
        nodes.append(node)
        weights.append(int(weight))
        id_map[node] = i-1

    for j in range(n+2, n+2+m):
        node1, node2 = lines[j].split()
        idx_1 = id_map[node1]
        idx_2 = id_map[node2]
        adj[idx_1].append(idx_2)
        adj[idx_2].append(idx_1)

    visited = [False] * n
    best_max_weight = -1
    final_max_node = None

    # Need to do DFS starting at ALL nodes, not just one
    for i in range(n):
        if visited[i] == False:
            start_idx = i
            max_weight, max_idx = dfs(start_idx, adj, weights, visited)
            if max_weight > best_max_weight:
                best_max_weight = max_weight
                final_max_node = nodes[max_idx]

    print(final_max_node, best_max_weight)








