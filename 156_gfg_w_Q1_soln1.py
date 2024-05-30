#156 GFG WEEKLY 
#Q1
#soln 1
#My soln
from typing import List
class Solution:
    def maximumStrongIndices(self, n : int, x : int, y : int, a : List[int], b : List[int]) -> int:
        i =0
        j =0
        count = 0 
        
        while i<n and j<n:
            if a[i] -x <= b[j] <= a[i]+y:
                count +=1
                i+=1
                j+=1
            elif b[j] < a[i] -x:
                j +=1
            else:
                i +=1
                
        return count
