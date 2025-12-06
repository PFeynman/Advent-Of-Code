import math
import pprint

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

def part_2(operations):
  total = 0
  operands = []
  lines = len(operations)
  delimiter = ' ' * (lines - 1)

  for j in range(len(operations[0]) - 1, -1, -1):
    operand = ''
    for i in range(lines):
      if i == lines - 1:
        if operand == delimiter:
          continue
        else:
          operands.append(int(operand))
          operand = ''
          if operations[i][j] != ' ':
            if operations[i][j] == '+':
              total += sum(operands)
            else:
              total += math.prod(operands)
            operands = []
      else:
        operand += operations[i][j]

  return total

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    operations = [i.rstrip('\n') for i in input.readlines()]

    operations_part1 = [i.rstrip().split() for i in operations]

  print(f'Part 1 solution: {part_1(operations_part1)}')
  print(f'Part 2 solution: {part_2(operations)}')
