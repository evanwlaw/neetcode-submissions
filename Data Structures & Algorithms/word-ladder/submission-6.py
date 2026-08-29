class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        edge case 
        - endWord not in wordlist -> 0
        - if beginWord == endWord -> 1

        change cat into sag
        Input: 
            beginWord = "cat", 
            endWord = "sag", 
            wordList = ["bat","bag","sag","dag","dot"]
        Output: 4 "cat" -> "bat" -> "bag" -> "sag"

        Looks like a graph problem -> get to target in min path


        From cat to bat:
            we know that they have 2 letters in common.
            we dont know how to "travese" from one word ot the next
       
        From bat to bag:
            we know that they have 2 letters in common.
            we dont know how to "travese" from one word ot the next 

        From bag to sag:
            we know that they have 2 letters in common.
            we dont know how to "travese" from one word ot the next

        Edges are the wildcard plus char they have in common.
        Adjacency map where key is words and values are the edge/chars with wildcard

        Edges that were traversed in curr example:
        cat : *at, c*t, ca*
        bat : *at, b*t, ba*
        sag : *ag, s*g, sa*

        *at : cat, bat,
        ba* : bat, bag
        *ag : bag, sag, dag

        """

        if endWord not in wordList:
            return 0

        output = 1
        # build adjacency list
        
        # add beginWord to wordlist first
        wordList.append(beginWord)
        adj_list = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                # key = begin + * + end
                adj_list[w[:i] + "*" + w[i+1:]].append(w)
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        # bfs
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return output
                
                # iterate through neighbors
                for i in range(len(word)):
                    for nei in adj_list[word[:i] + "*" + word[i+1:]]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

            output += 1
        return 0


        