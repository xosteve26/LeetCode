class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union Find By RANK

        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)

        def find(node):
            p = parent[node]

            while p != parent[p]:
                p = parent[p]

            return p

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)

            if p1 == p2:
                return False
            elif(rank[p1] > rank[p2]):
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
