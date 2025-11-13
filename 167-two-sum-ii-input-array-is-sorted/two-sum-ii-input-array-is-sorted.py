class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Bruteforce:
        # We could do like the best approach in Two Sum I, which is using hashmap, but this problem wants us to use only constant O(1) extra space
        # Maybe we could do the nested loop and check the pair, but it will be too long

        # Better Solution:
        # Use two pointer
        # Check if the sum of the two number of those pointer is:
        # 1) Bigger than the target -> this means that we could decrease the sum by decrement rightPointer by 1 (like there is no otherway, if we move the leftPointer by one, it will make the sum bigger right)
        # 2) Smaller than the target -> This means that we could increase the sum by increment leftPointer by one
        # Same with the target, then return those indices

        # Example
        # target = 18
        # [2,7,8,11,15]
        # Answer should be indices [1,4] (don't forget that the problem wants the index to starts from 1, not 0)

        leftPointer = 0
        rightPointer = len(numbers) - 1

        while leftPointer < rightPointer:
            if numbers[leftPointer] + numbers[rightPointer] == target:
                return [leftPointer + 1, rightPointer + 1]
            
            if numbers[leftPointer] + numbers[rightPointer] > target:
                rightPointer -= 1
            else:
                leftPointer += 1

        return []
            