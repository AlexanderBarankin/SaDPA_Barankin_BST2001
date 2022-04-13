def read_file():
    import re
    lt = list()
    data = list()
    pattern = '-*[0-9]+'
    filename = 'graph.txt'
    file = open(filename, 'r')
    lt.append(file.readlines())
    file.close()
    for x in lt:
        data = re.findall(pattern, str(x))
    return data


def set_data(data):
    source = list()
    destination = list()
    edge_cost = list()
    test = 0
    vertices = 0
    edges = 0
    distance = list()
    for x in data:
        if test == 0:
            vertices = x
        if test == 1:
            edges = x
        if test == 2:
            source.append(int(x))
        if test == 3:
            destination.append(int(x))
        if test == 4:
            edge_cost.append(int(x))
            test = 1
        test += 1
    vertex_list = list(vertices)
    test = int(vertices) - 1
    while test > 0:
        vertex_list.append(test)
        test -= 1
    for x in vertex_list:
        source.append(0)
        destination.append(int(x))
        edge_cost.append(0)
    distance = list()
    test = 0
    while test < int(vertices) + 1:
        distance.append(test)
        test += 1
    return vertices, edges, source, destination, edge_cost, vertex_list, distance


def initialize(distance):
    predecessor = list()
    d = list()
    # initialization
    for x in distance:
        if x == 0:
            d.append(0)
        else:
            d.append(999999999)
        predecessor.append('null')
    return d, predecessor


def relax(vertices, source, destination, edge_cost, d, predecessor, edges):
    y = 0
    i = 0
    z = 0
    for x in edge_cost:
        z += 1
    while i < int(vertices):
        while y < int(z):
            if d[int(source[y])] + edge_cost[y] < d[int(destination[y])]:
                d[int(destination[y])] = int(edge_cost[y]) + d[int(source[y])]
                predecessor[int(destination[y])] = source[y]
            y += 1
        y = 0
        i += 1
    return source, destination, edge_cost, d, predecessor


def re_weight(vertices, source, destination, edge_cost, d, edges):
    y = 0
    z = 0
    for x in edge_cost:
        z += 1
    while y < int(z) - 1:
        edge_cost[y] = edge_cost[y] + d[int(source[y])] - d[int(destination[y])]
        y += 1
    return source, destination, edge_cost, d


def output(source, destination, edge_cost):
    print('Output in the form...')
    print('[Source]')
    print('[Destination]')
    print('[Reweighting]')
    print()
    print('Running Dijkstra on vertex n')
    print('vertices [0...n]')
    print('previous of [0...n]')
    print('cost of [0...n]')
    print()
    print()
    print(source)
    print(destination)
    print(edge_cost)
    print()


def Dijkstra(vertex_list, source_vertex, source, destination, edge_cost, predecessor, edges, vertices):
    u = 0
    v = 0
    alt = 0
    count = 0
    smallest = 9999999
    new_vertex_list = list()
    new_vertex_list.append(0)
    for x in vertex_list:
        new_vertex_list.append(int(x))
    dist = list()
    previous = list()
    Q = set(new_vertex_list)
    Q.remove(0)
    for x in new_vertex_list:
        if int(x) == int(source_vertex):
            dist.append(0)
        else:
            dist.append(9999999)
        previous.append('undefined')
    while len(Q) != 0:
        for y in Q:
            if y != 0:
                if dist[int(y)] < smallest:
                    smallest = dist[y]
                    u = y
                if dist[y] == 999999:
                    break
        smallest = 9999999
        Q.remove(u)
        while int(count) < int(edges) + 1:
            if source[count] == u:
                v = destination[count]
                alt = dist[u] + edge_cost[count]
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
            count += 1
        count = 0
    print('Vertices:' + str(new_vertex_list))
    print('Previous:' + str(previous))
    print('Cost:    ' + str(dist))
    print()


def Johnson():
    data = list()
    source = list()
    destination = list()
    edge_cost = list()
    test = 0
    vertices = 0
    edges = 0
    data = read_file()
    vertex_list = list()
    distance = list()
    vertices, edges, source, destination, edge_cost, vertex_list, distance = set_data(data)
    predecessor = list()
    d = list()
    d, predecessor = initialize(distance)
    # relaxation
    source, destination, edge_cost, d, predecessor = relax(vertices, source, destination, edge_cost, d, predecessor,
                                                           edges)
    # change weights
    vertex_list.reverse()
    source, destination, edge_cost, d = re_weight(vertices, source, destination, edge_cost, d, edges)
    output(source, destination, edge_cost)
    for x in vertex_list:
        print('Running Dijkstra on vertex ' + str(x))
        Dijkstra(vertex_list, x, source, destination, edge_cost, predecessor, edges, vertices)


if __name__ == '__main__':
    Johnson()
