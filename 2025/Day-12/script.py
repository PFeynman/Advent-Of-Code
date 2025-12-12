def parse_file(filename):
  hashtags_count = {}
  current_block = None

  trees_info = []

  with open(filename, 'r') as f:
      for line in f:
          line = line.strip()
          if not line:
              continue

          if line.endswith(':') and line[:-1].isdigit():
              current_block = int(line[:-1])
              hashtags_count[current_block] = 0
              continue

          if ':' in line and 'x' in line:
              current_block = None
              
              parts = line.split(':')
              dimension = parts[0].strip()
              numeros = [int(x) for x in parts[1].strip().split()]

              trees_info.append({
                  'dim': dimension,
                  'vals': numeros
              })
              continue

          if current_block is not None:
              hashtags_count[current_block] += line.count('#')

  present_sizes = [hashtags_count[i] for i in sorted(hashtags_count.keys())]
  
  return present_sizes, trees_info


def part_1(present_sizes, trees_info):
  possible = 0
  for tree in trees_info:
    width, height = tree['dim'].split('x')
    tree_size = int(width) * int(height)
    presents_size_sum = 0
    for i, presents in enumerate(tree['vals']):
      presents_size_sum += present_sizes[i] * presents
    if presents_size_sum <= tree_size:
       possible += 1
      
  return possible

def part_2():
  return None

if __name__ == "__main__":
  present_sizes, trees_info = parse_file('input.txt')

  print(f'Part 1 solution: {part_1(present_sizes, trees_info)}')
  print(f'Part 2 solution: {part_2()}')
