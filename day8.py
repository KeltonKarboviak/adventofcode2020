from enum import Enum
from dataclasses import dataclass


class OpCode(str, Enum):
    ACC = 'acc'
    JMP = 'jmp'
    NOP = 'nop'


@dataclass
class Instruction(object):
    operation: OpCode
    argument: int
    has_run: bool = False


def reset_instructions(instructions):
    for ins in instructions:
        ins.has_run = False


def main_part1():
    print('\nPart 1:\n')

    with open('day8.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    instructions = []
    for line in lines:
        op_i = line.split(' ', maxsplit=1)
        op, i = OpCode(op_i[0]), int(op_i[1])
        instructions.append(Instruction(operation=op, argument=i))

    accumulator = 0
    idx = 0
    instruction: Instruction = instructions[idx]

    try:
        while not instruction.has_run:
            print(f'Processing #{idx}: {instruction}')

            idx_inc = 1
            if OpCode.ACC == instruction.operation:
                accumulator += instruction.argument
            elif OpCode.JMP == instruction.operation:
                idx_inc = instruction.argument

            idx += idx_inc
            instruction.has_run = True

            print(' -> acc:', accumulator)
            instruction = instructions[idx]
    except IndexError:
        print('\nProgram terminated!')
    else:
        print('\nProgram DID NOT terminate!')

    print(f'Answer: idx={idx}, acc={accumulator}')


def main_part2():
    print('\nPart 2:\n')

    with open('day8.txt', 'r') as fh:
        lines = [line.strip() for line in fh]

    instructions = []
    for line in lines:
        op_i = line.split(' ', maxsplit=1)
        op, i = OpCode(op_i[0]), int(op_i[1])
        instructions.append(Instruction(operation=op, argument=i))

    idx, accumulator = -1, -1
    mutate_instruction: Instruction
    for i, mutate_instruction in enumerate(instructions):
        if OpCode.ACC == mutate_instruction.operation:
            continue

        old_op = mutate_instruction.operation
        if OpCode.JMP == mutate_instruction.operation:
            print(f'\n#{i} Switching from jmp -> nop')
            mutate_instruction.operation = OpCode.NOP
        elif OpCode.NOP == mutate_instruction.operation:
            print(f'\n#{i} Switching from nop -> jmp')
            mutate_instruction.operation = OpCode.JMP

        accumulator = 0
        idx = 0
        instruction: Instruction = instructions[idx]
        try:
            while not instruction.has_run:
                print(f'Processing #{idx}: {instruction}')

                idx_inc = 1
                if OpCode.ACC == instruction.operation:
                    accumulator += instruction.argument
                elif OpCode.JMP == instruction.operation:
                    idx_inc = instruction.argument

                idx += idx_inc
                instruction.has_run = True

                print(' -> acc:', accumulator)
                instruction = instructions[idx]
        except IndexError:
            print('\nProgram terminated!')
            # break out of mutation loop since the
            # program successfully terminated
            break
        else:
            print('\nProgram DID NOT terminate!')

        print(f'Simulation Answer: idx={idx}, acc={accumulator}')

        mutate_instruction.operation = old_op
        reset_instructions(instructions)

    print(f'Answer: idx={idx}, acc={accumulator}')


if __name__ == '__main__':
    main_part1()
    main_part2()
