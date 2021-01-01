from itertools import combinations
from typing import Iterable


def main_part1():
    print('\nPart 1:\n')

    with open('day9.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    numbers = [int(line) for line in lines]
    # preamble = 5
    preamble = 25

    for idx, n in enumerate(numbers[preamble:], start=preamble):
        previous_nums = numbers[idx-preamble:idx]

        print(idx, n)

        all_pairs = combinations(previous_nums, r=2)
        sums_of_pairs = map(sum, all_pairs)

        if not any (s == n for s in sums_of_pairs):
            print(' -> Broke the rule!')
            break

    print(f'\nAnswer: idx={idx}, num={n}')


def main_part2():
    print('\nPart 2:\n')

    with open('day9.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    numbers = [int(line) for line in lines]
    # preamble = 5
    preamble = 25

    for idx, n in enumerate(numbers[preamble:], start=preamble):
        previous_nums = numbers[idx-preamble:idx]

        print(idx, n)

        all_pairs = combinations(previous_nums, r=2)
        sums_of_pairs = map(sum, all_pairs)

        if not any (s == n for s in sums_of_pairs):
            print(' -> Broke the rule!')
            break

    for subset_length in range(2, len(numbers)):
        for starting_idx in range(len(numbers) - subset_length):
            subset = numbers[starting_idx : starting_idx+subset_length]

            if subset_sum_equals_target(subset, n):
                sorted_subset = sorted(subset)
                min_num, max_num = sorted_subset[0], sorted_subset[-1]
                print(f' -> subset={subset}, min={min_num}, max={max_num}')
                print(f' -> min/max sum={min_num + max_num}')

    print(f'\nAnswer: idx={idx}, num={n}')


def subset_sum_equals_target(subset: Iterable[int], target: int) -> bool:
    return sum(subset) == target


if __name__ == '__main__':
    main_part1()
    main_part2()
