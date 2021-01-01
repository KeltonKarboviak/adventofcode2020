from dataclasses import dataclass, replace
from functools import reduce


@dataclass
class Pos(object):
    x: int
    y: int


def are_we_at_bottom(grid, pos):
    return pos.y >= len(grid) - 1


def move_position(grid, pos, increment):
    grid_width = len(grid[0])
    new_x, new_y = pos.x+increment[0], pos.y+increment[1]

    if new_x >= grid_width:
        # We've reached the right edge of the graph
        # need to wrap back around to the beginning
        new_x = new_x - grid_width

    return replace(pos, x=new_x, y=new_y)


def get_grid_char(grid, pos):
    return grid[pos.y][pos.x]


def is_tree(grid, pos):
    return is_tree_char(get_grid_char(grid, pos))


def is_tree_char(char):
    return '#' == char


def main_part1():
    print('\nPart 1:\n')

    with open('day3.txt', 'r') as fh:
        grid = [line.strip() for line in fh]

    increment = (3, 1)
    pos = Pos(0, 0)

    tree_count = 0
    while not are_we_at_bottom(grid, pos):
        pos = move_position(grid, pos, increment)
        char = get_grid_char(grid, pos)

        print(char)
        if is_tree_char(char):
            tree_count += 1

    print('\nAnswer:', tree_count)



def main_part2():
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    print('\nPart 2:\n')

    increments = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    with open('day3.txt', 'r') as fh:
        grid = [line.strip() for line in fh]

    tree_counts = []
    for increment in increments:
        print(f'\nRunning for increment:', increment)
        pos = Pos(0, 0)

        tree_count = 0
        while not are_we_at_bottom(grid, pos):
            pos = move_position(grid, pos, increment)
            char = get_grid_char(grid, pos)

            # print(char)
            if is_tree_char(char):
                tree_count += 1

        tree_counts.append(tree_count)
        print('\nAnswer:', tree_count)

    print('\nTree Counts:', tree_counts)
    print('Final Answer:', reduce(lambda x, y: x * y, tree_counts))


if __name__ == '__main__':
    main_part1()
    main_part2()
