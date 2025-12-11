connections = {}

memory = {}
def memorize(f):    
  def inner(device):
    if device not in memory:
      memory[device] = f(device)
    return memory[device]

  return inner

@memorize
def find_out(device):
  print(device)
  if connections[device][0] == 'out':
    return 1
  else:
    return sum(find_out(dev) for dev in connections[device])

def part_1():
  count = sum(find_out(dev) for dev in connections['you'])
  return count

def part_2(connections):
  return None

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    connections = {device: outputs.split() for device, outputs in (line.split(': ') for line in input.read().strip().split('\n'))}

  print(f'Part 1 solution: {part_1()}')
  print(f'Part 2 solution: {part_2(connections)}')
