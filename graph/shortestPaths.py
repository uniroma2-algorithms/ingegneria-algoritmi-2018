from priorityQueue.PQbinaryHeap import PQbinaryHeap as PriorityQueue
from graph.Graph import Edge
from graph.GraphHelper import GraphHelper
from dictionary.trees.treeArrayList import TALNode as TreeNode
from dictionary.trees.treeArrayList import TreeArrayList as Tree
from graph.Graph_IncidenceList import GraphIncidenceList as Graph


INFINITE = float("inf")


def BellmanFord(graph, root):
    """
    Bellman-Ford's algorithm for the computation of the shortest path.
    The algorithm assumes a graph implemented as incidence list.
    ---
    Time Complexity: O(|V|*|E|)
    Memory Complexity: O()

    :param graph: the graph.
    :param root: the root node to start from.
    :return: the list of distances.
    """
    nodes = len(graph.nodes)

    # initialize distances
    dist = nodes * [INFINITE]
    dist[root] = 0

    # apply the relaxation step |V| times
    for i in range(nodes):
        for j in range(len(graph.inc)):
            curr = graph.inc[j].getFirstRecord()
            while curr is not None:
                edge = curr.elem
                tail = edge.tail
                head = edge.head
                weight = edge.weight
                # relaxation step
                if dist[tail] + weight < dist[head]:
                    dist[head] = dist[tail] + weight
                curr = curr.next

    return dist


def FloydWarshall(graph):
    """
    Floyd-Warshall's algorithm for the computation of the shortest path.
    The algorithm assumes a graph implemented as incidence list.
    ---
    Time Complexity: O(|V|^3)
    Memory Complexity: O()

    :param graph: the graph.
    :return: the list of distances.
    """
    nodes = len(graph.nodes)

    # initialize distances:
    # dist[i,j]=inf, if (i,j) not in E
    # dist[i,i]=0,
    # dist[i,j]=w(i,j), if (i,j) in E
    dist = [[INFINITE] * nodes for _ in range(nodes)]
    for i in range(nodes):
        dist[i][i] = 0
        curr = graph.inc[i].getFirstRecord()
        while curr is not None:
            edge = curr.elem
            dist[edge.tail][edge.head] = edge.weight
            curr = curr.next

    # apply the relaxation step |V| times
    for i in range(nodes):
        for x in range(nodes):
            for y in range(nodes):
                # relaxation step
                if dist[x][i] + dist[i][y] < dist[x][y]:
                    dist[x][y] = dist[x][i] + dist[i][y]

    return dist[0]


def Dijkstra(graph, root):
    """
    Dijkstra's algorithm for the computation of the shortest path.
    The algorithm assumes a graph implemented as incidence list.
    This implementation leverages the BinaryTree and PriorityQueue data
    structures.
    ---
    Time Complexity: O(|E|*log(|V|))
    Memory Complexity: O()

    :param graph: the graph.
    :param root: the root node to start from.
    :return: the shortest path.
    """
    n = len(graph.nodes)

    # initialize weights:
    # d[i] = inf for every i in E
    # d[i] = 0, if i == root
    currentWeight = n * [INFINITE]
    currentWeight[root] = 0


    # initialize the tree
    tree = Tree(TreeNode(root))
    mstNodes = {root}
    mstWeight = 0

    # initialize the frontier (priority queue)
    pq = PriorityQueue()
    pq.insert((root, Edge(root, root, 0)), 0)

    # while the frontier is not empty ...
    while not pq.isEmpty():
        # pop from the priority queue the node u with the minimum weight
        pq_elem = pq.popMin()
        node = pq_elem[0]
        # if node not yet in the tree, update the tree
        if node not in mstNodes:
            edge = pq_elem[1]
            treeNode = TreeNode(node)
            father = tree.foundNodeByElem(edge.tail)
            father.sons.append(treeNode)
            treeNode.father = father
            mstNodes.add(node)
            mstWeight += edge.weight

        # for every edge (u,v) ...
        curr = graph.inc[node].getFirstRecord()
        while curr is not None:
            edge = curr.elem
            head = edge.head # the head node of the edge
            # if node v not yet added into the tree, push it into the priority
            # queue and apply the relaxation step
            if head not in mstNodes:
                tail = edge.tail
                weight = edge.weight
                currWeight = currentWeight[head]
                distTail = currentWeight[tail]
                pq.insert((head, edge), distTail + weight)
                # relaxation step
                if currWeight == INFINITE:
                    currentWeight[head] = distTail + weight
                elif distTail + weight < currWeight:
                    currentWeight[head] = distTail + weight
            curr = curr.next

    return currentWeight


if __name__ == "__main__":

    graph = Graph()
    graph.addNode('A')  # node 0
    graph.addNode('B')  # node 1
    graph.addNode('C')  # node 2
    graph.addNode('D')  # node 3
    graph.addNode('E')  # node 4
    graph.addNode('F')  # node 5
    graph.addNode('G')  # node 6

    graph.insertEdge(0, 1, 7)
    graph.insertEdge(0, 2, 14)
    graph.insertEdge(0, 3, 30)
    graph.insertEdge(1, 2, 6)
    graph.insertEdge(3, 2, 10)
    graph.insertEdge(2, 4, 1)
    graph.insertEdge(4, 5, 6)
    graph.insertEdge(4, 6, 9)
    graph.insertEdge(5, 6, 4)

    print("BellmanFordMoore:")
    distances = BellmanFord(graph, 0)
    print("\tDistances:", distances)

    print("FloydWarshall:")
    distances = FloydWarshall(graph)
    print("\tDistances:", distances)

    print("Dijkstra:")
    distances = Dijkstra(graph, 0)
    print("\tDistances:", distances)
