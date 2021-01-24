import sys

# The challenge: https://gist.github.com/1Computer1/3aaffc20f65c2bf736bf60c7c78fe90d
def check_deps(task):
    """Returns True if the given task will execute based on the dependency tree, False if not."""
    dep_combinations = dep_tree[task]
    # Holds booleans indicating if a particular combo of dependencies is met
    res = []
    # If no possible dependencies
    if not dep_combinations:
        return False
    # Check each possible combination of dependencies
    for combo in dep_combinations:
        # Count to hold number of met dependencies from combo
        counter = 0
        for task in combo:
            if task in reqs or check_deps(task):
                counter += 1
        # If number of met dependencies is less than the number of needed dependencies
        if counter < len(combo):
            res.append(False)
        elif counter == len(combo):
            res.append(True)
    # If any combo of dependencies is met, return True
    return True in res

filename = sys.argv[1]
file = open(filename)
number_of_reqs = int(file.readline().strip())
number_of_extras = int(file.readline().strip())
number_of_deps = int(file.readline().strip())

reqs = []
extras = []
deps = []

for i in range(1,number_of_reqs+1):
    reqs.append(file.readline().strip())

for i in range(1, number_of_extras+1):
    extras.append(file.readline().strip())

for i in range(1, number_of_deps+1):
    deps.append(file.readline().strip())

dep_tree = {k: [] for k in extras}

# Add dependencies for each extra task
for line in deps:
    # Process dependency lines into separate tasks
    # split returns a list of string before delimiter and string after, the d1,d2 syntax
    # will do the same as
    # d1 = line.split('->')[0]
    # d2 = line.split('->')[1]
    d1, d2 = line.split('->')
    d1 = [element.strip() for element in d1.split(',')]
    d2 = [element.strip() for element in d2.split(',')]
    for k in d2:
        dep_tree[k].append(d1)
for k,v in dep_tree.items():
    print(f'{k}: {v}')
for task in reqs:
    print(task)
for k in dep_tree.keys():
    if check_deps(k):
        print(k)