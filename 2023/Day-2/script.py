import re

class Game:
  def __init__(self, game_str) -> None:
    self.id = int(re.search('Game (\d+):', game_str).group(1))
    self.iterations = [i.strip() for i in re.search('Game \d+: (.*)', game_str).group(1).split(';')]

  def __str__(self) -> str:
    return f'Game id: {self.id}, iterations: {self.iterations}'

  def is_possible(self, red: int, blue:int , green: int):
    for i in self.iterations:
      i_red = int(re.search('(\d+) red', i).group(1)) if re.search('(\d+) red', i) else 0
      i_blue = int(re.search('(\d+) blue', i).group(1)) if re.search('(\d+) blue', i) else 0
      i_green = int(re.search('(\d+) green', i).group(1)) if re.search('(\d+) green', i) else 0
      if i_red > red or i_blue > blue or i_green > green:
        return False
    return True
  
  def power(self):
    min_red = 0
    min_blue = 0
    min_green = 0
    for i in self.iterations:
      i_red = int(re.search('(\d+) red', i).group(1)) if re.search('(\d+) red', i) else 0
      i_blue = int(re.search('(\d+) blue', i).group(1)) if re.search('(\d+) blue', i) else 0
      i_green = int(re.search('(\d+) green', i).group(1)) if re.search('(\d+) green', i) else 0
      min_red = i_red if i_red > min_red else min_red
      min_blue = i_blue if i_blue > min_blue else min_blue
      min_green = i_green if i_green > min_green else min_green

    return min_red * min_blue * min_green
      
def part_1(games):
  return sum(g.id for g in games if g.is_possible(12, 14, 13))

def part_2(games):
  return sum(g.power() for g in games)

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    games = [Game(i.rstrip()) for i in input.readlines()]
  
  print(part_2(games))