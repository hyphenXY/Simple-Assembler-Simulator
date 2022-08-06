import sys
import matplotlib.pyplot as graph

def decimal(num):
    pwr = 0
    ans = 0
    for i in num[::-1]:
        ans = ans+(int(i)*(2**pwr))
        pwr += 1
    return ans


def Addition(pc, ins):
    global d

    d[ins[13:16]] = d[ins[7:10]]+d[ins[10:13]]
    r = bin(d[ins[13:16]])[2:]
    if(len(r) > 16):
        d[ins[13:16]] = d[ins[13:16]] % (2**16)
        d['111'] = '0'*12+'1000'
    else:
        d['111'] = '0'*16
    pc += 1ls

    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def Subtraction(pc, ins):
    global d
    if (d[ins[10:13]] > d[ins[7:10]]):
        d[ins[13:16]] = 0
        d['111'] = '0'*12+'1000'
        pc += 1
        lst = [pc, d['000'], d['001'], d['010'], d['011'],
               d['100'], d['101'], d['110'], d['111']]
        return lst
    d[ins[13:16]] = d[ins[7:10]]-d[ins[10:13]]
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def mov_imm(pc, ins):
    global d
    d[ins[5:8]] = decimal(ins[8:])
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def mov_reg(pc, ins):
    global d
    d[ins[10:13]] = d[ins[13:16]]
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def load(pc, ins):
    global d
    keys = list(d.keys())
    if(ins[8:] not in keys):
        d[ins[8:]] = 0
    d[ins[5:8]] = d[ins[8:]]
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def store(pc, ins):
    global d
    d[ins[8:]] = d[ins[5:8]]
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def multiply(pc, ins):
    global d
    d[ins[13:16]] = d[ins[7:10]]*d[ins[10:13]]
    r = bin(d[ins[13:16]])[2:]
    if(len(r) > 16):
        d['111'] = '0'*12+'1000'
    else:
        d['111'] = '0'*16
    pc += 1

    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def divide(pc, ins):
    global d
    d['000'] = d[ins[10:13]]//d[ins[13:16]]
    d['001'] = d[ins[10:13]] % d[ins[13:16]]
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def rshift(pc, ins):
    global d
    d[ins[5:8]] = d[ins[5:8]]//(2**decimal(ins[8:]))
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def lshift(pc, ins):
    global d
    d[ins[5:8]] = d[ins[5:8]]*(2**decimal(ins[8:]))
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def xor(pc, ins):
    global d
    a = ''
    b = bin(d[ins[7:10]])[2:]
    b = '0'*(16-len(b))+b
    c = bin(d[ins[10:13]])[2:]
    c = '0'*(16-len(c))+c
    for i in range(16):
        if(b[i] == '0' and c[i] == '1'):
            a += '1'
        if(b[i] == '1' and c[i] == '0'):
            a += '1'
        else:
            a += '0'
    d[ins[13:16]] = decimal(a)

    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def Or(pc, ins):
    global d
    a = ''
    b = bin(d[ins[7:10]])[2:]
    b = '0'*(16-len(b))+b
    c = bin(d[ins[10:13]])[2:]
    c = '0'*(16-len(c))+c
    for i in range(16):
        if(b[i] == '0' and c[i] == '0'):
            a += '0'
        else:
            a += '1'
    d[ins[13:16]] = decimal(a)
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def And(pc, ins):
    global d
    a = ''
    b = bin(d[ins[7:10]])[2:]
    b = '0'*(16-len(b))+b
    c = bin(d[ins[10:13]])[2:]
    c = '0'*(16-len(c))+c
    for i in range(16):
        if(b[i] == '1' and c[i] == '1'):
            a += '1'
        else:
            a += '0'
    d[ins[13:16]] = decimal(a)
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def invert(pc, ins):
    global d
    a = bin(d[ins[10:13]])[2:]
    a = '0'*(16-len(a))+a
    b = ''
    for i in a:
        if i == '1':
            b += '0'
        else:
            b += '1'
    d[ins[13:]] = decimal(b)
    d['111'] = '0'*16
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def Compares(pc, ins):
    global d
    if (d[ins[10:13]] < d[ins[13:16]]):
        d['111'] = '0'*12+'0100'
    elif (d[ins[10:13]] > d[ins[13:16]]):
        d['111'] = '0'*12+'0010'
    elif (d[ins[10:13]] == d[ins[13:16]]):
        d['111'] = '0'*12+'0001'
    pc += 1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def unconditional(pc, ins):
    global d
    pc = decimal(ins[8:])
    d['111'] = '0'*16
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def jmp_ifLT(pc, ins):
    global d
    if d['111'] == '0'*12+'0100':
        pc = decimal(ins[8:])
    else:
        pc += 1
    d['111'] = '0'*16
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def jmp_ifGT(pc, ins):
    global d
    if d['111'] == '0'*12+'0010':
        pc = decimal(ins[8:])
    else:
        pc += 1
    d['111'] = '0'*16
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def jmp_ifEQ(pc, ins):
    global d
    if d['111'] == '0'*12+'0001':
        pc = decimal(ins[8:])
    else:
        pc += 1
    d['111'] = '0'*16
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst


def halt(pc, ins):
    global d
    d['111'] = '0'*16
    lst = [pc, d['000'], d['001'], d['010'], d['011'],
           d['100'], d['101'], d['110'], d['111']]
    return lst

def fun(str1):
    pwr=-1
    ans=0
    for i in str1:
        ans+=int(i)*(2**pwr)
        pwr-=1
    return ans
def fconvert(val):
    valm = val[3:]
    vale = val[:3]

    valm += "00000000000000000"
    
    edec = decimal(vale)
    valbin = "1" + valm[:edec] + "." + valm[edec:]
    ans=str(decimal("1"+valm[:edec])+fun(valm[edec:]))
    return ans
            

    
    
def F_Addition(pc,ins):
    global d
    a=fconvert(strreg(d[ins[7:10]])[8:])
    b=fconvert(strreg(d[ins[10:13]])[8:])
    
    
    d[ins[13:16]]=a+b
    if(d[ins[13:16]]>252.0):
         d['111']='0'*12+'1000'
    else:
        d['111']='0'*16
    pc+=1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],d['100'], d['101'], d['110'], d['111']]
    return lst
def F_Subtraction(pc,ins):
    global d
    a=fconvert(strreg(d[ins[7:10]])[8:])
    b=fconvert(strreg(d[ins[10:13]])[8:])
    
    if(b>a):
        d['111']='0'*12+'1000'
        d[ins[13:16]]=0
        pc+=1
        lst = [pc, d['000'], d['001'], d['010'], d['011'],d['100'], d['101'], d['110'], d['111']]
        return lst

        
    d[ins[13:16]]=a-b
    d['111']='0'*16
    pc+=1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],d['100'], d['101'], d['110'], d['111']]
    return lst
def Move_F_immediate(pc,ins):
    global d
    d[ins[5:8]]=fconvert(ins[8:])
    d['111']='0'*16
    pc+=1
    lst = [pc, d['000'], d['001'], d['010'], d['011'],d['100'], d['101'], d['110'], d['111']]
    return lst
    
def strpc(val):
    data = bin(val)[2:]
    data = '0'*(8-len(data))+data
    return data


def take_input():
    #input_list = []
    input_arr1=sys.stdin.read().splitlines()
    for line in input_arr1:
        if(line==''):
             input_arr_1.remove(line)
    input_list=list(x for x in input_arr1)

    return input_list

def ftod(num):
        pwr = -1
        ans = ''
        idx = 0
        for i in range(len(num)):
            if(num[i] == '.'):
                idx = i
                break
        itr = num[:idx]
        ans += bin(int(itr))[2:]+'.'
        fnum = float(num[idx:])
        para = float(num[idx:])
        check = []
        check.append(para)
        while(True):
            numflt = para*(2)
            numflt2 = str(numflt)
            ans += numflt2[0]
            fidx = 0
            for i in range(len(numflt2)):
                if numflt2[i] == '.':
                    fidx = i
                    break
            fnum2 = float(numflt2[fidx:])
            if (fnum2 in check):
                break
            check.append(fnum2)
            if fnum2 == 0:
                break
            para = fnum2
        
        x = ans.index('.')
        exp = x-1
        mantissa = ans[1:x]+ans[x+1:]
    
        explen = len(bin(exp)[2:])
        mlen = len(str(mantissa))

        data = "0"*(3-explen) + str(bin(exp))[2:] + str(mantissa) + "0"*(5-mlen)
        return data
def strreg(val):
    if('.' in str(val)):
        data=ftod(str(val))
    else:
        data=bin(val)[2:]
    data = '0'*(16-len(data))+data
    return data


r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0
flag = '0'


d = {'000': r0, '001': r1, '010': r2, '011': r3,
     '100': r4, '101': r5, '110': r6, '111': flag}


def main():
    global d
    getdata = take_input()
    PC = 0
    x_axis=[]
    y_axis=[]
    cycle=0
    output = []
    mem = {}
  #  d={'000':r0,'001':r1,'010':r2,'011':r3,'100':r4,'101':r5,'110':r6,'111':flag}
    halted = False
    while(not halted):
        instruction = getdata[PC]

        if (instruction[:5] == '01010'):
            halted = True
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = halt(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])

            break
        elif(instruction[:5] == '10000'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = Addition(PC, instruction)
            PC = lst[0]

            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])

        elif(instruction[:5] == '10001'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = Subtraction(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])

        elif(instruction[:5] == '10010'):

            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = mov_imm(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '10011'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = mov_reg(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '10100'):
            pc = strpc(PC)
            if(instruction[8:] not in list(mem.keys())):
                mem[instruction[8:]] = 0
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = load(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '10101'):

            mem[instruction[8:]] = d[instruction[5:8]]
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = store(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '10110'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = multiply(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '10111'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = divide(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11000'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = rshift(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11001'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = lshift(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11010'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = xor(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11011'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = Or(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11100'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = And(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11101'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = invert(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11110'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = Compares(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '11111'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = unconditional(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '01100'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = jmp_ifLT(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '01101'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = jmp_ifGT(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '01111'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = jmp_ifEQ(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '00000'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = F_Addition(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '00001'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = F_Subtraction(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
        elif(instruction[:5] == '00010'):
            pc = strpc(PC)
            x_axis.append(PC)
            y_axis.append(cycle)
            cycle+=1
            lst = Move_F_immediate(PC, instruction)
            PC = lst[0]
            r0 = strreg(lst[1])
            r1 = strreg(lst[2])
            r2 = strreg(lst[3])
            r3 = strreg(lst[4])
            r4 = strreg(lst[5])
            r5 = strreg(lst[6])
            r6 = strreg(lst[7])
            flag = lst[8]
            output.append([pc, r0, r1, r2, r3, r4, r5, r6, flag])
    if(len(output)+len(mem) > 256):
        sys.stdout.write(
            "ERROR: The Memory allocated is greater than 256 lines\n")
        exit()
    for i in range(len(output)):
        for j in output[i]:
            sys.stdout.write(j+" ")
        sys.stdout.write("\n")
    default = 256-(len(getdata)+len(mem))
    mem_list = list(mem.keys())
    lst_sorted = []
    for i in mem_list:
        lst_sorted.append(decimal(i))
    lst_sorted.sort()
    for i in range(len(mem_list)):
        mem_list[i] = strreg(lst_sorted[i])[8:]
    # countline=1
    for i in getdata:
        #sys.stdout.write(str(countline)+" : ")
        sys.stdout.write(i+"\n")
        # countline+=1
    for i in mem_list:
        #sys.stdout.write(str(countline)+" : ")
        sys.stdout.write(strreg(mem[i])+"\n")
        # countline+=1
    for i in range(default):
        #sys.stdout.write(str(countline)+" : ")
        sys.stdout.write("0"*16)
        sys.stdout.write("\n")
        # countline+=1
    graph.scatter(y_axis,x_axis)
    graph.show()


main()
