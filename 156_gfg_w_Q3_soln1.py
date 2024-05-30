#156 GFG WEEKLY 
#Q3
#soln 1
#My soln

from typing import List

class Solution:
    def minimumK(self, n : int, a : List[int]) -> int:
        
        sum_geekina = sum(a)
        max_a = max(a)
        min_k = (2*sum_geekina)//n +1
        return max(max_a, min_k)

#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumK(n, a)

        print(res)

# } Driver Code Ends
