import math
cpu=0
space=input("Enter memory :")
print(" 1. Bit Addressable Memory - Cell Size = 1 bit \n 2. Nibble Addressable Memory - Cell Size = 4 bit\n 3. Byte Addressable Memory - Cell Size = 8 bits \n 4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")
mem=int(input("Enter integer value to choose :"))
if mem==4:
    cpu=int(input("Enter memory supported by cpu in bits :"))
dic={1:1,2:4,3:8,4:cpu}

op1=dic[mem]

l=space.split()
no=int(l[0])
if l[1][0]=="K":
    ans=2**10
elif l[1][0]=="M":
    ans=2**20
elif l[1][0]=="G":
    ans=2**30
elif l[1][0]=="T":
    ans=2**40
mul=l[1][1]
if mul=='B':
    ans*=(2**3)
elif mul=='b':
    ans*=1
ans*=no

bits=ans/op1

length=int(input("Enter length of instruction in bits :"))
reg=int(input("Enter length of register in bits :"))

min_bits = int(math.log2(bits))
print("Minimum bits required to represent the address",min_bits)
op_c=int(length-reg-min_bits)
print("Bits needed by opcode",op_c)
filler=int(length-(2*reg+op_c))
print("No. of filler bits in second instruction ",filler)
sup_ins=int(2**op_c)
print("Maximum no. of instructions supported",sup_ins)
reg_sup=int(2**reg)
print("Maximum number of registers supported",reg_sup)


#SYSTEM ENHANCEMENT

#TYPE 1
option=int(input("Enter the second option of addressability you want to choose :"))
if option==4:
    cpu=int(input("Enter memory supported by cpu in bits :"))
dic={1:1,2:4,3:8,4:cpu}

op2=dic[option]
if op2>op1:
    saved=int(math.log2(op2/op1))
    print("-",saved,"pins saved")
else:
    extra=int((math.log2(op1/op2)))
    print(extra,"extra pins required")

#TYPE 2
cpu1=int(input("Enter no of bits of the cpu :"))
lg=math.log2(cpu1)
pins=int(input("No. of address pins of the cpu :"))
print(" 1. Bit Addressable Memory - Cell Size = 1 bit \n 2. Nibble Addressable Memory - Cell Size = 4 bit\n 3. Byte Addressable Memory - Cell Size = 8 bits \n 4. Word Addressable Memory - Cell Size = Word Size (depends on CPU)")
mem=int(input("Enter integer value to choose :"))
#if mem==4:
 #   cpu=int(input("Enter memory supported by cpu in bits :"))
dic={1:0,2:2,3:3,4:lg}
val=lg-dic[mem]
memory = cpu1*(2**pins)
final=memory//(2**val)
#print(final)
value=math.log2(final)
if value%10==0:
    rem=7
else:
    rem=int((value%10)-3)
print(2**rem,end=" ")
if value<=10:
    print("B")
elif value<=20:
    print("KB")
elif value<=30:
    print("MB")
elif value<=40:
    print("GB")
elif value<50:
    print("TB")
