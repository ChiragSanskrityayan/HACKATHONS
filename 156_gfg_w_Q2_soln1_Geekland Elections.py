#156 GFG WEEKLY 
#Q2
#soln 1
#My soln
class Solution:
        def geeklandElections(self, n: int, k: int, s: str) -> bool:     
                    ones = 0
                    zeros = 0
                    for i in range(n):
                        if s[i] == '1':
                            ones += 1
                        else:
                            zeros += 1                
                    return ones + k > zeros - k
                                                                                                                
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        k = int(input())

        s = (input())

        obj = Solution()
        res = obj.geeklandElections(n, k, s)

        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends
