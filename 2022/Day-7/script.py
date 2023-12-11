import re

class Node:
    def __init__(self, parent, name, type = 'd', size = 0):
        self.parent = parent
        self.name = name
        self.children = []
        self.type = type
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
    
    def traverse(self, level = 0):
        for child in self.children:
            child.traverse(level + 1)
        print(' ' * level + str(self))
    
    def is_leaf(self):
        return len(self.children) == 0

def part_1(node):
    sum = 0
    if node.size() <= 100000 and not node.is_leaf():
        sum += node.size()

    for child in node.children:
        sum += part_1(child)

    return sum

def get_directory_sizes(directory):
    sizes = []
    sizes.append(directory.size())

    child_dirs = [x for x in directory.children if x.type == 'd']
    for child in child_dirs:
        sizes.extend(get_directory_sizes(child))
    
    return sizes

def part_2(node):
    fs_size = 70000000
    update_size = 30000000
    free_space = fs_size - node.size()
    required_space = update_size - free_space
    current_node = node

    dirSizes = get_directory_sizes(current_node)
    dirSizes.sort()

    for size in dirSizes:
        if size >= required_space:
            return size

if __name__ == "__main__":
    cd_pattern = '(\$ cd) (.+)'
    file_pattern = '(\d+) (\w+(\.\w+)?)'
    dir_pattern = 'dir (\w+)'

    with open('_input.txt', 'r') as input:
        console = [i for i in input.readlines()]

    fs = Node(None, '/')
    current_node = fs
    level = 0
    for line in console:
        if line[0] == '$':
            if (m := re.search(cd_pattern, line)) != None:
                if m.group(2) == '/':
                    continue
                current_node = current_node.parent if m.group(2) == '..' else current_node.cd(m.group(2))
        else:
            if (m:= re.search(file_pattern, line)) != None:
                new_node = Node(current_node, m.group(2), 'f', int(m.group(1)))
            else:
                m = re.search(dir_pattern, line)
                new_node = Node(current_node, m.group(1))
            
            current_node.children.append(new_node)
    
    print(part_2(fs))
    
