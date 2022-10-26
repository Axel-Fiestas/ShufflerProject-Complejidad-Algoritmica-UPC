class Song:
    def __init__(self, name, artist,popularity,genres):
        self.name = name
        self.artist=artist
        self.popularity=popularity
        self.genres=genres


class Graphs:

    def __init__(self, size):
        self.size=size #Number of Vertices
        self.graph=[]
        self.vertex=[]

    def add_node(self,v):
        if v in self.vertex:
            pass
        else:
            self.vertex.append(v)
            temp=[]
            for i in range(self.size):
                temp.append(0)
            self.graph.append(temp)

    def add_edges(self,v1,v2,e):
        i1=self.vertex.index(v1)
        i2=self.vertex.index(v2)
        self.graph[i1][i2]=e

    def rem_edges(self,v1,v2):
        i1=self.vertex.index(v1)
        i2=self.vertex.index(v2)
        self.graph[i1][i2]=0

    def printGr(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.vertex[i],"->",self.vertex[j]," edge weight: ",self.graph[i][j])

