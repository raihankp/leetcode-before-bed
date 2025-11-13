class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Bruteforce (hm not really)
        # Convert first by looping and the string and checking whether it's a alphanumeric, if it's alphabet then make it lowercase.
        # Then, do a loop one more time with 2 pointer, one in the first character and one in the last character
        # check if they are the same and check until the second pointer is less than first pointer, then return the result
        # Time complexity is O(n) which is good but the space complexity is O(n) which we could enhance

        # Better solution:
        # Like the bruteforce solution but instead of converting first, we could directly loop through the original, and check first if the character is alphanum or not, if not then just skip it
        
        # Use two pointer
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            if not s[leftPointer].isalnum():
                leftPointer += 1
            elif not s[rightPointer].isalnum():
                rightPointer -= 1
            else:
                if str(s[leftPointer]).lower() != str(s[rightPointer]).lower():
                    return False

                leftPointer += 1
                rightPointer -= 1
                
        return True
        