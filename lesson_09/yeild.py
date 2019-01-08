import os

def get_files(folder):
    for item in os.listdir(folder):

        full_item = os.path.join(folder, item)
        if os.path.isfile(full_item):
            yield full_item
        elif os.path.isdir(full_item):
            yield from get_files(full_item)

for p in get_files('..'):
    print(p)