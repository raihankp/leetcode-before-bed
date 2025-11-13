class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert first by looping and the string and checking whether it's a alphanumeric, if it's alphabet then make it lowercase.
        # Then, do a loop one more time with 2 pointer, one in the first character and one in the last character
        # check if they are the same and check until the second pointer is less than first pointer, then return the result
        
        converted = ""

        for c in s:
            if c.isdigit():
                converted += c
            elif c.isalpha():
                converted += c.lower()
        
        # Use two pointer
        leftPointer = 0
        rightPointer = len(converted) - 1

        while leftPointer < rightPointer:
            if converted[leftPointer] != converted[rightPointer]:
                return False
            leftPointer += 1
            rightPointer -= 1
                
        return True
        