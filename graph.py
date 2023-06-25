from queue import Queue
from algorithms import *
from graph import *


class GraphAdjList:            
  #adjacency list representation 
            
    def __init__(self, numVertices):
        #Initialize a list for each vertex
        self.numVertices = numVertices 
        self.adjList = []
        for _ in range(numVertices):
            self.adjList.append([])

    def addEdge(self, src, dest, isDirected=False):
        #Add an edge between source and destination
        self.adjList[src].append(dest)
        
        #if undirected, add an edge back to source     
        if not isDirected:
            self.adjList[dest].append(src)

    def getNeighbors(self, vertex):
        #Return the list of neighbors
        return self.adjList[vertex]
    
    def getEdges(self):
        edges = []
        for v in range(self.numVertices):
            for n in self.getNeighbors(v):
                edges.append((v, n))  
        return edges

    
    def sortNeighbors(self, method=""): #choose a sorting method
        if method == "":    #unordered list
            return
        elif method == "timSort":
            for vertex_neighbors in self.adjList:
                vertex_neighbors.sort()

    def display(self):
        for vertex, neighbors in enumerate(self.adjList):
            print(str(vertex) + ": " + str(neighbors))


class GraphEdgeList:
    #edge list representation
    
    def __init__(self, numVertices):    
        self.edgeList = []  
        self.numVertices = numVertices  

    
    def addEdge(self, src, dest, isDirected=False):
        #Add an edge between source and destination
        self.edgeList.append((src, dest))       
        if not isDirected: #undirected graph 
            self.edgeList.append((dest, src))

    def getNeighbors(self, vertex):
        #Return the list of neighbors
        neighbors = []
        for i in self.edgeList:
            if i[0] == vertex:
                neighbors.append(i[1])
        return neighbors
    
    def getEdges(self):
        # Return the edge list
        return self.edgeList
            
    def display(self):
        for edge in self.edgeList:
            print(str(edge[0]) + " -- " + str(edge[1]))

            
            
class GraphAdjMatrix:
    # Adjacency matrix representation
    def __init__(self, numVertices):
        self.adjMatrix = [[0]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices 

    def addEdge(self, src, dest, isDirected=False):
        # Add an edge between source and destination
        self.adjMatrix[src][dest] = 1
        # undirected graph    
        if not isDirected:
            self.adjMatrix[dest][src] = 1

    def getNeighbors(self, vertex):
        #Return the list of neighbors
        neighbors = []
        for i, x in enumerate(self.adjMatrix[vertex]):
            if x == 1:
                neighbors.append(i)
        return neighbors
 
    def getEdges(self):
        # Return a list of all edges
        edges = []
        for v in range(self.numVertices):
            for n in self.getNeighbors(v):
                edges.append((v, n))  
        return edges

    def display(self):
        for vertex, neighbors in enumerate(self.adjMatrix):
            print(str(vertex) + ": " + str(neighbors))

