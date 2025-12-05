from operator import methodcaller
import pprint

def part_1(fresh_ids_ranges, available_ids):
  sum = 0

  for id in available_ids:
    for fresh_id in fresh_ids_ranges:
      if id >= fresh_id[0] and id <= fresh_id[1]:
        sum += 1
        break

  return sum

def part_2(fresh_ids_ranges):
  union = set()

  for id_range in fresh_ids_ranges:
    tmp = set(range(id_range[0], id_range[1] + 1))
    union = union | tmp
  
  return len(union)

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    fresh_ids_ranges, available_ids = (i.splitlines() for i in input.read().strip('\n').split('\n\n'))
  
  fresh_ids_ranges = [list(map(int, r.split("-"))) for r in fresh_ids_ranges]
  available_ids = list(map(int, available_ids))
  
  print(f'Part 1 solution: {part_1(fresh_ids_ranges, available_ids)}')
  print(f'Part 2 solution: {part_2(fresh_ids_ranges)}')
