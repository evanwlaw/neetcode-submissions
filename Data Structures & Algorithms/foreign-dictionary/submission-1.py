from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        1. intialize adj map and indegrees
        
        2. build adj map and indegrees
            - base case -> return "" if out of order
        3. put 0 indegree to queue

        4. BFS process indegrees

        5. Check that output is same len as indegrees (letters we have)


        hrn
        hrf
        er
        enn
        rfnn
        
        h -> e - r
        r -> n
        n -> f
        can see that there is a toplogical sort of h -> e -> r -> n -> f
        """

        adjList = {char : set() for w in words for char in w} # char : neighbors
        indegrees = {char : 0 for char in adjList} # char : indegrees

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return "" # invalid -> apes is before ape
            
            for j in range(minLen):
                if w1[j] != w2[j]: # only link if not the same char
                    if w2[j] not in adjList[w1[j]]:
                        adjList[w1[j]].add(w2[j])
                        indegrees[w2[j]] += 1
                    break
        # enqueue indegrees of 0
        queue = deque()
        for char in indegrees:
            if indegrees[char] == 0:
                queue.append(char)
        output = []

        while queue:
            char = queue.popleft()
            output.append(char
            )
            for nei in adjList[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)    
        if len(output) != len(indegrees):
            return ""
        return "".join(output)