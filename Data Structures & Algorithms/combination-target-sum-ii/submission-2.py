class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        sort the input -> doesnt change our overall time complexity. and we can skip n that we've seen already

        1   2   2   4   5   6   9


        """

        candidates.sort()
        output = []
        currPath = []

        def backtrack(i, currSum):
            if currSum > target:
                return
            if currSum == target:
                output.append(currPath[:])
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                currPath.append(candidates[j])
                backtrack(j + 1, currSum + candidates[j])
                currPath.pop()
            
         
            return
        
        backtrack(0, 0)
        return output