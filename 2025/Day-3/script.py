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

def part_2(banks):
  return None

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    banks = [i.rstrip() for i in input.readlines()]

  print(part_1(banks))
