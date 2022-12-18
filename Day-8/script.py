def part_1(grid):
    visible_count = 0
    grid_size = len(grid)

    visible_from_top = [[False for i in range(grid_size)] for j in range(grid_size)]
    visible_from_left = [[False for i in range(grid_size)] for j in range(grid_size)]
    visible_from_right = [[False for i in range(grid_size)] for j in range(grid_size)]
    visible_from_bottom = [[False for i in range(grid_size)] for j in range(grid_size)]

    for i in range(grid_size):
        visible_from_left[i][0] = True
        visible_from_top[0][i] = True
        visible_from_right[i][grid_size - 1] = True
        visible_from_bottom[grid_size - 1][i] = True
      
    # Check from the left
    for i in range(1, grid_size - 1):
        tallest_from_left = grid[i][0]
        for j in range(1, grid_size -1):
            if grid[i][j] > tallest_from_left:
                visible_from_left[i][j] = True
                tallest_from_left = grid[i][j]

    # Check from top
    for i in range(1, grid_size - 1):
        tallest_from_top = grid[0][i]
        for j in range(1, grid_size - 1):
            if grid[j][i] > tallest_from_top:
                visible_from_top[j][i] = True
                tallest_from_top = grid[j][i]
    
    # Check from right
    for i in range(1, grid_size - 1):
        tallest_from_right = grid[i][grid_size - 1]
        for j in range(grid_size - 2, 0, - 1):
            if grid[i][j] > tallest_from_right:
                visible_from_right[i][j] = True
                tallest_from_right = grid[i][j]

    # Check from bottom 
    for i in range(grid_size - 2, 0, - 1):
        tallest_from_bottom = grid[grid_size - 1][i]
        for j in range(grid_size - 2, 0, - 1):
            if grid[j][i] > tallest_from_bottom:
                visible_from_bottom[j][i] = True
                tallest_from_bottom = grid[j][i]

    for i in range(grid_size):
        for j in range(grid_size):
            if visible_from_top[i][j] or visible_from_left[i][j] or visible_from_right[i][j] or visible_from_bottom[i][j]:
                visible_count += 1

    return visible_count

if __name__ == "__main__":
    with open('input.txt', 'r') as input:
        grid = [i.rstrip() for i in input.readlines()]
    
    grid_size = len(grid)

    print(part_1(grid))
