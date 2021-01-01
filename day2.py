import re


pattern = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')


def main_part1():
    def is_valid_line(line):
        match = pattern.match(line)
        lowerbound = int(match.group(1))
        upperbound = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)

        return is_password_valid(lowerbound, upperbound, letter, password)

    def is_password_valid(lowerbound, upperbound, letter, password):
        return lowerbound <= password.count(letter) <= upperbound

    print('\nPart 1:\n')

    with open('day2.txt', 'r') as fh:
        lines = [line for line in fh]

    valid_lines = (line for line in lines if is_valid_line(line))
    valid_count = sum(1 for _ in valid_lines)

    print('\nAnswer:', valid_count)



def main_part2():
    def is_valid_line(line):
        match = pattern.match(line)
        pos1 = int(match.group(1))
        pos2 = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)

        return is_password_valid(pos1, pos2, letter, password)

    def is_password_valid(pos1, pos2, letter, password):
        return (letter == password[pos1-1]) ^ (letter == password[pos2-1])

    print('\nPart 2:\n')

    with open('day2.txt', 'r') as fh:
        lines = [line for line in fh]

    valid_lines = (line for line in lines if is_valid_line(line))
    valid_count = sum(1 for _ in valid_lines)

    print('\nAnswer:', valid_count)


if __name__ == '__main__':
    main_part1()
    main_part2()
