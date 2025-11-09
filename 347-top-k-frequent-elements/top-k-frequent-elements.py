from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bruteforce:
        # Store each integer count in a hashmap, and  we could sort the hashmap from the value by the largest first, then we get the first k-th value. Time complexity would be O(n log n) because we need to sort it where fastest sorting algorithm O(n log n)

        # Better Solution:
        # Store each integer count in a hashmap, and then store it to a 2-dimensional array with row length = len(nums) + 1. Example: nums = [1,1,1,2,2,3]
        # would have hashmap = {1:3, 2:2, 3:1} and 2-d array = [[], [3], [2], [1], [], [], []]
        # Then we could iterate the 2-d array from the last row and get top k frequent element 
        # Time complexity would be O(n + k) where n is to iterate through the nums to add each num to hashmap and to add them to 2-d array, then k is to get the top k frequent elements from the 2-d array  

        countDict = defaultdict(int)
        freqArr = [[] for i in range(len(nums) + 1)]

        # Add the freq of each number to hashmap
        for num in nums:
            countDict[num] += 1
        
        print(countDict)
        
        # Add to the 2-d array
        for num, freq in countDict.items():
            freqArr[freq].append(num)
        
        print(freqArr)

        # Get the top k frequent element from the last
        res = []
        for i in range(len(freqArr) - 1, -1, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        return res
