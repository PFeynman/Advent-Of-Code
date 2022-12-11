def part_1(message):
    chunk_size = 14
    begin = 0

    while begin + chunk_size < len(message):
        prev_begin = begin
        chunk = message[begin:begin + chunk_size]
        for i in range(chunk_size):
            if (f := chunk.find(chunk[i], i + 1)) != -1:
                begin += (i + 1)
                break
        if prev_begin == begin:
            break
    
    return begin + chunk_size

if __name__ == "__main__":
    with open('input.txt', 'r') as input:
        message = input.read()
    
    print(part_1(message))
    # Part 1 and 2 are the same with the difference of chunk size