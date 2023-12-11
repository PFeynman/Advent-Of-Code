import re

spelled_digits = {
  "one": "o1e",
  "two": "t2o",
  "three": "t3e",
  "four": "f4r",
  "five": "f5e",
  "six": "s6x",
  "seven": "s7n",
  "eight": "e8t",
  "nine": "n9e"
}

def part_1(lines):
  digits = [re.findall(r'\d', d) for d in lines]
  calibration_sum = 0

  for e in digits:
    if len(e) < 2:
      e.append(e[0])
    calibration = e[0] + e[-1]
    calibration_sum += int(calibration)
    
  return calibration_sum

def part_2(lines):
  amended_lines = []
  for l in lines:
    for k, v in spelled_digits.items():
      l = l.replace(k, v)
    amended_lines.append(l)
  
  return part_1(amended_lines)
  
if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    lines = [i.rstrip() for i in input.readlines()]

  print(part_2(lines))
