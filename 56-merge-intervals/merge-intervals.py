class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        solutionArrays = [intervals[0]]

        for i in range(1, len(intervals)):
            # Overlap
            if solutionArrays[-1][1] >= intervals[i][0]:
                solutionArrays[-1][1] = max(solutionArrays[-1][1], intervals[i][1])
            else:
                solutionArrays.append(intervals[i])

        return solutionArrays

        