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
  
  count = 0

  selected_ranges = [fresh_ids_ranges[0]]

  for id_range in fresh_ids_ranges[1:]:
    print(f'Checking: {id_range}')
    selectable = True
    for selected in enumerate(selected_ranges):
      print(f'Selected: {selected}')
      if id_range[0] < selected[1][0] and id_range[1] > selected[1][1]:
        # The checking range is a superset of the already selected one.
        selected_ranges[selected[0]] = id_range
        selectable = False
        break
      elif id_range[0] < selected[1][0] and id_range[1] >= selected[1][0] and id_range[1] < selected[1][1]:
        # The already selected and the checking range intersect. The lower bound is of the checking one
        selected_ranges[selected[0]][0] = id_range[0]
        selectable = False
        break
      elif id_range[0] > selected[1][0] and id_range[1] < selected[1][1]:
        # The checking range is inside the already selected one
        selectable = False
        break
      elif id_range[0] > selected[1][0] and id_range[0] < selected[1][1] and id_range[1] >= selected[1][1]:
        # The already selected and the checking range intersect. The upper bound is of the checking one
        selected_ranges[selected[0]][1] = id_range[1]
        selectable = False
        break
    
    if selectable:
      selected_ranges.append(id_range)

  print(len(selected_ranges))
  return None

if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    fresh_ids_ranges, available_ids = (i.splitlines() for i in input.read().strip('\n').split('\n\n'))
  
  fresh_ids_ranges = [list(map(int, r.split("-"))) for r in fresh_ids_ranges]
  available_ids = list(map(int, available_ids))


  print(f'Part 1 solution: {part_1(fresh_ids_ranges, available_ids)}')
  print(f'Part 2 solution: {part_2(fresh_ids_ranges)}')
