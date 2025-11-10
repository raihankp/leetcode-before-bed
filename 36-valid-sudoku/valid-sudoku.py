from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # There is no bruteforce, i think this is the best solution
        # Do a nested loop
        # Inside the inner loop, there will be 4 condition
        # Check if the digit is a dot, then skip
        # Check if the digit is already in rowSetHashmap
        # Check if the digit is already in columnSetHashmap
        # Check if the digit is already in row // 3 and column // 3 -> This will make row/column 0-2 in subbox 0, row/column 3-5 in subbox 1, and row/column 6-8 in subbox 2
        # If one of the condition is met, return False
        # Time complexity would be O(n^2) bcs we need to do nested loop
        # Space complexity would be O(3n^2) or equals to O(n^2) since we need to store 3 hashmap where each hashmap would have 9 set and each set can contain up to 9 digits, so basically 9^2 or n^2

        rowSetHashmap = defaultdict(set)
        columnSetHashmap = defaultdict(set)
        subboxSetHashmap = defaultdict(set)

        # row
        for i in range(len(board)):
            # column
            for j in range(len(board[i])):
                digit = board[i][j]
                subbox = str(i // 3) + "x" + str(j // 3)
                
                # Condition 1
                if digit == ".":
                    continue
                
                # Condition 2 or 3 or 4
                if digit in rowSetHashmap[i] or digit in columnSetHashmap[j] or digit in subboxSetHashmap[subbox]:
                    return False
                else:
                    rowSetHashmap[i].add(digit)
                    columnSetHashmap[j].add(digit)
                    subboxSetHashmap[subbox].add(digit)

                print("digit:", digit)
                print("row:", i, "column:", j)
                print("subbox:", subbox)
                print()

        return True        
        