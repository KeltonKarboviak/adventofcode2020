from collections import defaultdict
import re
from dataclasses import dataclass


OUTER_BAG_PATTERN = re.compile(r'(\w+ \w+) bags')
INNER_PATTERN = re.compile(r'(\d+) (\w+ \w+) bags?')


@dataclass(frozen=True, eq=True, order=True)
class Bag(object):
    desc: str


@dataclass(frozen=True, eq=True, order=True)
class Bag2(object):
    desc: str
    qty: int


def main_part1():
    print('\nPart 1:\n')

    with open('day7.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    target_bags = {Bag('shiny gold')}

    inner_to_outer_bags = defaultdict(set)
    for line in lines:
        outer, inner = line.split(' contain ')

        outer_bag = Bag(OUTER_BAG_PATTERN.match(outer).group(1))
        inner_bags = INNER_PATTERN.findall(inner)
        inner_bags = {Bag(b[1]) for b in inner_bags}

        for inner_bag in inner_bags:
            inner_to_outer_bags[inner_bag].add(outer_bag)

    result = set()
    while target_bags:
        target_bag = target_bags.pop()
        result.add(target_bag)
        print('Target:', target_bag)

        outer_bags = inner_to_outer_bags[target_bag]
        print(' -> New Targets:', outer_bags)
        target_bags.update(outer_bags)

    # Subtract 1 since the initial 'shiny gold' bag
    # doesn't count
    print('Answer:', len(result) - 1)


def main_part2():
    print('\nPart 2:\n')

    with open('day7.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    target_bag = Bag2(qty=1, desc='shiny gold')

    outer_to_inner_bags = defaultdict(set)
    for line in lines:
        outer, inner = line.split(' contain ')

        outer_bag = Bag2(qty=1, desc=OUTER_BAG_PATTERN.match(outer).group(1))
        inner_bags = INNER_PATTERN.findall(inner)
        inner_bags = {Bag2(qty=int(b[0]), desc=b[1]) for b in inner_bags}

        outer_to_inner_bags[outer_bag.desc] = inner_bags

    def recursive_inner_sum(b: Bag2):
        inner_bags = outer_to_inner_bags[b.desc]
        return b.qty + (b.qty * sum(recursive_inner_sum(b) for b in inner_bags))

    print('Target:', target_bag)

    total = recursive_inner_sum(target_bag)

    # Subtract 1 since the initial 'shiny gold' bag
    # doesn't count
    print('\nAnswer:', total - 1)


if __name__ == '__main__':
    main_part1()
    main_part2()
