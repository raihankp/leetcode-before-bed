class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Bruteforce:
        # We could do like the best approach in Two Sum I, which is using hashmap, but this problem wants us to use only constant O(1) extra space
        # Maybe we could do the nested loop and check the pair, but it will be too long

        # Better Solution:
        # Use two pointer
        # Start from the left side, check the number

        # [1,2,3,4,5,6,7]
        # target = 8
        # 1,7
        # 2,6
        # 3,5
        # target = 18
        # [2,7,8,11,15]
        # [1,4]
        #     - while loop until the leftPointer > rightPointer
        #     - check if the sum of both is equals target then return their index
        #     - check if the sum of both is more than the target
        #         - if yes then reduce the right pointer by one
        #         - check it again, until the sum of both is less than the target then quit and add the left pointer by one

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
            