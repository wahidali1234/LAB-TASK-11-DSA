class TreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def is_balanced(root):
    if not root:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)