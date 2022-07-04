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
    if strlist[0] == 'add':
        return 'A'
    elif strlist[0] == 'sub':
        return 'B'
    elif strlist[0] == 'mov':
        if strlist[2][0] == '$':
            return 'B'
        else:
            return 'C'
    elif strlist[0] == 'ld':
        return 'D'
    elif strlist[0] == 'st':
        return 'D'
    elif strlist[0] == 'mul':
        return 'A'
    elif strlist[0] == 'div':
        return 'C'
    elif strlist[0] == 'rs':
        return 'B'
    elif strlist[0] == 'ls':
        return 'B'
    elif strlist[0] == 'xor':
        return 'A'
    elif strlist[0] == 'or':
        return 'A'
    elif strlist[0] == 'and':
        return 'A'
    elif strlist[0] == 'not':
        return 'C'
    elif strlist[0] == 'cmp':
        return 'C'
    elif strlist[0] == 'jmp':
        return 'E'
    elif strlist[0] == 'jlt':
        return 'E'
    elif strlist[0] == 'jgt':
        return 'E'
    elif strlist[0] == 'je':
        return 'E'
    elif strlist[0] == 'hlt':
        return 'F'
    else:
        print('\nERROR: Instruction not Defined')
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
        ans += '100'
    elif r1 == 'FLAGS':
        print('ERROR: Invalid Instruction')
        exit()
    else:
        print('ERROR: Register not Defined')
        exit()

    r2 = strlist[2]

    if r1 == 'R0':
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
        ans += '100'
    elif r1 == 'FLAGS':
        print('ERROR: Invalid Instruction')
        exit()
    else:
        print('ERROR: Register not Defined')
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
        ans += '100'
    elif r1 == 'FLAGS':
        print('ERROR: Invalid Instruction')
        exit()
    else:
        print('ERROR: Register not Defined')
        exit()

    return ans


def typeB(strlist):
    ans = ''
    if strlist[0] == 'mov':
        ans += '10010'
    elif strlist[0] == 'ls':
        s1 += '11001'
    elif strlist[0] == 'rs':
        ans += '11000'

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
        ans += '100'
    elif r1 == 'FLAGS':
        print('ERROR: Invalid Instruction')
        exit()
    else:
        print('ERROR: Register not Defined')
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
    else:
        print('ERROR: Register not Defined')
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
    elif strlist[2] == 'FLAGS' and strlist[0] == 'mov':
        ans += '111'
    else:
        print('ERROR: Register not Defined')
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
            strD += '100'
        elif r1 == 'FLAGS':
            print('ERROR: Invalid Instruction')
            exit()
        else:
            print('ERROR: Register not Defined')
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
            strD += '100'
        elif r1 == 'FLAGS':
            print('ERROR: Invalid Instruction')
            exit()
        else:
            print('ERROR: Register not Defined')
            exit()

        strD += mem

    return strD


def typeE(strlist, mem):
    strE = ''
    if strlist[0] == 'jmp':
        strE += '11111'
        strE += mem
    elif strlist[0] == 'jlt':
        strE += '01100'
        strE += mem
    elif strlist[0] == 'jgt':
        strE += '01101'
        strE += mem
    elif strlist[0] == 'je':
        strE += '01111'
        strE += mem

    return strE


def typeF():
    strF = '01010' + '0'*11
    return strF
