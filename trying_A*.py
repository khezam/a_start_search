import math
intersections = {0: [0.7801603911549438, 0.49474860768712914],
                            1: [0.5249831588690298, 0.14953665513987202],
                            2: [0.8085335344099086, 0.7696330846542071],
                            3: [0.2599134798656856, 0.14485659826020547],
                            4: [0.7353838928272886, 0.8089961609345658],
                            5: [0.09088671576431506, 0.7222846879290787],
                            6: [0.313999018186756, 0.01876171413125327],
                            7: [0.6824813442515916, 0.8016111783687677],
                            8: [0.20128789391122526, 0.43196344222361227],
                            9: [0.8551947714242674, 0.9011339078096633],
                            10: [0.7581736589784409, 0.24026772497187532],
                            11: [0.25311953895059136, 0.10321622277398101],
                            12: [0.4813859169876731, 0.5006237737207431],
                            13: [0.9112422509614865, 0.1839028760606296],
                            14: [0.04580558670435442, 0.5886703168399895],
                            15: [0.4582523173083307, 0.1735506267461867],
                            16: [0.12939557977525573, 0.690016328140396],
                            17: [0.607698913404794, 0.362322730884702],
                            18: [0.719569201584275, 0.13985272363426526],
                            19: [0.8860336256842246, 0.891868301175821],
                            20: [0.4238357358399233, 0.026771817842421997],
                            21: [0.8252497121120052, 0.9532681441921305],
                            22: [0.47415009287034726, 0.7353428557575755],
                            23: [0.26253385360950576, 0.9768234503830939],
                            24: [0.9363713903322148, 0.13022993020357043],
                            25: [0.6243437191127235, 0.21665962402659544],
                            26: [0.5572917679006295, 0.2083567880838434],
                            27: [0.7482655725962591, 0.12631654071213483],
                            28: [0.6435799740880603, 0.5488515965193208],
                            29: [0.34509802713919313, 0.8800306496459869],
                            30: [0.021423673670808885, 0.4666482714834408],
                            31: [0.640952694324525, 0.3232711412508066],
                            32: [0.17440205342790494, 0.9528527425842739],
                            33: [0.1332965908314021, 0.3996510641743197],
                            34: [0.583993110207876, 0.42704536740474663],
                            35: [0.3073865727705063, 0.09186645974288632],
                            36: [0.740625863119245, 0.68128520136847],
                            37: [0.3345284735051981, 0.6569436279895382],
                            38: [0.17972981733780147, 0.999395685828547],
                            39: [0.6315322816286787, 0.7311657634689946]}


G = [[36, 34, 31, 28, 17],
 [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
 [39, 36, 21, 19, 9, 7, 4],
 [35, 20, 15, 11, 6],
 [39, 36, 21, 19, 9, 7, 2],
 [32, 16, 14],
 [35, 20, 15, 11, 1, 3],
 [39, 36, 22, 21, 19, 9, 2, 4],
 [33, 30, 14],
 [36, 21, 19, 2, 4, 7],
 [31, 27, 26, 25, 24, 18, 17, 13],
 [35, 20, 15, 3, 6],
 [37, 34, 31, 28, 22, 17],
 [27, 24, 18, 10],
 [33, 30, 16, 5, 8],
 [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
 [37, 30, 5, 14],
 [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
 [31, 27, 26, 25, 24, 1, 10, 13, 17],
 [21, 2, 4, 7, 9],
 [35, 26, 1, 3, 6, 11, 15],
 [2, 4, 7, 9, 19],
 [39, 37, 29, 7, 12],
 [38, 32, 29],
 [27, 10, 13, 18],
 [34, 31, 27, 26, 1, 10, 15, 17, 18],
 [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
 [31, 1, 10, 13, 18, 24, 25, 26],
 [39, 36, 34, 31, 0, 12, 17],
 [38, 37, 32, 22, 23],
 [33, 8, 14, 16],
 [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
 [38, 5, 23, 29],
 [8, 14, 30],
 [0, 12, 17, 25, 26, 28, 31],
 [1, 3, 6, 11, 15, 20],
 [39, 0, 2, 4, 7, 9, 28],
 [12, 16, 22, 29],
 [23, 29, 32],
 [2, 4, 7, 22, 28, 36]]

# This is the correct version from A* algorithm I implemented so far
"""I understand python has a built-in heap data strucres but decided to build it from scrach to practice.
"""
def insert(heap, node, element):
    """Insert nodes into the end of the heap and then calling siftUp() function to maintain a priority of min-heap
        Note: The heap structure  
    """
    n = len(heap)
    if n == 0:
        heap.append((node, element))
        return heap
    heap.append((node, element))
    n = len(heap)-1
    return siftUp(heap, n, node)
    
def swap(heap, first, last):
    """The varible 'last' is an index that containss a value smaller than the value at index 'first'.
        Swap a child vertix with a parent vertix and the return back nothing
    """
    tmp = heap[last]
    heap[last] = heap[first]
    heap[first] = tmp
    return 
        
def siftUp(heap, position, node):
    """The varible 'position' is an index that containes a child verticx that's less than the value at index parent 
    """
    parent = (position - 1) // 2
    if position <= 0 or heap[position][1] >= heap[parent][1]:
        return heap
    swap(heap, parent, position)
    return siftUp(heap, parent, node)
    
def extract(heap):
    """Take the last value in the heap and set to be at index zero which it becomes root.
        Then delete the last value at the end of the heap. And then siftDown to mantain a min_heap
    """
    n = len(heap)
    if n == 0:
        return "Heap is empty"
    heap[0] = heap[n-1]
    heap.pop()
    n = len(heap) - 1
    return siftDown(heap, n - n)

def heappopmin(heap):
    """This function is the same extract but it returns back a tuple that containes a vertix and the total cost
    """
    val = heap[0]
    new_top = heap.pop()
    if len(heap) == 0:
        return val
    heap[0] = new_top
    siftDown(heap, 0)
    return val[0], val[1]

def siftDown(heap, position):
    left = (2 * position) + 1
    right = (2 * position) + 2
    if left > len(heap)-1 or right > len(heap)-1:
        if left <= len(heap)-1 and heap[left][1] < heap[position][1]:
            return swap(heap, position, left)
        if right <= len(heap)-1 and heap[right][1] < heap[position][1]:
            return swap(heap, position, right)
        return heap
    if heap[left][1] < heap[right][1] and heap[position][1] > heap[left][1]:
        swap(heap, position, left)
        return siftDown(heap, left)
    if heap[right][1] < heap[left][1] and heap[position][1] > heap[right][1]:
        swap(heap, position, right)
        return siftDown(heap, right)
    return heap

def euclidean(start, goal):
    """This function measures two things:
            1- The distance from where we are to the next stop or how long its gonna take from where we are to the next stop.
            2- An estimation distance of how long is gonna take from the next stop location(in front of us) to the final destination.
        Note:
            There are some other methods that measure the distance between twp locations such Manhattan Distance but Euclidean Distance
            is better for this type of measuring.
    """
    return math.sqrt(((intersections[start][0] - intersections[goal][0]) ** 2) + ((intersections[start][1] - intersections[goal][1]) ** 2))

def shortest_path(graphMap, start_node, end_node):
    # frontier is heap
    frontier = [(start_node, 0)]
    # explored_so_far keeps track of where we have been so far and how long it took from the start point to each location
    explored_so_far = {start_node:0}
    # path_to_goal is the path of the shortest distance from start point to final destination
    path_to_goal = {start_node:[start_node]}
    while len(frontier):
        current_node = heappopmin(frontier)[0]
        print(current_node)

        if current_node == end_node:
            if current_node == end_node and len(frontier) == 0:
                return [current_node]
            path_to_goal[neighbor] = path_to_goal[current_node] + [neighbor]
            return path_to_goal[end_node]

        neighbors = graphMap[current_node]
        for neighbor in neighbors:
            # path_cost = how long is gonna take to get to the next stop + how long it took from the start point to where we are
            path_cost = euclidean(current_node, neighbor) + explored_so_far[current_node]
            # If we have not been to where we are yet, then check the following:
                # total_cost_to_neighbor = the total traveled distance(path_cost) + the estimated travel distance from where we are to the final destination
                # go ahead and add total_cost_to_neighbor to the list(frontier/heap) which only picks the shortest distance
                # set the current location = the total traveled distance to current location or how long it took to get here and add it to explored_so_far
            if neighbor not in explored_so_far or path_cost < explored_so_far[neighbor]:
                total_cost_to_neighbor = path_cost + euclidean(neighbor, end_node)
                insert(frontier, neighbor, total_cost_to_neighbor)
                explored_so_far[neighbor] = path_cost
                path_to_goal[neighbor] = path_to_goal[current_node] + [neighbor]
    return False 

result = shortest_path(G, 8, 24)
print("path is {}".format(result))