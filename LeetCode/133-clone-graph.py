"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    cloned_nodes = dict()

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        newNode = Node(val=node.val, neighbors=None)
        self.cloned_nodes[node] = newNode
        for n in node.neighbors:
            if n in self.cloned_nodes:
                newNode.neighbors.append(self.cloned_nodes[n])
            else:
                newNode.neighbors.append(self.cloneGraph(n))
        return newNode