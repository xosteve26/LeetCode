class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.posts[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = []
        tweets = self.posts[userId][:]
        for followee in self.followers[userId]:
            tweets+=self.posts[followee]

        heapq.heapify(tweets)
        t=10
        while tweets and t:
            recentTweets.append(heapq.heappop(tweets)[1])
            t-=1

        return recentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)