def TreeConsuctor(str):
    parent_count = {}
    child_set = set()
    for pair in str:
        pair = pair.strip("()")
        child, parent = map(int , pair.split(','))

        if child in child_set:
            return False
        child_set.add(child)

        if parent in parent_count:
            if parent_count[parent] == 2:
                return False
            parent_count[parent] += 1
        else:
            parent_count[parent] = 1
    return True