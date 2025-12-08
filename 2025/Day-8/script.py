import pprint
import math
import numpy as np
import time

def part_1(junction_boxes):
  distances = np.zeros((len(junction_boxes), len(junction_boxes)), dtype=float)

  for i in range(len(junction_boxes)):
    for j in range(len(junction_boxes)):
      distances[i][j] = math.dist(junction_boxes[i], junction_boxes[j])

  circuits = [[i] for i in range(len(junction_boxes))]
  # 0: 162,817,812 and 425,690,689
  # 1: 162,817,812 and 431,825,988
  # 2: 906,360,560 and 805,96,715
  # 3: 431,825,988 and 425,690,689 -> Nothing happens
  min_val = 0
  iter_count = 0
  connections_done = 0
  while connections_done < 10:
    masked = np.where(distances > min_val, distances, np.inf)
    flat_idx = np.argmin(masked)
    idx = np.unravel_index(flat_idx, distances.shape)
    min_val = distances[idx]
    print(idx)
    print(junction_boxes[idx[0]], junction_boxes[idx[1]])
    
    if circuits[idx[1]]: 
      circuits[idx[0]].append(idx[1].item())
      connections_done += 1
    circuits[idx[1]].clear()
    print(circuits)
    distances[idx[1], :] = 0
    distances[:, idx[1]] = 0

  print(circuits)
  return None

def part_2(junction_boxes):
  
  return None

if __name__ == "__main__":
  with open('test_input.txt', 'r') as input:
    junction_boxes = [list(map(int, i.rstrip().split(','))) for i in input.readlines()]

  print(f'Part 1 solution: {part_1(junction_boxes)}')
  print(f'Part 2 solution: {part_2(junction_boxes)}')
