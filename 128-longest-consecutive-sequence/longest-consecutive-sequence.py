class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Bruteforce:
        # Sort them, and then loop from the second element, and compare it with the previous element if the difference is 1, then it's consecutive elements, then add 1 to the currResult as int, if the difference is more than 1, then set the result as a max and redefine currResult as 0 again, and compare the new currResult with the max and set the maximum from those 2
        
        # Better Solution:
        # First, we turn the nums into a set, where set is based on hash so the time complexity to search if a digit is present in the set is only O(1).
        #  We loop through the nums, and check if the digit BEFORE the digit we're currently looping is digit minus 1,
        # we do this to know if the digit could be the starting of sequence or not, 
        # if yes, then we could increment the sequence by doing loop and check if the digit + 1 is available in the set or not

        numsSet = set(nums)
        longestSequence = 0

        for num in numsSet:
            if (num - 1) not in numsSet:
                # This means that the num could be the starting of a sequence
                currLength = 1
                numSequence = num + 1
                while numSequence in numsSet:
                    currLength += 1
                    numSequence += 1
                longestSequence = max(longestSequence, currLength)        

        return longestSequence