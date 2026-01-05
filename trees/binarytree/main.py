# Binary tree implementation
class TreeNode: 
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 


# This method builds an example tree based on previous impl.
# Should be ready for other modules to use
def build_tree_example() -> list[TreeNode]:
    root = TreeNode("R")
    nodeA = TreeNode("A")
    nodeB = TreeNode("B")
    nodeC = TreeNode("C")
    nodeD = TreeNode("D")
    nodeE = TreeNode("E")
    nodeF = TreeNode("F")
    nodeG = TreeNode("G")

    root.left = nodeA
    root.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG
    return root


tree = build_tree_example()
