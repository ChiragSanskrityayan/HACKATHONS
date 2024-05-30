#156 GFG WEEKLY 
#Q4
#soln 1
#Editorial
from typing import List

from typing import List


class Solution:

    def citiesVisited(self, n: int, m: int, isHaunted: List[int],
                      edges: List[List[int]]) -> int:
        ans = [0]
        adj = [[] for _ in range(n + 1)]
        for el in edges:
            a, b = el[0], el[1]
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, par, am):
            if am > m:
                return

            leaf = True
            for el in adj[node]:
                if el != par:
                    leaf = False
                    if isHaunted[el - 1]:
                        dfs(el, node, am + 1)
                        
                    else:
                        dfs(el, node, 0)
                        

            if leaf:
                if am <= m:
                    ans[0] += 1

        dfs(1, -1, isHaunted[0])
        return ans[0]


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


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):

        n = int(input())

        m = int(input())

        isHaunted = IntArray().Input(n)

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.citiesVisited(n, m, isHaunted, edges)

        print(res)

# } Driver Code Ends
