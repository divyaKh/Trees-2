"""
 TC = O(N) and SC = O(H)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        if root != None:
            self.dfs(root, 0)
        return self.answer

    def dfs(self, root, sumSoFar):
        if root != None:
            sumSoFar = sumSoFar*10 + root.val
            if root.left == None and root.right == None:  #leaf node
                self.answer += sumSoFar
                return
            self.dfs(root.left, sumSoFar)   
            self.dfs(root.right, sumSoFar)