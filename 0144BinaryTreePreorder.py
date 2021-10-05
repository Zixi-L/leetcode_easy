# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val]

        result = []

        def research(node):
        # 如果 node 存在就做以下的事情： node 值加入list，再继续搜索 node的左和右
            if node:
                result.append(node.val)
                research(node.left)
                research(node.right)

        research(root)
        return result

