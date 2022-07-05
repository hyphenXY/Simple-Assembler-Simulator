import sys
from Types import *
c = 0
d = {}


def memory():
    global c
    var = bin(c)[2:]
    c += 1
    if(len(var) < 8):
        zeroes = 8-len(var)
        var = "0"*zeroes+var
    return var


def take_input():
    input_arr = []

    for line in sys.stdin:
        line_arr = [str(x) for x in line[:-1].split(" ")]
        input_arr.append(line_arr)

        line_no = 1
        var_flag = 0

        if len(line_arr) > 5:
            print(f"{line_no}: ERROR => Invalid Instruction")
            exit()

        if len(line_arr) == 2 and line_arr[0] == 'var':
            if var_flag == 1:
                print(f"{line_no}: ERROR => Variable Not Declared in Beginning")
                exit()
        else:
            var_flag = 1

        if line_arr[0] != "var" and line_arr[0][-1] != ':':
            ins_type = Type(line_arr)
            if ins_type == 'A' and len(line_arr) == 4:
                pass
            elif ins_type == 'B' and len(line_arr) == 3:
                pass
            elif ins_type == 'C' and len(line_arr) == 3:
                pass
            elif ins_type == 'D' and len(line_arr) == 3:
                pass
            elif ins_type == 'E' and len(line_arr) == 2:
                pass
            elif ins_type == 'F' and len(line_arr) == 1:
                pass
            else:
                print(f"{line_no}: ERROR => Invalid Instruction")
                exit()

        if line_arr[0][-1] == ':':
            ins_type = Type(line_arr[1:])
            if ins_type == 'A' and len(line_arr) == 5:
                pass
            elif ins_type == 'B' and len(line_arr) == 4:
                pass
            elif ins_type == 'C' and len(line_arr) == 4:
                pass
            elif ins_type == 'D' and len(line_arr) == 4:
                pass
            elif ins_type == 'E' and len(line_arr) == 3:
                pass
            elif ins_type == 'F' and len(line_arr) == 1:
                pass
            else:
                print(f"{line_no}: ERROR => Invalid Instruction")
                exit()

        line_no += 1

        if line == 'hlt':
            break

    for i in range(len(input_arr)):
        if(input_arr[i].split()[0] == "var"):
            d[input_arr[i].split()[1]] = memory()

    return input_arr


def give_output(input_arr):
    var_arr = []
    label_arr = []
    output_arr = []

    var_flag = 0

    for line_arr in input_arr:
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
