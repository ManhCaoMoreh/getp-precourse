def build_level_cols(root, level, margin, lefts, rights, level_cols):
    num_node = 1
    root_col = margin + 1

    if root in lefts:
        left_num_node = build_level_cols(
            lefts[root], level + 1, margin, lefts, rights, level_cols
        )
        root_col = left_num_node + margin + 1
        num_node += left_num_node

    if level not in level_cols:
        level_cols[level] = []

    level_cols[level].append(root_col)

    if root in rights:
        right_num_node = build_level_cols(
            rights[root], level + 1, root_col, lefts, rights, level_cols
        )
        num_node += right_num_node

    return num_node


def width_of_binary_tree(root, lefts, rights):
    """
    Calculate the widest level and the width of that level
    =================================================================================================
    Arguments:
        + args: something containing information about the input binary tree
    Outputs:
        + widest_level: widest level of given binary tree
        + max_width: widht of the widest level of given binary tree
    """

    level_cols = {}
    build_level_cols(1, 1, 0, lefts, rights, level_cols)

    widest_level, max_width = (0, 0)

    for level in level_cols:
        level_max_width = 0
        if len(level_cols[level]) == 1:
            level_max_width = 1
        else:
            for index in range(1, len(level_cols[level])):
                level_max_width = max(
                    level_max_width,
                    level_cols[level][index] - level_cols[level][index - 1] + 1,
                )
        if max_width < level_max_width:
            max_width = level_max_width
            widest_level = level

    return widest_level, max_width


def main():
    with open("input.txt", "r") as file:
        n = int(file.readline())
        lines = file.readlines()
        lefts = {}
        rights = {}
        for line in lines:
            line = line.strip().split()
            p, u, v = int(line[0]), int(line[1]), int(line[2])
            if u != -1:
                lefts[p] = u
            if v != -1:
                rights[p] = v

    output = width_of_binary_tree(1, lefts, rights)

    with open("output.txt", "w") as f:
        f.write(f"{output[0]} {output[1]}\n")


if __name__ == "__main__":
    main()
