class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        indices = {} 
        for i, num in enumerate(nums):
            if num == x:
                if x not in indices:
                    indices[x] = []
                indices[x].append(i)
           
        result = []
        
        for query in queries:
            
            if x not in indices or query > len(indices[x]):
                result.append(-1)
            else:
                result.append(indices[x][query - 1])
        
        return result
