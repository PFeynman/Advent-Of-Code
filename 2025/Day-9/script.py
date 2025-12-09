import numpy as np
import math

def part_1(tiles):
  distances = np.zeros((len(tiles), len(tiles)), dtype=float)

  for i in range(len(tiles)):
    for j in range(len(tiles)):
      distances[i][j] = math.dist(tiles[i], tiles[j])

  flat_idx = np.argmax(distances)
  idx = np.unravel_index(flat_idx, distances.shape)

  base = abs(tiles[idx[0].item()][0] - tiles[idx[1].item()][0]) + 1
  height = abs(tiles[idx[0].item()][1] - tiles[idx[1].item()][1]) + 1

  return base * height

def part_2(tiles):
  return None

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    tiles = [list(map(int, i.rstrip().split(','))) for i in input.readlines()]

  print(f'Part 1 solution: {part_1(tiles)}')
  print(f'Part 2 solution: {part_2(tiles)}')
