if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    engine = [list(i.rstrip()) for i in input.readlines()]

  print(engine)
  