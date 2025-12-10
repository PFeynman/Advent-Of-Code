import time

tachyon_manifold = []

def part_1():
  splits = 0
  s = (0, tachyon_manifold[0].index('S'))
  tachyon_manifold[1][s[1]] = '|'

  for i in range(2, len(tachyon_manifold)):
    for j in range(len(tachyon_manifold[i])):
      if tachyon_manifold[i][j] == '^' and tachyon_manifold[i-1][j] == '|':
        splits += 1
        tachyon_manifold[i][j-1] = tachyon_manifold[i][j+1] = '|'
      if tachyon_manifold[i][j] == '.' and tachyon_manifold[i-1][j] == '|':
        tachyon_manifold[i][j] = '|'

  return splits

memory = {}
def memorize(f):    
  def inner(point):
    if point not in memory:
      memory[point] = f(point)
    return memory[point]

  return inner

@memorize
def timelines(point):
  current_point = point
  if point[1] < 0 or point[1] >= len(tachyon_manifold[0]):
    return 0
  while current_point[0] < len(tachyon_manifold):
    if tachyon_manifold[current_point[0]][current_point[1]] == '^':
      return timelines((current_point[0] + 1, current_point[1] - 1)) + timelines((current_point[0] + 1, current_point[1] + 1))
    current_point = (current_point[0] + 1, current_point[1])
  return 1

def part_2():
  s = (0, tachyon_manifold[0].index('S'))
  
  timelines_count = timelines(s)
  return timelines_count

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    tachyon_manifold = [list(i.rstrip('\n')) for i in input.readlines()]

  print(f'Part 1 solution: {part_1()}')
  print(f'Part 2 solution: {part_2()}')
