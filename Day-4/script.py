def range_from_list(list):
    return range(list[0], list[1] + 1)

def part_2(assignment_pairs):
    overlapped = 0
    for pair in assignment_pairs:
        assignments = pair.rstrip().split(',')
        assignment_1 = {x for x in range_from_list(list(map(int, assignments[0].split('-'))))}
        assignment_2 = {x for x in range_from_list(list(map(int, assignments[1].split('-'))))}
        if len(assignment_1.intersection(assignment_2)):
            overlapped += 1

    return overlapped

def part_1(assignment_pairs):
    contained = 0
    for pair in assignment_pairs:
        assignments = pair.rstrip().split(',')
        assignment_1 = {x for x in range_from_list(list(map(int, assignments[0].split('-'))))}
        assignment_2 = {x for x in range_from_list(list(map(int, assignments[1].split('-'))))}
        if (assignment_1.issubset(assignment_2) or assignment_2.issubset(assignment_1)):
            contained += 1
    
    return contained
        
if __name__ == "__main__":
    with open('input.txt', 'r') as input:
        assignment_pairs = input.readlines()
        print('Part 1 result: ' + str(part_1(assignment_pairs)))
        print('Part 2 result: ' + str(part_2(assignment_pairs)))
        
