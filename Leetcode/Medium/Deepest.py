# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        max_depth = 0
        total_sum = 0

        while queue:
            node, depth = queue.popleft()

            if depth > max_depth:
                max_depth = depth
                total_sum = node.val
            elif depth == max_depth:
                total_sum += node.val

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return total_sum