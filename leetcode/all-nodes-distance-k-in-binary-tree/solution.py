# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        path = self.path_to_target(root, target, [root])
        previous = None
        # print(path)
        print([n.val for n in path])
        for i, node in enumerate(path):
            if i > k:
                break
            result.extend(self.child_distance_k(node, previous, k-i))
            previous = node
        return result

    def path_to_target(self, root: TreeNode, target: TreeNode, path: List[TreeNode]) -> List[TreeNode]:
        if root == target or root is None:
            return path
        for direction in (root.left, root.right):
            if direction:
                new_path = path.copy()
                new_path.insert(0, direction)
                if successful_direction := self.path_to_target(direction, target, new_path):
                    return successful_direction
        return []

    def child_distance_k(self, root: TreeNode, ignore: TreeNode, k: int) -> List[int]:
        if root == ignore or root is None:
            return []
        if k == 0:
            return [root.val]
        if k == 1:
            result = []
            for direction in (root.right, root.left):
                if direction and direction != ignore:
                    result.append(direction.val)
            return result

        result = self.child_distance_k(root.left, ignore, k-1)
        result.extend(self.child_distance_k(root.right, ignore, k-1))
        return result