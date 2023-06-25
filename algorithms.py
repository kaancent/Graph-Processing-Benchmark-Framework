import time
from queue import Queue


def bfsVertexCentric(graph, startVertex):
    """
    Parameters
    ----------
    graph: The graph to perform BFS(vertex-centric) on
    startVertex: Starting vertex of BFS
    """
    startTime = time.perf_counter()
    #To track visited vertices
    visited = [False] * graph.numVertices
    
    #To store vertices to be visited
    vertexQueue = Queue()
    vertexQueue.put(startVertex)
    visited[startVertex] = True

    while not vertexQueue.empty():
        vertex = vertexQueue.get()
        #access the vertices using the function from graph representation class
        neighbors = graph.getNeighbors(vertex)
        for i in neighbors:
            # If a neighbor is not been visited, add to the queue and mark visited
            if not visited[i]:
                vertexQueue.put(i)
                visited[i] = True
                
    endTime = time.perf_counter()
    roundedTime = round(endTime - startTime,5)
    print("BFS(vertex-centric) runtime:" + str(roundedTime) +" seconds")
    
    
    
  
def bfsEdgeCentric(graph, startVertex):                         
    """
    Parameters
    ----------
    graph: The graph to perform BFS(edge-centric) on
    startVertex: Starting vertex of BFS
    """
    startTime = time.perf_counter()
    #To track visited vertices
    visited = [False] * graph.numVertices
    
    #To store edges to be visited
    edgeQueue = Queue()
    
    #Get neighbors of the starting vertex and enque the edges
    neighbors = graph.getNeighbors(startVertex)
    for neighbor in neighbors:
        edgeQueue.put((startVertex, neighbor))

    visited[startVertex] = True

    while not edgeQueue.empty():
        #Get the next edge to be explored
        edge = edgeQueue.get()
        
        parent = edge[0]
        neighbor = edge[1]
        
        if not visited[neighbor]:
            #print(edge)
            neighborsOfNeighbor = graph.getNeighbors(neighbor) #sorted?
            for nextNeighbor in neighborsOfNeighbor:
                
                #Exclude the parent vertex
                if nextNeighbor != parent:
                    edgeQueue.put((neighbor, nextNeighbor))

            visited[neighbor] = True

    endTime = time.perf_counter()
    roundedTime = round(endTime - startTime,5)
    print("BFS(edge-centric) runtime:" + str(roundedTime) +" seconds")
    
    


def dfsVertexCentric(graph, startVertex):
    """
    Parameters
    ----------
    graph: The graph to perform DFS(vertex-centric) on
    startVertex: Starting vertex of DFS """
    startTime = time.perf_counter()
    
    #init list for visited vertices
    visited = [False] * graph.numVertices
    
    #init stack for storing vertices to visit
    vertexStack = []

    vertexStack.append(startVertex)
    visited[startVertex] = True

    while vertexStack:
        
        vertex = vertexStack.pop()
        # print(vertex)
        
        #Get the neighbors of current vertex
        neighbors = graph.getNeighbors(vertex)
        
        #Visit the neighbors in reverse order
        for i in neighbors:
            #print(vertex)
            if not visited[i]:
                # Add the neighbor to the stack and mark it as visited

                vertexStack.append(i)
                visited[i] = True

    endTime = time.perf_counter()
    roundedTime = round(endTime - startTime, 5)
    print("DFS (vertex-centric) runtime: " + str(roundedTime) + " seconds")


def dfsEdgeCentric(graph, startVertex):
    """
    Parameters
    ----------
    graph: The graph to perform DFS(vertex-centric) on
    startVertex: Starting vertex of DFS """
    
    startTime = time.perf_counter()
    visited = [False] * graph.numVertices
    
    # init stack to keep track of edges
    edgeStack = []
    
    neighbors = graph.getNeighbors(startVertex)
    # Add all edges from the start vertex to the stack
    for neighbor in neighbors:
        edgeStack.append((startVertex, neighbor))

    visited[startVertex] = True

    while edgeStack:
        edge = edgeStack.pop()
        #print(edge)
        #Get parent vertex and its neighbor from the edge
        parent = edge[0]
        neighbor = edge[1]
        
        if not visited[neighbor]:
            # print(edge)
            neighborsOfNeighbor = graph.getNeighbors(neighbor)
            
            for nextNeighbor in (neighborsOfNeighbor):
                
                # Avoid going backwards
                if nextNeighbor != parent:
                    edgeStack.append((neighbor, nextNeighbor))

            visited[neighbor] = True

    endTime = time.perf_counter()
    roundedTime = round(endTime - startTime, 5)
    print("DFS (edge-centric) runtime: " + str(roundedTime) + " seconds")

    
    
def pageRankVertexCentric(graph, alpha=0.85, tol=1e-6, iterations=100):
    """
     Parameters
    -----------
    graph: The graph on which to compute the PR
    alpha: Damping parameter for PR
    tol: Error tolerance value
    iterations: max number of iterations"""

    # Measure start time for execution profiling
    startTime = time.perf_counter()
   

    # Number of vertices in the graph
    vertexCount = graph.numVertices

    # Initial PageRank value for each vertex
    pageRanks = [1.0 / vertexCount] * vertexCount  

    for _ in range(iterations):
        # Initialize contributions to zero for the new iteration
        newContributions = [0.0] * vertexCount  

        # List of dangling nodes, i.e., nodes without outgoing edges
        danglingNodes = []

        # Compute contributions from each vertex
        for vertex in range(vertexCount):
            neighbors = graph.getNeighbors(vertex)
            if not neighbors:
                danglingNodes.append(vertex)
            else:
                contribution = pageRanks[vertex] / len(neighbors)
                for neighbor in neighbors:
                    newContributions[neighbor] += contribution

        # Compute PageRank values
        dangling= sum(pageRanks[node] for node in danglingNodes)
        for i in range(vertexCount):
            pageRanks[i] = alpha * (newContributions[i] + dangling / vertexCount) + (1.0 - alpha) / vertexCount 
            
        diff = sum(abs(newContributions[i] - pageRanks[i]) for i in range(vertexCount))
        if diff < tol:
            break


    endTime = time.perf_counter()
    roundedTime = round(endTime - startTime,5)
    print("PageRank (Vertex-centric) runtime:" + str(roundedTime)  +"seconds")
    return pageRanks



def pageRankEdgeCentric(graph, alpha=0.85, tol=1e-6, iterations=100):
    """
    Parameters
    ----------
    graph: The graph on which to compute the PR
    alpha: Damping factor
    tol: Error tolerance value
    iterations: Max number of iterations
    
    """
    startTime = time.perf_counter()
    vertexCount = graph.numVertices
 
    # Initialize pageRank and contribution for each vertex
    contributions = [0] * vertexCount
    pageRanks = [1 / vertexCount] * vertexCount
    
    # Calculate outdegree for each vertex
    outDegrees = [len(graph.getNeighbors(v)) for v in range(vertexCount)]
    edgeList = graph.getEdges()

    for _ in range(iterations):
        # Reset contributions for each iteration
        contributions = [0] * vertexCount

        # Update contributions
        for edge in edgeList:
            src, dest = edge
            if outDegrees[src] > 0:
                contributions[dest] += alpha * pageRanks[src] / outDegrees[src]

        danglingSum = sum(pageRanks[i] for i in range(vertexCount) if outDegrees[i] == 0)
                
        newPR = []  
        for i in range(vertexCount):  
            res = contributions[i] + alpha * (danglingSum / vertexCount) + (1 - alpha) / vertexCount
            newPR.append(res)  
        
        if sum(abs(newPR[i] - pageRanks[i]) for i in range(vertexCount)) < tol:
            break
        pageRanks = newPR

    endTime = time.perf_counter()
    roundedTime = round(endTime - startTime, 5)
    print("PageRank (Edge-Centric) runtime: " + str(roundedTime) + " seconds")
    return pageRanks







