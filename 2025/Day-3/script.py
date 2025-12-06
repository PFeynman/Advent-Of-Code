from itertools import combinations

def part_1(banks):
  sum = 0
  for bank in banks:
    bateries = [int(batery) for batery in bank]
    
    greatest_joltage = bateries[0]
    for joltage in bateries[1:-1]:
      if joltage > greatest_joltage:
        greatest_joltage = joltage
    position = bateries.index(greatest_joltage)

    second_greatest_joltage = bateries[position+1]
    for joltage in bateries[position+1:]:
      if joltage > second_greatest_joltage:
        second_greatest_joltage = joltage

    sum += int(str(greatest_joltage) + str(second_greatest_joltage))
    
  return sum

def find_joltage(joltages, missing=12):
  selected = ''
  if missing == len(joltages):
    return joltages
  elif missing == 0:
    return '';
  else:
    max = joltages[0]
    max_index = 0
    for j in enumerate(joltages[:len(joltages) - missing + 1]):
      if int(j[1]) > int(max):
        max = j[1]
        max_index = j[0]
    
    selected += max
    
    return selected + find_joltage(joltages[max_index + 1:], missing - 1)

def part_2(banks):
  sum = 0

  for bank in banks:
    sum += int(find_joltage(bank))

  return sum

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    banks = [i.rstrip() for i in input.readlines()]

  print(part_2(banks))
