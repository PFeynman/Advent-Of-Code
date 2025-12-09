import pprint
import math
import numpy as np
import time

class UnionFind:
  def __init__(self, size):
      self.parent = [i for i in range(size)]
      self.size = [1] * size
  
  def find(self, x):
      while x != self.parent[x]:
          x = self.parent[x]
      return x
  
  def union(self, x, y):
      rootX = self.find(x)
      rootY = self.find(y)
      if rootX != rootY:
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
  
  def get_sizes(self):
    return self.size
  
  def print_sets(self):
    sets = {}
    print(self.parent)
    for i in range(len(self.parent)):
        root = self.find(i)
        if root not in sets:
            sets[root] = []
        sets[root].append(i)

    print("Conjuntos actuales:")
    for root, elements in sets.items():
        print(f"  {root} -> {elements}")
  
  def isConnected(self):
    root = self.parent[0]
    for i in range(1, len(self.parent)):
        if self.find(i) != root:
            return False
    return True

def part_1(junction_boxes):
  distances = np.zeros((len(junction_boxes), len(junction_boxes)), dtype=float)

  for i in range(len(junction_boxes)):
    for j in range(len(junction_boxes)):
      distances[i][j] = math.dist(junction_boxes[i], junction_boxes[j])

  circuits = UnionFind(len(junction_boxes))

  min_val = 0
  connections_done = 0
  while connections_done < 1000:
    masked = np.where(distances > min_val, distances, np.inf)
    flat_idx = np.argmin(masked)
    idx = np.unravel_index(flat_idx, distances.shape)
    min_val = distances[idx]
    circuits.union(idx[0].item(), idx[1].item())
    connections_done += 1

  sizes = circuits.get_sizes()
  sizes.sort(reverse=True)

  return math.prod(sizes[0:3])

def part_2(junction_boxes):
  distances = np.zeros((len(junction_boxes), len(junction_boxes)), dtype=float)

  for i in range(len(junction_boxes)):
    for j in range(len(junction_boxes)):
      distances[i][j] = math.dist(junction_boxes[i], junction_boxes[j])

  circuits = UnionFind(len(junction_boxes))

  min_val = 0
  connections_done = 0
  current = 0
  while circuits.isConnected() == False:
    masked = np.where(distances > min_val, distances, np.inf)
    flat_idx = np.argmin(masked)
    idx = np.unravel_index(flat_idx, distances.shape)
    min_val = distances[idx]
    circuits.union(idx[0].item(), idx[1].item())
    connections_done += 1

  return junction_boxes[idx[0].item()][0] * junction_boxes[idx[1].item()][0]

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    junction_boxes = [list(map(int, i.rstrip().split(','))) for i in input.readlines()]

  print(f'Part 1 solution: {part_1(junction_boxes)}')
  print(f'Part 2 solution: {part_2(junction_boxes)}')
