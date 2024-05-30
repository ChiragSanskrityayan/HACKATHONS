#156 GFG WEEKLY 
#Q1
#soln 2
#EDITORIAL

from typing import List

class Solution:

    def maximumStrongIndices(self, n: int, x: int, y: int, a: List[int],
                             b: List[int]) -> int:
        j = 0
        ans = 0
        for i in range(n):
            while j < n and b[j] < a[i] - x:
                j += 1
            if j < n and b[j] <= a[i] + y:
                ans += 1
                j += 1
        return ans
