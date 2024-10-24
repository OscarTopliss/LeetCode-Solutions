# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None:
            if root2 == None:
                return True
            return False

        if root2 == None:
            return False

        tree1_current_layer = {root1.val: root1}
        tree2_current_layer = {root2.val: root2}

        tree1_next_layer = {}
        tree2_next_layer = {}

        while True:
            for node in tree1_current_layer.values():
                if node.left != None:
                    tree1_next_layer[node.left.val] = node.left
                if node.right != None:
                    tree1_next_layer[node.right.val] = node.right

            for node in tree2_current_layer.values():
                if node.val not in tree1_current_layer:
                    return False
                if node.val in tree1_current_layer:
                    tree1_node_children_vals = [node.val for node in [tree1_current_layer[node.val].left, 
                    tree1_current_layer[node.val].right] if node != None]
                else:
                    break

                
                if node.left != None:
                        if node.left.val not in tree1_node_children_vals:
                            return False
                        else:
                            tree2_next_layer[node.left.val] = node.left
                if node.right != None:
                    if node.right.val not in tree1_node_children_vals:
                        return False
                    else:
                        tree2_next_layer[node.right.val] = node.right
            
            if len(tree1_next_layer) == 0 and len(tree2_next_layer) == 0:
                return True
            
            if len(tree1_next_layer) != len(tree2_next_layer):
                print("48")
                return False

            
            tree1_current_layer = tree1_next_layer
            tree2_current_layer = tree2_next_layer
            
            tree1_next_layer = {}
            tree2_next_layer = {}


            
