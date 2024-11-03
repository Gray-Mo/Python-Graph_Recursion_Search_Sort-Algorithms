def print_path_cost(parents, cost):
    path = ['finish']
    previous = 'finish'
    while (previous != 'start'):
        path.append(parents[previous])
        previous = parents[previous]
    path.reverse()
    for i in range(len(path)):
        if (i==len(path)-1):
            print(path[i] + f' / cost: {cost}')
        else:
            print(path[i] + ' -> ',end ='')

def find_nearest_node(costs, processed):
    shortest_path = float('inf')
    nearest_node = None
    for node in costs:
        cost = costs[node]
        if (cost < shortest_path and node not in processed):
            shortest_path = cost
            nearest_node = node
    return nearest_node

def dijkstra(graph, costs, parents, processed):
    nearest_node = find_nearest_node(costs, processed)
    while (nearest_node is not None):
        cost = costs[nearest_node]
        neighbors = graph[nearest_node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if(new_cost < costs[n]):
                costs[n] = new_cost
                parents[n] = nearest_node
        processed.append(nearest_node)
        nearest_node = find_nearest_node(costs, processed)
    print_path_cost(parents, costs['finish'])


graph = {
    'start':{'a':5, 'b':2},
    'a':{'d':4, 'c':2},
    'b':{'c':7},
    'c':{'finish':1},
    'd':{'c':6, 'finish':3},
    'finish':{}
}
costs = {
    'a':5, 'b':2, 'c':float('inf'), 'd':float('inf'), 'finish':float('inf')
}
parents = {
    'a':'start', 'b':'start', 'c':None, 'd':None, 'finish':None
}
processed = []

dijkstra(graph, costs, parents, processed)
