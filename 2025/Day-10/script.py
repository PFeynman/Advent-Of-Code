def part_1():
  return None

def part_2():
  return None

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    _, _, _  = (i.splitlines() for i in input.read().strip('\n').split('\n\n'))

  print(f'Part 1 solution: {part_1()}')
  print(f'Part 2 solution: {part_2()}')
