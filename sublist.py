def sublist(a, b):
    """Checks if one list is a subset of another list, i.e. all elements in list a are also in list b.
    Number of times an element occurs in the list is considered."""
    for element in a:
        if element not in b:
            return False
        if a.count(element) > b.count(element):
            return False
    return True