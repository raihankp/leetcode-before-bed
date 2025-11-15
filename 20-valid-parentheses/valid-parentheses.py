class Solution:
    def isValid(self, s: str) -> bool:
        # Better Solution:
        # Create a stack and a hashmap with the key as the closing tag and the value as the opening tag
        # Append to the stack if the character is the opening of paranthesis
        # If it's the closing, pop the stack from the last added (LIFO/Last in First Out)
        # Check if it's a pair in the hashmap, if yes then continue to check the next character
        # If not a pair, then return False
        # Time complexity O(n)

        hashMapParantheses = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            # This means that the character is the closing tag
            if c in hashMapParantheses and stack:
                poppedCharacter = stack.pop()
                if poppedCharacter != hashMapParantheses[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
