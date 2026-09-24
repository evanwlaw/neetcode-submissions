class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        Input: words = ["hrn","hrf","er","enn","rfnn"]
        Output: "hernf"

        hrn
        hrf
        er
        enn
        rfnn

        str hrn and hrf -> same prefix hr. n before f
        str er and enn -> same prefix e. r before n
        h is before e
        e before r

        r -> n -> f
        h -> e
        e -> r

        toplogical sort is  h -> e -> r -> n -> f

        so p much return the topological sorted str

        1. build adjList and indegrees
            adj map -> char : set()
            indegrees -> 
        2. bfs -> process from indegree 0 letters
        """

        adj_map = {char : set() for w in words for char in w}
        # h: set(), r: set(), n: set(),....

        indegrees = {char : 0 for char in adj_map}
        # h: 0, r: 0, n: 0,...

        # populate adj and indegrees between two words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # invalid if apes is before ape. the prefix is the same but the s is lexigraphically larger
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # iterate through both words of equal len    
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_map[w1[j]]:
                        adj_map[w1[j]].add(w2[j])
                        indegrees[w2[j]] += 1
                    break
        # add 0 degree to queue
        queue = deque()

        for char in indegrees:
            if indegrees[char] == 0:
                queue.append(char)
        
        output = []
        while queue:
            char = queue.popleft()
            output.append(char)

            for nei in adj_map[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        if len(output) != len(indegrees):
            return ""
        return "".join(output)


        