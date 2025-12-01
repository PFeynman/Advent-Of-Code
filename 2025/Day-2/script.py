if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    lines = [i.rstrip() for i in input.readlines()]

  print(part_2(lines))
