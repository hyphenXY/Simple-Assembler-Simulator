import sys
from Types import *
c = 0
mem = '00000101'


def take_input():
    input_arr = []

    for line in sys.stdin:
        line_arr = [str(x) for x in line.split(" ")]
        input_arr.append(line_arr)

        if line.strip() == 'hlt':
            break

    return input_arr


def give_output(input_arr):
    for line_arr in input_arr:
        var_arr = []
        label_arr = []
        output_arr = []

        line_no = 1
        var_flag = 0

        if len(line_arr) > 5:
            print("'ERROR: Invalid Instruction'")
            exit()

        if len(line_arr) == 2 and line_arr[0] == 'var':
            if var_flag == 0:
                var_arr.append(line_arr[1])
            else:
                print("ERROR: Variable Not Declared in Beginning")
                exit()
        else:
            var_flag = 1

        if line_arr[0][-1] == ':':
            label_arr.append(line_arr[0][:-1])

        if line_arr[0] != "var" and line_arr[0][-1] != ':':
            ins_type = Type(line_arr)
            if ins_type == 'A' and len(line_arr) == 4:
                output_arr.append(typeA(line_arr))
            elif ins_type == 'B' and len(line_arr) == 3:
                output_arr.append(typeB(line_arr))
            elif ins_type == 'C' and len(line_arr) == 3:
                output_arr.append(typeC(line_arr))
            elif ins_type == 'D' and len(line_arr) == 3:
                output_arr.append(typeD(line_arr, memory()))
            elif ins_type == 'E' and len(line_arr) == 2:
                output_arr.append(typeE(line_arr, memory()))
            elif ins_type == 'F' and len(line_arr) == 1:
                output_arr.append(typeF())
            else:
                print("ERROR: Invalid Instruction")
                exit()

        if line_arr[0][-1] == ':':
            ins_type = Type(line_arr[1:])
            if ins_type == 'A' and len(line_arr) == 5:
                output_arr.append(typeA(line_arr[1:]))
            elif ins_type == 'B' and len(line_arr) == 4:
                output_arr.append(typeB(line_arr[1:]))
            elif ins_type == 'C' and len(line_arr) == 4:
                output_arr.append(typeC(line_arr[1:]))
            elif ins_type == 'D' and len(line_arr) == 4:
                output_arr.append(typeD(line_arr[1:], memory()))
            elif ins_type == 'E' and len(line_arr) == 3:
                output_arr.append(typeE(line_arr[1:], memory()))
            elif ins_type == 'F' and len(line_arr) == 1:
                output_arr.append(typeF())
            else:
                print("ERROR: Invalid Instruction")
                exit()

        line_no += 1

    return output_arr


input_arr = take_input()

output_arr = give_output(input_arr)

for x in output_arr:
    print(x)
