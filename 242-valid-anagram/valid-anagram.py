from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Bruteforce:
        # Sort s and t, and then just compare it directly. Time complexity would be O(n log n) because we need to sort it

        # Better Solution: 
        # Store each character occurences in string s into a hashset, then iterate through the string t and reduce the occurences of character in the hashset. And then check if each of the value in the hashset is 0 then it will be true. Time Complexity would be O(s + t) with Space complexity O(1) since we assume alphabet is 26 letter linear

        characterOccurence = defaultdict(int)

        for c in s:
            characterOccurence[c] += 1
        
        for c in t:
            characterOccurence[c] -= 1
        
        for v in characterOccurence.values():
            if v != 0:
                return False
            
        return True

        