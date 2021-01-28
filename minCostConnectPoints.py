def distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        ls = [i for i in range(n)]

        eage = []
        for i in range(n-1):
            for j in range(i+1, n):
                eage.append([i, j, distance(points[i], points[j])])

        eage.sort(key=lambda x: x[2])

        def find(x):
            print(ls)
            if ls[x] == x:
                return x
            ls[x]=find(ls[x])
            return ls[x]
        def merge(a,b):
            a = find(a)
            b = find(b)
            print(ls)
            ls[b]=a

        res = 0
        for e in eage:
            e1 = find(e[0])
            e2 = find(e[1])
            if e1!=e2:
                merge(e1,e2)
                res += e[2]
        return res

so = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
so.minCostConnectPoints(points)