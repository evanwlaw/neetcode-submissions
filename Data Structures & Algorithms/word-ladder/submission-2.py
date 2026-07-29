from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        output = 1
        # create adjacency map - wildcards : word
        adj = defaultdict(list)
        wordList.append(beginWord) # append starting word to create adj list from all words

        for word in wordList:
            for c in range(len(word)):
                adj[word[:c] + "*" + word[c + 1:]].append(word)

        # bfs
        queue = deque([beginWord])
        visited = {beginWord}

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                # base case
                if word == endWord:
                    return output

                # go through all patterns of word
                for c in range(len(word)):
                    root = word[:c] + "*" + word[c + 1:]

                    for neiWord in adj[root]:
                        if neiWord not in visited:
                            queue.append(neiWord)
                            visited.add(neiWord)
            output += 1
        return 0