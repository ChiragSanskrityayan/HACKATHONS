#156 GFG WEEKLY 
#Q2
#soln 2
#editorial
class Solution:

    def geeklandElections(self, n: int, k: int, s: str) -> bool:
        ans = s.count("1") + min(k, s.count("0"))
        return ans > n - ans
