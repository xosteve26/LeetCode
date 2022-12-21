class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * (len(graph))

        def helper(start):
            queue = deque()
            queue.append(start)
            color[start] = 1

            while queue:
                LENGTH = len(queue)
                for _ in range(LENGTH):
                    node = queue.pop()

                    for neighbour in graph[node]:
                        if color[node] == color[neighbour]:
                            return False
                        if color[neighbour] == -1:
                            color[neighbour] = 1-color[node]
                            queue.append(neighbour)
            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not helper(i):
                    return False
        return True
