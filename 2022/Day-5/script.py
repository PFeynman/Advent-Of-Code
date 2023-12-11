import re

def parse_instruction(instruction):
    m = re.search('move (\d+) from (\d+) to (\d+)', instruction)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))

def part_1(crates_stack, instructions):
    for instruction in instructions:
        times, from_stack, to_stack = parse_instruction(instruction)
        for t in range(times):
            crate = crates_stack[from_stack - 1].pop()
            crates_stack[to_stack - 1].append(crate)
        
    result = ''
    for stack in crates_stack:
        result += stack[-1]

    return result

def part_2(crates_stack, instructions):
    for instruction in instructions:
        times, from_stack, to_stack = parse_instruction(instruction)
        crates = []
        for t in range(times):
            crates.append(crates_stack[from_stack - 1].pop())
        crates.reverse()
        for crate in crates:
            crates_stack[to_stack - 1].append(crate)

    
    result = ''
    for stack in crates_stack:
        result += stack[-1]

    return result


if __name__ == "__main__":
    stack_pos = []
    crates_stack = []
    with open('input.txt', 'r') as input:
        stack_strings, instructions = (i.splitlines() for i in input.read().strip('\n').split('\n\n'))
        
        stack_strings.reverse()
        
        for i in range(len(stack_strings[0])):
            if stack_strings[0][i] != ' ':
                stack_pos.append(i)
                crates_stack.append([])
        
        for stack in stack_strings[1:]:
            for i, pos in enumerate(stack_pos):
                if stack[pos] != ' ':
                    crates_stack[i].append(stack[pos])
        
        print(part_2(crates_stack, instructions))
        #part_2(crates_stack, instructions)
