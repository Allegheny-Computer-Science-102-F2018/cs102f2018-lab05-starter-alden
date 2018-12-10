def get_matrix(content):
# get the info of map, length and width
# and the location of obstacles
    # set enter point
    enterP = (0,0)
    # convert str to lis by line
    content_list = content.splitlines()
    width = len(content_list) #get line width
    i = 0
    obstacles = []
    for line in content_list:
        length = len(line) #get line length
        i+=1 # increament
        # get the index for every # in a line
        index_list = [pos for pos, char in enumerate(line) if char == '#']
        if index_list != []:
            for id in index_list:
                obstacles.append((id, i-1))
    # get exit point, -1 because starts from 0
    exitP = (length-1, width-1)
    return length, width, enterP, exitP, obstacles
# length 0, width 1, enterP 2, exitP 3, obstacles 4

# https://www.redblobgames.com/pathfinding/a-star/
def heuristic(a, b):
    # 4-way Manhatten distance
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    # Open and closed list
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def draw_tile(graph, id, style, width):
    r = "."
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r

def draw_grid(command, graph, width=2, **style):
    with open(command, 'w') as f:
        for y in range(graph.height):
            for x in range(graph.width):
                f.write(b"%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")

if __name__ == "__main__":
    import argparse
    from implementation import *
    # argumant to get the map file path from terminal commend
    parser = argparse.ArgumentParser(description='Input your designed map file path.')
    parser.add_argument('-m', '--map', required=True, help = 'path to the map file')
    parser.add_argument('-s', '--solution', required=True, help = 'path to the output file')
    args = parser.parse_args()
    #initialize map
    with open(args.map, 'rt') as f:
    #open map.txt as read text mode
        # content = f.read() #read content from f
        print("\n\nHere is your map: \n\n")
        content = ''
        for l in f:
            content = content + l
        print(content)
        data_tuple = get_matrix(content)
        #define entry and exit then pass to a_star
        start, goal = data_tuple[2], data_tuple[3]
        diagram = GridWithWeights(data_tuple[0], data_tuple[1])
        diagram.walls = data_tuple[4]
        #diagram.weights =
        came_from, cost_so_far = a_star(diagram, start, goal)
        # write answers
        draw_grid(args.solution, diagram, width=3, point_to=came_from, start=start, goal=goal)
        print("\n\nHere is the solution: \n\n")
