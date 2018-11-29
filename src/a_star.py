import argparse

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

# def heuristic():
# # TODO
# def a_star():
# # TODO

if __name__ == "__main__":
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
        print(data_tuple)
    # with open(args.solution, 'w') as f:
    #     print("\n\nHere is the solution: \n\n")
