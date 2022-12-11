import re
import time

class Node:
    def __init__(self, parent, name, size = 0):
        self.parent = parent
        self.name = name
        self.children = []
        self._size = size
    
    def __str__(self) -> str:
        return f'{self.name} {self.size()}'
    
    def cd(self, dir_name):
        for x in self.children:
            if x.name == dir_name:
                return x
    
    def size(self):
        if self._size != 0:
            return self._size
        else:
            children_size = 0
            for child in self.children:
                children_size += child.size()
            return children_size
    
    def traverse(self):
        for child in self.children:
            child.traverse()

        print(self)
    
    def is_leaf(self):
        return len(self.children) == 0

def part_1(node):
    sum = 0
    if node.size() <= 100000 and not node.is_leaf():
        sum += node.size()

    for child in node.children:
        sum += part_1(child)

    return sum

if __name__ == "__main__":
    cd_pattern = '(\$ cd) (.+)'
    file_pattern = '(\d+) (\w+(\.\w+)?)'
    dir_pattern = 'dir (\w+)'

    with open('input.txt', 'r') as input:
        console = [i for i in input.readlines()]

    fs = Node(None, '/')
    current_dir = fs

    for line in console:
        if line[0] == '$':
            if (m := re.search(cd_pattern, line)) is not None:
                if m.group(2) == '/':
                    continue
                current_dir = current_dir.parent if m.group(2) == '..' else current_dir.cd(m.group(2))
        else:
            if (m:= re.search(file_pattern, line)) is not None:
                new_node = Node(current_dir, m.group(2), int(m.group(1)))
            else:
                m = re.search(dir_pattern, line)
                new_node = Node(current_dir, m.group(1))
            
            current_dir.children.append(new_node)
    
    print(part_1(fs))
