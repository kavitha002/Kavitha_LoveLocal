'''
Question
Medium 1

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6. 

'''

'''
METHOD:
If root is null or if root is x or if root is y then return root
Made a recursion call for both
i) Left subtree 

ii)Right subtree

Because we would find LCA in the left or right subtree only.

If the left subtree recursive call gives a null value that means we haven’t found LCA in the left subtree, which means we found LCA on the right subtree. So we will return right.
If the right subtree recursive call gives null value, that means we haven’t found LCA on the right subtree, which means we found LCA on the left subtree. So we will return left .
 If both left & right calls give values (not null)  that means the root is the LCA.
 
'''

#code ->

class Treenodeelement:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(nodes, index, n):
    if index < n and nodes[index] != -1:
        node = Treenodeelement(nodes[index])
        node.left = build_tree(nodes, 2 * index + 1, n)
        node.right = build_tree(nodes, 2 * index + 2, n)
        return node
    return None

def LCA(root, p, q):
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left = LCA(root.left, p, q)
    right =LCA(root.right, p, q)

    if left is not None and right is not None:
        return root

    if left is None:
        return right
    else:
        return left

# Input
nodes = [6, 2, 8, 0, 4, 7, 9, -1, -1, 3, 5]
p = 2
q = 8

# Build the tree from the input list
root = build_tree(nodes, 0, len(nodes))

# Find the lowest common ancestor
ancestor = LCA(root, p, q)

if ancestor is not None:
    print(ancestor.val)
else:
    print("No common ancestor found.")
    
'''
 TRACING: 
 build_tree (index=0):

 Create a TreeNode with value 6.
 Recursively call build_tree for the left child (index = 2 * 0 + 1 = 1).
 Recursively call build_tree for the right child (index = 2 * 0 + 2 = 2).
 build_tree (index=1):

 Create a TreeNode with value 2.
 Recursively call build_tree for the left child (index = 2 * 1 + 1 = 3).
 Recursively call build_tree for the right child (index = 2 * 1 + 2 = 4).
 build_tree (index=3):

 Create a TreeNode with value 0.
 Recursively call build_tree for the left child (index = 2 * 3 + 1 = 7).
 Recursively call build_tree for the right child (index = 2 * 3 + 2 = 8).
 build_tree (index=7):

 Create a TreeNode with value 3.
 Left child is Null.
 Right child is Null.
 build_tree (index=8):

 Create a TreeNode with value 5.
 Left child is Null.
 Right child is Null.
 build_tree (index=4):

 Create a TreeNode with value 4.
 Recursively call build_tree for the left child (index = 2 * 4 + 1 = 9).
 Recursively call build_tree for the right child (index = 2 * 4 + 2 = 10).
 build_tree (index=9):

 Left child is Null.
 Right child is Null.
 build_tree (index=10):

 Left child is Null.
 Right child is Null.
 build_tree (index=2):

 Create a TreeNode with value 8.
 Recursively call build_tree for the left child (index = 2 * 2 + 1 = 5).
 Recursively call build_tree for the right child (index = 2 * 2 + 2 = 6).
 build_tree (index=5):

 Left child is Null.
 Right child is Null.
 build_tree (index=6):
 Create a TreeNode with value 7.
 Left child is Null.
 Right child is Null.
 
 '''


