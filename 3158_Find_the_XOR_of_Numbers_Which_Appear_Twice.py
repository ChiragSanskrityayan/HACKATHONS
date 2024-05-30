class Solution(object):
    def duplicateNumbersXOR(self, nums):
        
        XOR_prod = 0
        once = set()
        twice = set()

        for num in nums:
            if num in once:
                twice.add(num)
            else:
                once.add(num)

        for num in twice:
            XOR_prod ^= num

        return XOR_prod
