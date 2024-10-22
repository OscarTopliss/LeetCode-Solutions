# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        totals = [root.val]
        previous_level_nodes = [root]
        current_level_nodes = []
        current_level_total = 0

        while True:
            for node in previous_level_nodes:
                if node.left != None:
                    current_level_nodes.append(node.left)
                    current_level_total += node.left.val
                if node.right != None:
                    current_level_nodes.append(node.right)
                    current_level_total += node.right.val
            if len(current_level_nodes) == 0:
                break
            previous_level_nodes = current_level_nodes
            totals.append(current_level_total)
            current_level_nodes = []
            current_level_total = 0
        
        if len(totals) < k:
            return -1
        
        totals.sort(reverse = True)
        return totals[k - 1] 
