import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# bst = BinarySearchTree('M')
# for name_1 in names_1:
#     bst.insert(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2):
#         duplicates.append(name_2)

# Stretch solution
duplicates = []
# Loop over names_1, creating arrays with names of the first letter
for name_1 in names_1:
    # Check if array exists
    try:
        vars()[name_1[0]]
    # If it doesn't, create one and add name to it
    except KeyError:
        arr = name_1
        vars()[arr[0]] = [arr]
    # If it does exist, add name to it
    else:
        vars()[name_1[0]].append(name_1)
for name_2 in names_2:
    # Check if array exists
    try:
        vars()[name_2[0]]
    # If it doesn't, ignore and move on
    except KeyError:
        pass
    # If it does, loop over it and if you find duplicate, add to duplicates array
    else:
        for name in vars()[name_2[0]]:
            if name == name_2:
                duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
