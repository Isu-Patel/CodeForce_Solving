import sys

roots = {}

for line in sys.stdin:
    path = line.strip()
    if not path:
        continue

    parts = path.split('\\')
    disk = parts[0]

    if disk not in roots:
        roots[disk] = [{}, 0]

    node = roots[disk]

    for folder in parts[1:-1]:
        children = node[0]

        if folder not in children:
            children[folder] = [{}, 0]

        node = children[folder]

    node[1] += 1


max_folders = 0
max_files = 0


def dfs(node):
    global max_folders, max_files

    children, direct_files = node

    total_folders = len(children)
    total_files = direct_files

    for child in children.values():
        subfolders, subfiles = dfs(child)
        total_folders += subfolders
        total_files += subfiles

    max_folders = max(max_folders, total_folders)
    max_files = max(max_files, total_files)

    return total_folders, total_files

for root in roots.values():
    for folder in root[0].values():
        dfs(folder)

print(max_folders, max_files)
