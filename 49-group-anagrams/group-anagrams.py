from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Bruteforce:
        # Create a hashmap that will store sorted character in words and then append the value of each word that are anagram to that. For example we would have hashmap = {"aet": ["eat", "tea", "ate"], ...}. Time complexity would be O(m.nlogn) where m is the length of strs and nlogn is to sort the character in the word.

        # Solution 2:
        # Create a hashmap that will store frozenset (a hashable version of set) as the key and the str in strs as the value. 
        # Loop through the strs, then create each word into a set, then insert it into the hasmap with set as the key and the word as the value in an array, so we could append it later if we have the same anagram.
        # Time Complexity would be O(m.n) where n is the strs length and m is to change the words into frozenset.
        # BUT THIS WOULD FAIL BECAUSE WE DON'T KEEP TRACK OF HOW MUCH EACH CHARACTER PRESENT, LIKE IT WOULD FAIL IF strs = ["aab", "abb"] WHERE IT WILL ASSUME BOTH ARE ANAGRAM BCS THEY BOTH HAVE "a" AND "b"

        # Better Solution:
        # Rather than using frozen set as the key, we could use a list with length of 26 where each of the value is 0, then when we iterate through the strs, we would set the list with the count of occurences of each character.
        # For example, "acea" will have the list as "20101000000000000000000000"

        setAnagram = defaultdict(list)  # so we could just append it without initializing it as array again

        for string in strs:
            characterCount = [0] * 26
            for character in string:
                characterIndex = ord(character) - ord("a")      # if the char is a, it will be 0, if the char is z, it will be 25
                characterCount[characterIndex] += 1 
                
            # Set the characterCount to be a tuple first to make it immutable, hence hashable to be a key
            characterCountTuple = tuple(characterCount)
            setAnagram[characterCountTuple].append(string)
            
        res = []
        for value in setAnagram.values():
            res.append(value)
        
        return res