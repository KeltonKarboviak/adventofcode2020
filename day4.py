import re


"""
* byr (Birth Year)
* iyr (Issue Year)
* eyr (Expiration Year)
* hgt (Height)
* hcl (Hair Color)
* ecl (Eye Color)
* pid (Passport ID)
* cid (Country ID)
"""


fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid',
}

required_fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}


def read_batches(lines):
    batch = []
    for line in lines:
        if not line.strip():
            # flatten batch so we get a list
            # of the key:value pairs
            yield _flatten_batch_of_lines(batch)
            batch = []
        else:
            batch.append(line.strip())

    if batch:
        yield _flatten_batch_of_lines(batch)


def _flatten_batch_of_lines(batch):
    return [
        kv
        for l in batch
        for kv in l.split()
    ]


def validate_byr(passport):
    return 1920 <= int(passport['byr']) <= 2002


def validate_iyr(passport):
    return 2010 <= int(passport['iyr']) <= 2020


def validate_eyr(passport):
    return 2020 <= int(passport['eyr']) <= 2030


def validate_hgt(passport):
    hgt = passport['hgt']

    if hgt.endswith('cm'):
        hgt = int(_strip_suffix(hgt, 'cm'))
        return 150 <= hgt <= 193
    if hgt.endswith('in'):
        hgt = int(_strip_suffix(hgt, 'in'))
        return 59 <= hgt <= 76

    return False


def validate_hcl(passport):
    return bool(re.match(r'^#[a-f0-9]{6}$', passport['hcl']))


def validate_ecl(passport):
    colors = {
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    }
    return passport['ecl'] in colors


def validate_pid(passport):
    return bool(re.match(r'^[0-9]{9}$', passport['pid']))
    # return len(passport['pid']) == 9 and passport['pid'].isdigit()


def validate_cid(passport):
    return True


def _strip_suffix(string, suffix):
    return string[:len(string) - len(suffix)]


def main_part1():
    print('\nPart 1:\n')

    with open('day4.txt', 'r') as fh:
        batches = tuple(read_batches(fh))

    valid_count = 0
    for batch in batches:
        # create a dict from the key:value pairs
        d = dict(kv.split(':') for kv in batch)

        missing_fields = required_fields - set(d)
        if not missing_fields:
            valid_count += 1

    print('\nAnswer:', valid_count)



def main_part2():
    print('\nPart 2:\n')

    validations = [
        validate_byr,
        validate_iyr,
        validate_eyr,
        validate_hgt,
        validate_hcl,
        validate_ecl,
        validate_pid,
        validate_cid,
    ]

    with open('day4.txt', 'r') as fh:
        batches = tuple(read_batches(fh))

    valid_count = 0
    for batch in batches:
        # create a dict from the key:value pairs
        d = dict(kv.split(':') for kv in batch)

        print(d, end=' ')
        missing_fields = required_fields - set(d)
        if (
            not missing_fields
            and all(func(d) for func in validations)
        ):
            valid_count += 1
            print(True)
        else:
            print(False)

    print('\nAnswer:', valid_count)


if __name__ == '__main__':
    main_part1()
    main_part2()
