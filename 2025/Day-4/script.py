import pprint

def is_out_of_bound(i_prime, j_prime, height, width):
  return  i_prime < 0 or i_prime > height - 1 or j_prime < 0 or j_prime > width - 1

def part_1(grid):
  sum = 0
  height = len(grid)
  width  = len(grid[0])
  
  for i in range(height):
    for j in range(width):
      accessible = True
      adjacent_rolls = 0
      if grid[i][j] == '@':
        for i_offset in range(-1, 2):
          for j_offset in range(-1, 2):
            if is_out_of_bound(i + i_offset, j + j_offset, height, width):
              continue

            if i_offset == 0 and j_offset == 0:
              continue
            
            if grid[i + i_offset][j + j_offset] == '@':
              adjacent_rolls += 1
            
            if adjacent_rolls > 3:
              accessible = False
              break
          
          if not accessible:
            break
        
        if accessible:
          sum += 1
            
  return sum

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    grid = [list(i.rstrip()) for i in input.readlines()]

  print(part_1(grid))
