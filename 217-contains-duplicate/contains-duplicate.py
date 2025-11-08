class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Bruteforce: 
        # Create nested loops, the outer loop would store the digit that we want to find the duplicate and the inner loop would be to find the same digit as the digit stored in the outer loop. Time Complexity would be O(n^2)

        # Better Solution:
        # Iterate only once, while iterating, store the digit into a hashmap or set if there is no occurence of that digit yet, but if there is occurence, means the digit appears twice
        setNums = set()

        for num in nums:
            if num in setNums:
                return True
            else:
                setNums.add(num)
            
        return False