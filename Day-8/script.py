def part_1(grid):
    visible = 0
    grid_size = len(grid)

    for col in range(1, grid_size - 1):
        for row in range(1, grid_size - 1):
            print(grid[col][row])

    return None

if __name__ == "__main__":
    with open('_input.txt', 'r') as input:
        grid = [i.rstrip() for i in input.readlines()]
    
    grid_size = len(grid)

    print(grid)
    part_1(grid)
