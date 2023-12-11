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

def part_2(grid):
    grid_size = len(grid)
    max_trees_visible = 0
    
    for row in range(grid_size):
        for col in range(grid_size):
            trees_visible = 1
            # Check for top
            visibles = 0
            for i in range(row - 1, -1, -1):
                visibles += 1
                if grid[row][col] <= grid[i][col]:
                    break
            trees_visible *= visibles
            # Check for left
            visibles = 0
            for i in range(col - 1, -1, -1):
                visibles += 1
                if grid[row][col] <= grid[row][i]:
                    break
            trees_visible *= visibles
            # Check for bottom
            visibles = 0
            for i in range(row + 1, grid_size):
                visibles += 1
                if grid[row][col] <= grid[i][col]:
                    break
            trees_visible *= visibles
            # Check for right
            visibles = 0
            for i in range(col + 1, grid_size):
                visibles += 1
                if grid[row][col] <= grid[row][i]:
                    break
            trees_visible *= visibles

            if trees_visible > max_trees_visible:
                max_trees_visible = trees_visible

    return max_trees_visible

if __name__ == "__main__":
    with open('input.txt', 'r') as input:
        grid = [i.rstrip() for i in input.readlines()]

    print(part_2(grid))
