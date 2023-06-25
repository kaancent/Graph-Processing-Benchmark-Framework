from algorithms import *
from graph import *
from utilities import *

#file = "facebook_undirected.txt"   #[Nodes 4,039 - Edges 88,234]  
file = "CollegeMsg.txt"             #[Nodes: 1,899 - Edges: 20,296]
#file = "wikiTalk_directed.txt"     #[Nodes 1,140,149 - Edges 3,309,592]
#file = "roadNet-TX.txt"            #[Nodes 1,379,917 - Edges 1,921,660]

adjListGraph, edgeListGraph, adjMatrixGraph, firstVertex, roundedAdjList, roundedEdgeList, roundedAdjMatrix, numVertices = fileToGraph(file, True)


print("\n----------DFS-EdgeCentric(adjList,edgeList,adjMatrix)----------")
dfsEdgeCentric(adjListGraph, firstVertex)   
print("----------------------------------------------------------------")
dfsEdgeCentric(edgeListGraph, firstVertex)
print("----------------------------------------------------------------")
dfsEdgeCentric(adjMatrixGraph, firstVertex)
    

print("\n----------DFS-VertexCentric(adjList,edgeList,adjMatrix)--------")
dfsVertexCentric(adjListGraph, firstVertex)   
print("----------------------------------------------------------------")
dfsVertexCentric(edgeListGraph, firstVertex)
print("----------------------------------------------------------------")
dfsVertexCentric(adjMatrixGraph, firstVertex)



print("\n---------------BFS-EdgeCentric(adjList,edgeList,adjMatrix)-----")
bfsEdgeCentric(adjListGraph, firstVertex)
print("----------------------------------------------------------------")
bfsEdgeCentric(edgeListGraph, firstVertex)
print("----------------------------------------------------------------")
bfsEdgeCentric(adjMatrixGraph, firstVertex)


print("\n-------------BFS-VertexCentric(adjList,edgeList,adjMatrix)-----")
bfsVertexCentric(adjListGraph, firstVertex)
print("----------------------------------------------------------------")
bfsVertexCentric(edgeListGraph, firstVertex)
print("----------------------------------------------------------------")
bfsVertexCentric(adjMatrixGraph, firstVertex)
    


print("\n--------------PR-VertexCentric(adjList,edgeList,adjMatrix)-----")
pageRankVertexCentric(adjListGraph)
print("----------------------------------------------------------------")
pageRankVertexCentric(edgeListGraph)  
print("----------------------------------------------------------------")
pageRankVertexCentric(adjMatrixGraph)    


print("\n--------------PR-EdgeCentric(adjList,edgeList,adjMatrix)-----")
pageRankEdgeCentric(adjListGraph) 
print("----------------------------------------------------------------")
pageRankEdgeCentric(edgeListGraph) 
print("----------------------------------------------------------------")
pageRankEdgeCentric(adjMatrixGraph)  