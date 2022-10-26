class Twitter:

    def __init__(self):
        self.i = 0
        self.posts = {}
        self.follo = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.i -= 1
        self.posts[userId].append((self.i, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        if userId in self.posts:
            for post in self.posts[userId]:
                result.append(post)

        if userId in self.follo:
            for followee in self.follo[userId]:
                if followee in self.posts:
                    for pos in self.posts[followee]:
                        result.append(pos)

        final = []
        heapq.heapify(result)
        c = 1
        while result and c <= 10:
            item = heapq.heappop(result)
            final.append(item[1])
            c += 1

        return final

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follo:
            self.follo[followerId] = set()
        self.follo[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follo:
            self.follo[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
