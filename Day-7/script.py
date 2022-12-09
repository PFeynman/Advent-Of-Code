import re

class Node:
    def __init__(self, parent, name, size = 0):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = size
    
    def __str__(self) -> str:
        return f'{self.name} {self.actual_size()}'
    
    def cd(self, dir_name):
        if dir_name == self.name:
            return self
        for x in self.children:
            if x.name == dir_name:
                return x
    
    def actual_size(self):
        if self.size != 0:
            return self.size
        else:
            children_size = 0
            for child in self.children:
                children_size += child.actual_size()
            return children_size

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
                current_dir = current_dir.parent if m.group(2) == '..' else current_dir.cd(m.group(2))
        else:
            if (m:= re.search(file_pattern, line)) is not None:
                new_node = Node(current_dir, m.group(2), int(m.group(1)))
            else:
                m = re.search(dir_pattern, line)
                new_node = Node(current_dir, m.group(1))
            current_dir.children.append(new_node)
