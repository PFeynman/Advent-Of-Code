import re

def part_1(ranges):
  sum = 0
  for r in ranges:
    ids = r.split('-')
    for i in range(int(ids[0]), int(ids[1]) + 1):
      result = re.search(r"(^\d+)\1$", str(i))
      if result != None:
        sum += int(result.group())
  return sum

def part_2(ranges):
  sum = 0
  for r in ranges:
    ids = r.split('-')
    for i in range(int(ids[0]), int(ids[1]) + 1):
      result = re.search(r"(^\d+)\1+$", str(i))
      if result != None:
        sum += int(result.group())
  return sum

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    ranges = [r for line in input for r in line.rstrip().split(',')]

  print(part_2(ranges))
