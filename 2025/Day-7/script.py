import pprint

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

def part_2():
  timelines = 0
  s = (0, tachyon_manifold[0].index('S'))
  tachyon_manifold[1][s[1]] = '|'

  for i in range(2, len(tachyon_manifold)):
    for j in range(len(tachyon_manifold[i])):
      if tachyon_manifold[i][j] == '^' and tachyon_manifold[i-1][j] == '|':
        tachyon_manifold[i][j-1] = tachyon_manifold[i][j+1] = '|'
      if tachyon_manifold[i][j] == '.' and tachyon_manifold[i-1][j] == '|':
        tachyon_manifold[i][j] = '|'
  
  pprint.pp(tachyon_manifold)

  stack = []
  stack.append(s)
  stack.append((current[0] + 1, current[1]))

  while len(stack) > 0:
    current = stack.pop()
    if tachyon_manifold[current[0]][current[1]] == 'S':
      stack.append((current[0] + 1, current[1]))
    
    print(stack)
    return None
  
  return None

if __name__ == "__main__":
  with open('test_input.txt', 'r') as input:
    tachyon_manifold = [list(i.rstrip('\n')) for i in input.readlines()]

  print(f'Part 1 solution: {part_1()}')
  print(f'Part 2 solution: {part_2()}')
