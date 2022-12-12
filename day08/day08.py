# For this time, I'll refer to the grid as "forest", because well. That is a forest. Right?
# PS: I wish I knew what "all" did earlier.. lol

def part1():
    with open ("day08/file.txt") as file:

        input_file=file.read().strip().split()
        forest_grid = [list(map(int, list(line))) for line in input_file]

        forest_lenght=len(forest_grid[0])
        forest_height=len(forest_grid)
        tree_counter=0
        print(forest_grid)  

        for i in range(forest_height):
            for j in range(forest_lenght):
                tree_height=forest_grid[i][j]
                if all(forest_grid[i][jj] < tree_height for jj in range(j)) or all(forest_grid[i][jj] < tree_height for jj in range(j+1, forest_lenght)) or all(forest_grid[ii][j] < tree_height for ii in range(i)) or all(forest_grid[ii][j] < tree_height for ii in range(i+1, forest_height)): 
                    tree_counter+=1

        return tree_counter
    
print(part1())

def part2():
    with open ("day08/file.txt") as file:
        pass