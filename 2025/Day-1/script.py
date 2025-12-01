def part_1(lines):
  dial_position = 50
  times_dial_0 = 0

  for line in lines:
    turn_direction = line[0]
    turn_positions = int(line[1:])
    if turn_direction == "L":
      dial_position = (dial_position - turn_positions) % 100
    else:
      dial_position = (dial_position + turn_positions) % 100
    
    if dial_position == 0:
      times_dial_0 += 1
    
  return times_dial_0

def part_2(lines):
  dial_position = 50
  times_dial_0 = 0

  for line in lines:
    turn_direction = line[0]
    raw_turn_positions = int(line[1:])
    complete_turns = int(raw_turn_positions / 100)
    turn_positions = raw_turn_positions % 100
    passed_through_0 = False

    if turn_direction == "L":
      dial_position = dial_position - turn_positions
      if dial_position < 0 and dial_position + turn_positions > 0:
        passed_through_0 = True
      dial_position = dial_position % 100
    else:
      dial_position = dial_position + turn_positions
      if dial_position > 100:
        passed_through_0 = True
      dial_position = dial_position % 100
    
    times_dial_0 += complete_turns

    if passed_through_0:
      times_dial_0 += 1

    if dial_position == 0:
      times_dial_0 += 1
    
  return times_dial_0
  
if __name__ == "__main__":
  with open('input.txt', 'r') as input:
    lines = [i.rstrip() for i in input.readlines()]

  print(part_2(lines))
