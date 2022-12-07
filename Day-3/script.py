PRIORITY_DICT = {}

def char_range(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 2))

def part_1(rucksacks):
    result_sum = 0
    for rucksack in rucksacks:
        rucksack_size = len(rucksack) - 1
        half_1 = rucksack[0:rucksack_size//2]
        half_2 = rucksack[rucksack_size//2:]
        
        for item in half_1:
            if item in half_2:
                result_sum += PRIORITY_DICT[item]
                break
    
    return result_sum

def part_2(rucksacks):
    result_sum = 0
    groups = zip(*(iter(rucksacks),)*3)
    
    for group in groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                result_sum += PRIORITY_DICT[item]
                break
    
    return result_sum

if __name__ == "__main__":

    for item, priority in zip(char_range('a', 'z'), range(1, 27)):
        PRIORITY_DICT[item] = priority
    for item, priority in zip(char_range('A', 'Z'), range(27, 53)):
        PRIORITY_DICT[item] = priority

    with open('input.txt', 'r') as input:
        rucksacks = input.readlines()
        
        print(part_2(rucksacks))
