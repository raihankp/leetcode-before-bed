class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bruteforce:
        # Do a nested loop, the outer loop would store the digit that will add up to the target, the inner loop would find that digit. For example, in nums = [2,7,11,15] with target=9, the first outer loop will store digitToFind = target - 2 = 7, then it will find that digitToFind in the inner loop. Time Complexity would be O(n^2) bcs we need to do nested loop

        # Better Solution:
        # Only do iteration once, while we do the iteration, we need to store the digit being iterated into a hashmap with the indices as the value. For example, while we iterate [2, 7, 11, 15], we store {2:0} in the first digit. Before storing that, we could find the complement first if it's inside the hashmap (we calculate it by substracting target to the digit being iterated, i.e. 9 - 2 = 7), if yes, then directly return both indices

        complementDigitMap = {}

        for idx, num in enumerate(nums):
            complementDigit = target - num
            if complementDigit in complementDigitMap:
                return [complementDigitMap[complementDigit], idx]
            else:
                complementDigitMap[num] = idx
            
        return -1
