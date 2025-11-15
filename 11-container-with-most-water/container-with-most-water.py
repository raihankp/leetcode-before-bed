class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Bruteforce:
        # Store a maxArea as an integer
        # Do a nested loop where it will calculate the area using formula min(height[i], height[j]) times (j-1) where min() is to find the height the water could stay without overload and (j-1) is the width or length. And then compare with the maxArea, replace it if it's greater than the maxArea
        # Time complexity would be O(n^2)

        # Better Solution:
        # Use two pointer with leftPointer in index 0 and rightPointer in index length-1
        # Calculate the area with formula min(height[i], height[j]) times (j-1)
        # Move the pointer if it's the smaller digit: Move leftPointer by one if the digit in leftPointer is less than rightPointer and vice versa.
        # Why we move the pointer for the smaller digit?
        # The idea is that, if we have one of the height is small and the other pair height is like 1 million, the area will still be the same (which is the small * width, because the water will not overflow if the height is the small one)
        # Which means that, we basically have 2 option:
        # 1. Move the pointer if the height is smaller: This will make 2 possible scenario, where MAYBE we could get greater AREA if the next height is bigger, or MAYBE we could get smaller area if the next height is the same/smaller
        # 2. Move the pointer if the height is greater: This will make ONLY 1 possible scenario, where we would get the SAME AREA, even though the next height is much bigger, bcs the water will overload no matter how big the next height is.
        # THEREFORE, we move the pointer that has the smaller height
        # Time complexity would be O(n) CRAZYYY

        maxArea = -1
        leftPointer = 0
        rightPointer = len(height) - 1

        while leftPointer < rightPointer:
            currArea = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
            maxArea = max(maxArea, currArea)

            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            elif height[leftPointer] > height[rightPointer]:
                rightPointer -= 1
            else:
                # height is the same
                if height[leftPointer + 1] < height[rightPointer - 1]:
                    leftPointer += 1
                else:
                    rightPointer -= 1

        return maxArea