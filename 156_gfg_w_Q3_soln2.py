#156 GFG WEEKLY 
#Q3
#soln 2
#Editorial

from typing import List

class Solution:
    def minimumK(self, n: int, a: List[int]) -> int:
        k = max(a)
        while True:
            geekina_sum = 0
            geek_sum = 0
            for i in range(n):
                geekina_sum += a[i]
                geek_sum += (k - a[i])
            if geek_sum > geekina_sum:
                break  # Found the minimum k
            k += 1
        return k
