
def main_part1():
    print('\nPart 1:\n')

    target_sum = 2020

    with open('day1.txt', 'r') as fh:
        numbers = {int(line) for line in fh}

    for x in numbers:
        remaining = target_sum - x
        if remaining in (numbers - {x}):
            y = remaining
            print(f'Found it! x = {x}, y = {y}')
            print(f'Answer: {x * y}')
            break



def main_part2():
    print('\nPart 2:\n')

    target_sum = 2020

    with open('day1.txt', 'r') as fh:
        numbers = {int(line) for line in fh}

    for x in numbers:
        for y in (numbers - {x}):
            remaining = target_sum - x - y
            if remaining in (numbers - {x, y}):
                z = remaining
                print(f'Found it! {x} + {y} + {z} = {x + y + z}')
                print(f'Answer: {x} * {y} * {z} = {x * y * z}')
                break


if __name__ == '__main__':
    main_part1()
    main_part2()
