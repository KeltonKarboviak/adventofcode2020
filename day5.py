def main_part1():
    print('\nPart 1:\n')

    numrows = 128
    numcolumns = 8

    with open('day5.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    seat_ids = []
    for line in lines:
        row_codes = line[:7]
        col_codes = line[-3:]

        print(row_codes, col_codes)

        print('\nFinding row')
        rows = range(numrows)
        for code in row_codes:
            print(code, end='')

            if 'F' == code:
                # keep lower half
                rows = rows[:len(rows) // 2]
            else:
                # keep upper half
                rows = rows[len(rows) // 2:]

            print(' ->', rows)

        row = rows.start

        print('\nFinding column')
        cols = range(numcolumns)
        for code in col_codes:
            print(code, end='')

            if 'L' == code:
                # keep lower half
                cols = cols[:len(cols) // 2]
            else:
                # keep upper half
                cols = cols[len(cols) // 2:]

            print(' ->', cols)

        column = cols.start

        seat_id = row * 8 + column
        seat_ids.append(seat_id)

        print(f'\nAnswer: {row} * 8 + {column} = {seat_id}')

    sorted_ids = sorted(seat_ids)

    print('\nAnswer:', sorted_ids[-1])


    print('\nPart 2:\n')

    all_possible_seat_ids = set(range(sorted_ids[0], sorted_ids[-1]+1))
    print('\nAnswer:', all_possible_seat_ids - set(sorted_ids))


# def main_part2():
#     print('\nPart 2:\n')

#     numrows = 128
#     numcolumns = 8

#     with open('day5.txt', 'r') as fh:
#         lines = fh.readlines()

#     line = 'FBFBBFFRLR'

#     row_codes = line[:7]
#     col_codes = line[-3:]

#     print(row_codes, col_codes)

#     row = 0
#     column = 0
#     seat_id = row * 8 + column

#     print(f'\nAnswer: {row} * 8 + {column} = {seat_id}')


if __name__ == '__main__':
    main_part1()
    # main_part2()
