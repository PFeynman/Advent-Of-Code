def part_1(message):
    return None
if __name__ == "__main__":
    with open('input.txt', 'r') as input:
        messages = [x for x in input.readlines()]

    for message in messages:
        print(part_1(message))