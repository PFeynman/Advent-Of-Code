import math

def part_1(operations):
  total = 0

  for i in range(len(operations[0])):
    operator = operations[-1][i]
    operands = []
    for j in range(len(operations) - 1):
      operands.append(int(operations[j][i]))
    
    if operator == '+':
      total += sum(operands)
    else:
      total += math.prod(operands)

  return total

if __name__ == "__main__":
  with open('test_input.txt', 'r') as input:
    operations = [i.rstrip().split() for i in input.readlines()]

  print(f'Part 1 solution: {part_1(operations)}')
