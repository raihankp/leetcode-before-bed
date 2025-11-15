class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Bruteforce:
        # Nested loop 3 times, with the index should be different, and then if they add up to the target which is 0, then add that index to an array that stores the result
        # Time complexity would be O(n^3) damn

        # Solution 2:
        # We could sort the array first
        # Then, we would loop through the nums with the index, and we kind of like "set" the index and the num that we are currently loop to be the first num in our triplets, and then we would loop again using 2 pointer like in Two Sum II, where leftPointer is index + 1 and rightPointer is length - 1. Then just like in Two Sum II, if the triplets sum is > 0, then that means we should reduce the rightPointer by 1, and if the sum is < 0, then we should increment the leftPointer by 1.
        # Example nums = [-1,0,1,2,-1,-4]
        # sortedNums = [-4, -1, -1, 0, 1, 2]


        result = []
        nums.sort()
        print("sorted:", nums)
        for i, num in enumerate(nums):
            # Check if the previous num before this index is the same or not, if yes, then skip until the num is different. this will prevent a duplicate
            if i > 0 and num == nums[i-1]:
                continue

            leftPointer = i + 1
            rightPointer = len(nums) -1

            while leftPointer < rightPointer:
                if num + nums[leftPointer] + nums[rightPointer] > 0:
                    rightPointer -= 1
                elif num + nums[leftPointer] + nums[rightPointer] < 0:
                    leftPointer += 1
                else:
                    # Add to the result
                    result.append([num, nums[leftPointer], nums[rightPointer]])

                    # Move leftPointer until the digit is not the same as the previous one
                    leftPointer += 1
                    while nums[leftPointer - 1] == nums[leftPointer] and leftPointer < rightPointer:
                        leftPointer += 1

        return (result)