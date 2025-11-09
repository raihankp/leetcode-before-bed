class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Bruteforce:
        # Do a nested loop, where if index i == j, then do not multiply it to the current product
        # Time complexity would be O(n^2)

        # Better Solution:
        # Create 2 array, prefix product and suffix product.
        # Time complexity would be O(n)
        # For example nums = [1,2,3,4]
        # Prefix product would be [1,1,2,6] where first index is assigned as 1
        # Suffix product would be [24,12,4,1] where last index is assigned as 1
        # Then multiply the same index to get the product without self
        # Result = [24,12,8,6]
        # Example 2 nums = [-1,1,0,-3,3]
        # Prefix = [1,-1,-1,0,0]
        # Suffix = [0,0,-9,3,1]
        # Result = [0,0,9,0,0]
        
        numsLength = len(nums)
        prefixProduct = [1] * numsLength
        suffixProduct = [1] * numsLength

        # Generate the prefix product
        for i in range(1, numsLength):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        
        # Generate the suffix product
        for i in range(numsLength - 2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]

        # Multiple the same index
        res = []
        for i in range(numsLength):
            res.append(prefixProduct[i] * suffixProduct[i])
        
        return res