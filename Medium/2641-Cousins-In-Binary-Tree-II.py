# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_layer = [root]
        root.val = 0
        next_layer = []
        original_values = {}

        while True:
            for node in current_layer:
                if node.left != None:
                    next_layer.append(node.left)
                    original_values[node.left] = node.left.val
                if node.right != None:
                    next_layer.append(node.right)
                    original_values[node.right] = node.right.val

            if len(next_layer) == 0:
                break
            
            layer_sum = sum(list(original_values.values()))
            
            for node in current_layer:
                child_nodes = [child for child in [node.left, node.right] if child != None]

                if len(child_nodes) == 0:
                    continue

                child_sum = sum([node.val for node in child_nodes])
                
                cousin_sum = layer_sum - child_sum

                for child in child_nodes:
                    child.val = cousin_sum
                

            current_layer = next_layer
            next_layer = []
            original_values = {}
        
        return root
