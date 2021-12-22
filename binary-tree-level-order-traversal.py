# pass on Leetcode?: yes  
# approach: Iterative BFS
# TC: O(N), SC: O(n/2) -> O(N)
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        
        q = deque([root])
        res = []
        
        while len(q) is not 0:
            size = len(q)
            li = []
            for i in range(size):
                curr = q.popleft()
                li.append(curr.val)
                if (curr.left): q.append(curr.left)
                if (curr.right): q.append(curr.right)
            res.append(li)
        
        return res