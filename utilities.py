import time
from algorithms import *
from graph import *
from utilities import *


def printTopRanks(pageRanks, top=10):
    """
    Prints the top 10 vertices with the highest page ranks.
    """
    # A list of tuples (vertex, rank) 
    vertexPageRanks = list(enumerate(pageRanks))
    # Sort the list 
    vertexPageRanks.sort(key=lambda x: x[1], reverse=True)

    print("BEST RANKS:")
    for i in range(min(top, len(vertexPageRanks))):
        print("Vertex: " + str(vertexPageRanks[i][0]) + ", PageRank: " + str(vertexPageRanks[i][1]))



def fileToGraph(filePath, isDirected=False):
    #Converts a txt file into a graph
    
    firstVertex = None
    vertices = set()
    edges = []
    
    with open(filePath, 'r') as file:
        for line in file:
            if line:
                parts = line.split(',') 
                if len(parts) == 1: 
                    parts = line.split()
                vertex1 = int(parts[0])
                vertex2 = int(parts[1])
                
                vertices.add(vertex1)
                vertices.add(vertex2)
                edges.append((vertex1, vertex2))

                if firstVertex is None:
                    firstVertex = vertex1

    numVertices = max(vertices) + 1

    print("--------------------------------------------------------")

    print("numVertices =" + str(numVertices))
    print("filePath =" + str(filePath))
    print("isDirected =" + str(isDirected))
    
    #create AdjListGraphs with counter
    startAdjListCounter = time.perf_counter()
    adjListGraph = GraphAdjList(numVertices)
    
    for edge in edges:
        vertex1, vertex2 = edge
        adjListGraph.addEdge(vertex1, vertex2, isDirected)
        
    #change sorting here
    adjListGraph.sortNeighbors(method="") 
    endAdjListCounter = time.perf_counter()  
    
    #create EdgeListGraphs with counter
    startEdgeListCounter = time.perf_counter()
    edgeListGraph = GraphEdgeList(numVertices)
    
    for edge in edges:
        vertex1, vertex2 = edge
        edgeListGraph.addEdge(vertex1, vertex2, isDirected)
    
    endEdgeListCounter = time.perf_counter()
        
    #create Adjacency Matrix with counter  
    startAdjMatrixCounter = time.perf_counter()
    adjMatrixGraph = GraphAdjMatrix(numVertices)
    for edge in edges:
        vertex1, vertex2 = edge
        adjMatrixGraph.addEdge(vertex1, vertex2, isDirected)
    endAdjMatrixCounter = time.perf_counter()
    
    roundedAdjList = round(endAdjListCounter - startAdjListCounter,5)
    roundedEdgeList = round(endEdgeListCounter - startEdgeListCounter,5)
    roundedAdjMatrix = round(endAdjMatrixCounter - startAdjMatrixCounter,5)

    print("----------------------------------------------------------------")
    print("Adjacency list loading time: " + str(roundedAdjList) + " seconds")
    print("Edge list loading time: " + str(roundedEdgeList) + " seconds")
    print("Adjacency matrix loading time: " + str(roundedAdjMatrix) + " seconds")
    print("----------------------------------------------------------------")
    return adjListGraph, edgeListGraph, adjMatrixGraph, firstVertex, roundedAdjList, roundedEdgeList, roundedAdjMatrix, numVertices



