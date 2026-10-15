import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.count = 0 # helper for tweets in order
        self.tweetMap = defaultdict(list) # userID : list of [count, tweetId]
        self.followMap = defaultdict(set) # userID : set of followeeIDs

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId) # have to also get their own

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: # make sure followee exists
                lastTweetIdx = len(self.tweetMap[followeeId]) - 1  # get idx of last tweet
                count, tweetId = self.tweetMap[followeeId][lastTweetIdx]
                minHeap.append([count, tweetId, followeeId, lastTweetIdx - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, lastTweetIdx = heapq.heappop(minHeap)
            res.append(tweetId)

            if lastTweetIdx >= 0: # if we still have more tweets
                count, tweetId = self.tweetMap[followeeId][lastTweetIdx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, lastTweetIdx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
