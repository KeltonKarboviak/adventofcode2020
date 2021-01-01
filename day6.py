def read_groups(lines):
    batch = []
    for line in lines:
        line = line.strip()
        if not line:
            # flatten batch so we get a list
            # of the key:value pairs
            yield batch
            batch = []
        else:
            batch.append(line)

    if batch:
        yield batch


def main_part1():
    print('\nPart 1:\n')

    with open('day6.txt', 'r') as fh:
        groups = list(read_groups(fh))

    counts = []
    for group in groups:
        anyone_yes_answers = {
            answer
            for person in group
            for answer in person
        }
        print(anyone_yes_answers)

        counts.append(len(anyone_yes_answers))

    print('\nAnswer:', sum(counts))


def main_part2():
    print('\nPart 2:\n')

    with open('day6.txt', 'r') as fh:
        groups = list(read_groups(fh))

    counts = []
    for group in groups:
        everyone_yes_answers = set(group[0])
        for person in group[1:]:
            everyone_yes_answers.intersection_update(set(person))

        print(everyone_yes_answers)
        counts.append(len(everyone_yes_answers))

    print('\nAnswer:', sum(counts))


if __name__ == '__main__':
    main_part1()
    main_part2()
