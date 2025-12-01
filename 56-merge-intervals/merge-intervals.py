class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        solutionArrays = [intervals[0]]

        for i in range(1, len(intervals)):
            foundOverlap = False
            for j in range(len(solutionArrays)):
                # if solutionArrays[j][0] > intervals[i][1] and solutionArrays[j][1] < intervals[i][0]:
                #     solutionArrays[j][0] = min(solutionArrays[j][0], intervals[i][0])
                #     solutionArrays[j][1] = max(solutionArrays[j][1], intervals[i][1])
                #     continue
                if solutionArrays[j][0] <= intervals[i][1] and solutionArrays[j][1] >= intervals[i][0]: 
                    newSolution = [0,0]
                    newSolution[0] = min(solutionArrays[j][0], intervals[i][0])
                    newSolution[1] = max(solutionArrays[j][1], intervals[i][1])
                    # solutionArrays[j][0] = min(solutionArrays[j][0], intervals[i][0])
                    # solutionArrays[j][1] = max(solutionArrays[j][1], intervals[i][1])
                    if newSolution not in solutionArrays:
                        solutionArrays[j] = newSolution

                    foundOverlap = True
                    continue
                # elif solutionArrays[j][0] < intervals[i][1] and solutionArrays
            if foundOverlap == False:
                solutionArrays.append(intervals[i])
            
        return solutionArrays

        