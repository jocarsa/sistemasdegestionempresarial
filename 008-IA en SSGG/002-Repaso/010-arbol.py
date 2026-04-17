import os
import sys

def print_tree(path, prefix=""):
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(prefix + "[Permission denied]")
        return

    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = i == len(items) - 1

        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)

        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            print_tree(full_path, prefix + extension)

# Get folder from command line
if len(sys.argv) < 2:
    print("Usage: python tree.py <folder>")
    sys.exit(1)

root = sys.argv[1]

if os.path.isdir(root):
    print(root)
    print_tree(root)
else:
    print("Invalid folder")