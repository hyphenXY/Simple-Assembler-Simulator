import sys
# code = sys.stdin.read().splitlines()
line_no = 1


def memory():
    global c

    var = bin(c)[2:]
    c += 1
    if(len(var) < 8):
        zeroes = 8-len(var)
        var = '0'*zeroes+var
    return var


def binary(n):
    ans = bin(n)[2:]
    l = len(ans)
    l1 = 8-l
    a1 = '0'*l1
    a1 += ans
    return a1


def Type(strlist):
    if strlist[0] == 'add' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'sub' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'mov' and len(strlist) == 3:
        if strlist[2][0] == '$':
            return 'B'
        else:
            return 'C'
    elif strlist[0] == 'ld' and len(strlist) == 3:
        return 'D'
    elif strlist[0] == 'st' and len(strlist) == 3:
        return 'D'
    elif strlist[0] == 'mul' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'div' and len(strlist) == 3:
        return 'C'
    elif strlist[0] == 'rs' and len(strlist) == 3:
        return 'B'
    elif strlist[0] == 'ls' and len(strlist) == 3:
        return 'B'
    elif strlist[0] == 'xor' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'or' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'and' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'not' and len(strlist) == 3:
        return 'C'
    elif strlist[0] == 'cmp' and len(strlist) == 3:
        return 'C'
    elif strlist[0] == 'jmp' and len(strlist) == 2:
        return 'E'
    elif strlist[0] == 'jlt' and len(strlist) == 2:
        return 'E'
    elif strlist[0] == 'jgt' and len(strlist) == 2:
        return 'E'
    elif strlist[0] == 'je' and len(strlist) == 2:
        return 'E'
    elif strlist[0] == 'hlt' and len(strlist) == 1:
        return 'F'
    elif strlist[0] == 'addf' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'subf' and len(strlist) == 4:
        return 'A'
    elif strlist[0] == 'movf' and len(strlist) == 3:
        return 'B'
    else:
        sys.stdout.write(f'{line_no}: ERROR => Instruction not Defined\n')
        exit()


def typeA(strlist):
    ans = ''

    if strlist[0] == 'add':
        ans += '10000'
    elif strlist[0] == 'sub':
        ans += '10001'
    elif strlist[0] == 'mul':
        ans += '10110'
    elif strlist[0] == 'xor':
        ans += '11010'
    elif strlist[0] == 'or':
        ans += '11011'
    elif strlist[0] == 'and':
        ans += '11100'
    elif strlist[0] == 'addf':
        ans += '00000'
    elif strlist[0] == 'subf':
        ans += '00001'

    ans += '00'

    r1 = strlist[1]

    if r1 == 'R0':
        ans += '000'
    elif r1 == 'R1':
        ans += '001'
    elif r1 == 'R2':
        ans += '010'
    elif r1 == 'R3':
        ans += '011'
    elif r1 == 'R4':
        ans += '100'
    elif r1 == 'R5':
        ans += '101'
    elif r1 == 'R6':
        ans += '110'
    elif r1 == 'FLAGS':
        sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
        exit()
    else:
        sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
        exit()

    r2 = strlist[2]

    if r2 == 'R0':
        ans += '000'
    elif r2 == 'R1':
        ans += '001'
    elif r2 == 'R2':
        ans += '010'
    elif r2 == 'R3':
        ans += '011'
    elif r2 == 'R4':
        ans += '100'
    elif r2 == 'R5':
        ans += '101'
    elif r2 == 'R6':
        ans += '110'
    elif r2 == 'FLAGS':
        sys.stdout.write(f'{line_no}: ERROR =>  Invalid Instruction\n')
        exit()
    else:
        sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
        exit()

    r3 = strlist[3]

    if r3 == 'R0':
        ans += '000'
    elif r3 == 'R1':
        ans += '001'
    elif r3 == 'R2':
        ans += '010'
    elif r3 == 'R3':
        ans += '011'
    elif r3 == 'R4':
        ans += '100'
    elif r3 == 'R5':
        ans += '101'
    elif r3 == 'R6':
        ans += '110'
    elif r3 == 'FLAGS':
        sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
        exit()
    else:
        sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
        exit()

    return ans


def typeB(strlist):
    ans = ''
    if strlist[0] == 'mov':
        ans += '10010'
    elif strlist[0] == 'ls':
        ans += '11001'
    elif strlist[0] == 'rs':
        ans += '11000'
    elif strlist[0] == 'movf':
        ans += '00010'

    r1 = strlist[1]

    if r1 == 'R0':
        ans += '000'
    elif r1 == 'R1':
        ans += '001'
    elif r1 == 'R2':
        ans += '010'
    elif r1 == 'R3':
        ans += '011'
    elif r1 == 'R4':
        ans += '100'
    elif r1 == 'R5':
        ans += '101'
    elif r1 == 'R6':
        ans += '110'
    elif r1 == 'FLAGS':
        sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
        exit()
    else:
        sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
        exit()
    if strlist[0] == 'mov':
        if int(strlist[2][1:]) >= 255 or int(strlist[2][1:]) <= 0:
            sys.stdout.write(
                f'{line_no}: ERROR => Number is not between 0 and 255\n')
            exit()

    if strlist[0] == 'movf':
        if int(strlist[2][1:]) >= 252 or int(strlist[2][1:]) <= 0:
            sys.stdout.write(
                f'{line_no}: ERROR => Number is not between 0 and 255\n')
            exit()

    ans += binary(int(strlist[2][1:]))

    return ans


def typeC(strlist):
    ans = ''
    if strlist[0] == 'mov':
        ans += '10011'
    elif strlist[0] == 'div':
        ans += '10111'
    elif strlist[0] == 'not':
        ans += '11101'
    elif strlist[0] == 'cmp':
        ans += '11110'

    ans += '00000'

    if strlist[1] == 'R0':
        ans += '000'
    elif strlist[1] == 'R1':
        ans += '001'
    elif strlist[1] == 'R2':
        ans += '010'
    elif strlist[1] == 'R3':
        ans += '011'
    elif strlist[1] == 'R4':
        ans += '100'
    elif strlist[1] == 'R5':
        ans += '101'
    elif strlist[1] == 'R6':
        ans += '110'
    elif strlist[1] == 'FLAGS' and strlist[0] == 'mov':
        ans += '111'
    else:
        sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
        exit()

    if strlist[2] == 'R0':
        ans += '000'
    elif strlist[2] == 'R1':
        ans += '001'
    elif strlist[2] == 'R2':
        ans += '010'
    elif strlist[2] == 'R3':
        ans += '011'
    elif strlist[2] == 'R4':
        ans += '100'
    elif strlist[2] == 'R5':
        ans += '101'
    elif strlist[2] == 'R6':
        ans += '110'
    else:
        sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
        exit()

    return ans


def typeD(strlist, mem):
    strD = ''
    if strlist[0] == 'ld':
        strD += '10100'
        r1 = strlist[1]
        if r1 == 'R0':
            strD += '000'
        elif r1 == 'R1':
            strD += '001'
        elif r1 == 'R2':
            strD += '010'
        elif r1 == 'R3':
            strD += '011'
        elif r1 == 'R4':
            strD += '100'
        elif r1 == 'R5':
            strD += '101'
        elif r1 == 'R6':
            strD += '110'
        elif r1 == 'FLAGS' and r1 not in var_arr:
            sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
            exit()
        else:
            sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
            exit()

        strD += mem

    elif strlist[0] == 'st':
        strD += '10101'
        r1 = strlist[1]
        if r1 == 'R0':
            strD += '000'
        elif r1 == 'R1':
            strD += '001'
        elif r1 == 'R2':
            strD += '010'
        elif r1 == 'R3':
            strD += '011'
        elif r1 == 'R4':
            strD += '100'
        elif r1 == 'R5':
            strD += '101'
        elif r1 == 'R6':
            strD += '110'
        elif r1 == 'FLAGS' and r1 not in var_arr:
            sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
            exit()
        else:
            sys.stdout.write(f'{line_no}: ERROR => Register not Defined\n')
            exit()

        strD += mem

    return strD


def typeE(strlist, mem):
    strE = ''
    if strlist[0] == 'jmp' and strlist[1] in label_arr:
        strE += '11111000'
        strE += mem
    elif strlist[0] == 'jlt' and strlist[1] in label_arr:
        strE += '01100000'
        strE += mem
    elif strlist[0] == 'jgt' and strlist[1] in label_arr:
        strE += '01101000'
        strE += mem
    elif strlist[0] == 'je' and strlist[1] in label_arr:
        strE += '01111000'
        strE += mem
    else:
        sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
        exit()

    return strE


def typeF(strlist):
    if strlist[0] != 'hlt':
        sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
        exit()
    strF = '01010' + '0'*11
    return strF


def memory():
    global c
    var = bin(c)[2:]
    c += 1
    if(len(var) < 8):
        zeroes = 8-len(var)
        var = '0'*zeroes+var
    return var


def memory_label():
    global c
    var = bin(c-1)[2:]

    if(len(var) < 8):
        zeroes = 8-len(var)
        var = '0'*zeroes+var
    return var


def take_input():
    global c
    global label_arr
    label_arr = []

    # for line in sys.stdin:
    #     line_arr = [str(x) for x in line[:-1].split(' ')]
    #     input_arr.append(line_arr)

    input_arr_1 = sys.stdin.read().splitlines()

    for line in input_arr_1:
        if line == '':
            input_arr_1.remove(line)

    input_arr = list(x.split() for x in input_arr_1)

    hlt_flag = 0

    for line_arr in input_arr:
        if line_arr[0][-1] == ':':
            if len(line_arr) != 1:
                if line_arr[1] == 'hlt':
                    if hlt_flag == 0:
                        hlt_flag = 1
                    else:
                        sys.stdout.write(
                            f'{input_arr.index(line_arr)+1}: ERROR => Instructions Written after "hlt" Instruction\n')
                        exit()
        else:
            if line_arr[0] == 'hlt':
                if hlt_flag == 0:
                    hlt_flag = 1
                else:
                    sys.stdout.write(
                        f'{input_arr.index(line_arr)+1}: ERROR => Instructions Written after "hlt" Instruction\n')
                    exit()

    for line_arr in input_arr:
        if line_arr[0][-1] == ':':
            if len(line_arr) == 1:
                sys.stdout.write(
                    f'{input_arr.index(line_arr)+1}: ERROR => Invalid Instruction\n')
                exit()

    if input_arr[-1][0][-1] == ':':
        if input_arr[-1][1] != 'hlt':
            sys.stdout.write(
                f'{input_arr.index(line_arr)+1}: ERROR => Missing "hlt" Instruction in Last Line\n')
            exit()
    else:
        if input_arr[-1][0] != 'hlt':
            sys.stdout.write(
                f'{input_arr.index(line_arr)+1}: ERROR => Missing "hlt" Instruction in Last Line\n')
            exit()

    for line_arr in input_arr:
        if line_arr[0][-1] == ':':
            label_arr.append(line_arr[0][:-1])

    for i in range(len(input_arr)):
        if (input_arr[i][0] != 'var'):
            c += 1
        if(input_arr[i][0][-1] == ':'):
            d[input_arr[i][0][:-1]] = memory_label()

    # for x in input_arr:
    #     print(x)
    for i in range(len(input_arr)):
        if(input_arr[i][0] == 'var' and len(input_arr[i]) == 2):
            # d.update(input_arr[i])
            d[input_arr[i][1]] = memory()

    return input_arr


def give_output(input_arr):
    global line_no
    global var_arr

    var_arr = []
    output_arr = []

    var_flag = 0

    for line_arr in input_arr:
        if len(line_arr) > 5:
            sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
            exit()

        if line_arr[0] == 'var':
            if len(line_arr) == 2:
                if var_flag == 0:
                    var_arr.append(line_arr[1])
                else:
                    sys.stdout.write(
                        f'{line_no}: ERROR => Variable Not Declared in Beginning\n')
                    exit()
            else:
                sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
                exit()
        else:
            var_flag = 1

        if line_arr[0] != 'var' and line_arr[0][-1] != ':':
            ins_type = Type(line_arr)
            if ins_type == 'A' and len(line_arr) == 4:
                output_arr.append(typeA(line_arr))
            elif ins_type == 'B' and len(line_arr) == 3:
                output_arr.append(typeB(line_arr))
            elif ins_type == 'C' and len(line_arr) == 3:
                output_arr.append(typeC(line_arr))
            elif ins_type == 'D' and len(line_arr) == 3 and line_arr[2] in var_arr:
                output_arr.append(typeD(line_arr, d[line_arr[2]]))
            elif ins_type == 'E' and len(line_arr) == 2 and line_arr[1] in label_arr:
                output_arr.append(typeE(line_arr, d[line_arr[1]]))
            elif ins_type == 'F' and len(line_arr) == 1:
                output_arr.append(typeF(line_arr))
            else:
                sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
                exit()

        if line_arr[0] != 'var' and line_arr[0][-1] == ':':
            ins_type = Type(line_arr[1:])
            if ins_type == 'A' and len(line_arr) == 5:
                output_arr.append(typeA(line_arr[1:]))
            elif ins_type == 'B' and len(line_arr) == 4:
                output_arr.append(typeB(line_arr[1:]))
            elif ins_type == 'C' and len(line_arr) == 4:
                output_arr.append(typeC(line_arr[1:]))
            elif ins_type == 'D' and len(line_arr) == 4 and line_arr[3] in var_arr:
                output_arr.append(typeD(line_arr[1:], d[line_arr[3]]))
            elif ins_type == 'E' and len(line_arr) == 3 and line_arr[2] in label_arr:
                output_arr.append(typeE(line_arr[1:], d[line_arr[2]]))
            elif ins_type == 'F' and len(line_arr) == 2:
                output_arr.append(typeF(line_arr[1:]))
            else:
                sys.stdout.write(f'{line_no}: ERROR => Invalid Instruction\n')
                exit()

        line_no += 1

    return output_arr


c = 0
global d
d = dict()

input_arr = take_input()

output_arr = give_output(input_arr)

for x in output_arr:
    sys.stdout.write(x)
    sys.stdout.write('\n')
