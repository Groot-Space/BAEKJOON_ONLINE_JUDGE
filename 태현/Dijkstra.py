class Dijkstra:
    def __init__(self,nodes):
        self.g = {}
        self.dist = {}
        for node in nodes:
            self.g[node] = {}
            self.dist[node] = [float("inf"), "none"]

    def setEdge(self,a,b,w,bidirection=True):
        self.g[a][b] = w
        if bidirection == True: self.g[b][a] = w

    def getPath(self,start,end):
        dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        visits = set()
        curNode = start
        self.dist[curNode][0] = 0
        while True:
            visits.add(curNode)
            nodes.remove(curNode)
            neighbors = self.g[curNode]

            for node in neighbors:
                if min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node]) < self.dist[node][0]:
                    self.dist[node][0] = min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node])
                    self.dist[node][1] = curNode

            if len(nodes) > 0:
                curNode = min(dictfilt(self.dist, nodes), key=dictfilt(self.dist, nodes).get)
            else:
                break

        path = [end]
        dist = []

        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]

        return path[::-1], dist[::-1]

graph = [['start','A', 6],['start','B', 2], ['A', 'finish', 1], ['B', 'finish', 5], ['B', 'A', 3]]
nodes = set()
for edge in graph:
    nodes.add(edge[0])
    nodes.add(edge[1])

dj = Dijkstra(nodes)
for g in graph:
    dj.setEdge(g[0],g[1],g[2])

print(dj.getPath("start","finish"))