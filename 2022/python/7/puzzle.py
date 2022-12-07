from common import iterate_input_lines

class File:
    def __init__(self, name, size):
        self.name: str = name
        self.size: int = size

class Directory:
    name: str
    directories: ['Directory']
    files: [File]
    parent: 'Directory'

    def __init__(self, name):
        self.name = name
        self.directories = []
        self.files = []
        self.parent: Directory = None

    def add_directory(self, directory):
        directory.parent = self
        self.directories += [directory]

    def add_file(self, file):
        self.files += [file]

    @property
    def size(self):
        dir_size = sum([directory.size for directory in self.directories])
        file_size = sum([f.size for f in self.files])
        return dir_size + file_size

    def __str__(self):
        return f"{self.name}, size: {'{:,}'.format(self.size)}"

    def path(self):
        return self.parent.path().rstrip("/") + "/" + self.name if self.parent else self.name


class FileSystem:
    def __init__(self):
        self.root = Directory(name="/")
        self.cur_dir: Directory = self.root

    def cd(self, arg):
        if arg == "/":
            self.cur_dir = self.root
        elif arg == "..":
            self.cur_dir = self.cur_dir.parent
        else:
            for child in self.cur_dir.directories:
                if child.name == arg:
                    self.cur_dir = child
                    break
    def ls(self):
        def print_ls(directory, prefix):
            print(f"{prefix}- {directory.name} (dir, size={'{:,}'.format(directory.size)})")
            children = sorted(directory.files + directory.directories, key=lambda x: x.name)
            for child in children:
                if type(child) == File:
                    print(f"{prefix}  - {child.name} (file, size={'{:,}'.format(child.size)})")
                else:
                    print_ls(child, f"{prefix}  ")
        print_ls(self.cur_dir, "")


def parse_input(case) -> FileSystem:
    fs = FileSystem()
    for line in iterate_input_lines(case):
        if line.startswith("$"):
            # this is a command
            parts = line.split(" ")
            if parts[1] == "cd":
                fs.cd(parts[2])
        else:
            # this is output
            parts = line.split(" ")
            if parts[0] == "dir":
                fs.cur_dir.add_directory(Directory(parts[1]))
            else:
                fs.cur_dir.add_file(File(parts[1], int(parts[0])))
    fs.cd("/")
    return fs



def get_directories_of_maxsize(given_dir: Directory, max_size: int):
    found_directories = []
    for directory in given_dir.directories:
        if directory.size <= max_size:
            found_directories += [directory]
        if directory.directories:
            found_directories += get_directories_of_maxsize(directory, max_size)
    return found_directories


def get_directories_of_minsize(given_dir: Directory, min_size: int):
    found_directories = []
    if given_dir.size >= min_size:
        found_directories += [given_dir]
    for directory in given_dir.directories:
        if directory.directories:
            found_directories += get_directories_of_minsize(directory, min_size)
    return found_directories


def solve(case) -> int:
    fs = parse_input(case)
    dirs = get_directories_of_maxsize(fs.cur_dir, 100000)
    return sum([d.size for d in dirs])

def solve_part2(case):
    fs = parse_input(case)
    max_used = 70000000 - 30000000
    total_used = fs.root.size
    need_to_free = total_used - max_used
    dirs = get_directories_of_minsize(fs.cur_dir, need_to_free)
    for d in dirs:
        print(d.path(), '{:,}'.format(d.size))
    dir_to_remove: Directory = min(dirs,key=lambda d: d.size)
    return dir_to_remove.size


if __name__ == '__main__':
    print(solve_part2("input.txt"))
    # fs = parse_input("input.txt")
    # fs.ls()