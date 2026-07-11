from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbor = defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            queue.append(neighborWord)
            res += 1

        return 0
