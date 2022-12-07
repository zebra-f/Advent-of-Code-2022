with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip().split(" ") for line in lines]


class DirNode:
    def __init__(self, name, prev=None):
        self.name = name
        self.files = []
        self.prev = prev
        self.sub_dirs = dict()


class FilesystemTree:
    def __init__(self):
        self.root = DirNode('root')
    
    def mkdir(self, name, prev):
        dir = DirNode(name, prev)
        return dir

    def build_filesystem_tree(self, lines):
        
        def build(curr_dir, lines):
            if lines[0][0] == '$':
                i = 0
                if lines[i][1] == 'ls':
                    i = 1
                    while i < len(lines) and (lines[i][0].isnumeric() or lines[i][0] == 'dir'):
                        if lines[i][0] == 'dir':
                            curr_dir.sub_dirs[lines[i][1]] = self.mkdir(lines[i][1], curr_dir)
                        else:
                            curr_dir.files.append(lines[i])
                        i += 1
                                      
                if i < len(lines):
                    if lines[i][2] == '/':
                        build(self.root, [*lines[i+1:]])
                    elif lines[i][2] == '..':
                        prev_directory = curr_dir.prev
                        build(prev_directory, [*lines[i+1:]])
                    else:
                        next_directory = curr_dir.sub_dirs[lines[i][2]]
                        next_directory.prev = curr_dir
                        build(next_directory, [*lines[i+1:]])
            else:
                raise Exception("Wrong input!")

        build(self.root, lines[1:])
        return self.root


file_system = FilesystemTree()
root = file_system.build_filesystem_tree(lines)


class DaySeven:
    def __init__(self, root):
        self.part_one_answer = 0
        self.total_filesize = self.part_one(root)
        self.size_to_remove = 30000000 - (70000000 - self.total_filesize)
    
        self.dirs_to_remove = []
        self.part_two(root)
        self.part_two_answer = min(self.dirs_to_remove)

    def part_one(self, root):
        filesize = 0

        for file in root.files:
            filesize += int(file[0])

        for dir in root.sub_dirs.values():
            filesize += self.part_one(dir)
        
        if filesize <= 100000:
            self.part_one_answer += filesize 
        return filesize

    def part_two(self, root):
        filesize = 0

        for file in root.files:
            filesize += int(file[0])

        for dir in root.sub_dirs.values():
            filesize += self.part_two(dir)
        
        if filesize >= self.size_to_remove:
            self.dirs_to_remove.append(filesize)
        
        return filesize


day_seven = DaySeven(root)

