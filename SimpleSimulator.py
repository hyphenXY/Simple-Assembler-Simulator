import sys

def decimal(num):
     
     pwr=0
     ans=0
     for i in num[::-1]:
          ans=ans+(int(i)*(2**pwr))
          pwr+=1
     return ans
          
def Addition(pc,ins):
     global d
     d[ins[13:16]]=d[ins[7:10]]+d[ins[10:13]]
     r=bin(d[ins[13:16]])[2:]
     if(len(r)>16):
         d[ins[13:16]]=d[ins[13:16]]%(2**16)
         d['111']='0'*12+'1000'
     else:
          d['111']='0'*16
     pc+=1
     
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def Subtraction(pc,ins):
     global d
     if (d[ins[10:13]]>d[ins[7:10]]):
          d[ins[13:16]]=0
          d['111']='0'*12+'1000'
          pc+=1
          lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
          return lst
     d[ins[13:16]]=d[ins[7:10]]-d[ins[10:13]]
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
     
def mov_imm(pc,ins):
     global d
     d[ins[5:8]]=decimal(ins[8:])
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
     

def mov_reg(pc,ins):
     global d
     d[ins[10:13]]=d[ins[13:16]]
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst


def load(pc,ins):
     global d
     keys=list(d.keys())
     if(ins[8:] not in keys):
          d[ins[8:]]=0
     d[ins[5:8]]=d[ins[8:]]
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst

def store(pc,ins):
     global d
     d[ins[8:]]=d[ins[3:6]]
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def multiply(pc,ins):
     global d
     d[ins[13:16]]=d[ins[7:10]]*d[ins[10:13]]
     r=bin(d[ins[13:16]])[2:]
     if(len(r)>16):
         d['111']='0'*12+'1000'
     else:
          d['111']='0'*16
     pc+=1
     
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def divide(pc,ins):
     global d
     d['000']=d[ins[10:13]]//d[ins[13:16]]
     d['001']=d[ins[10:13]]%d[ins[13:16]]
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def rshift(pc,ins):
     global d
     d[ins[5:8]]=d[ins[5:8]]//(2**decimal(ins[8:]))
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def lshift(pc,ins):
     global d
     d[ins[5:8]]=d[ins[5:8]]*(2**decimal(ins[8:]))
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst

def xor(pc,ins):
     global d
     a=''
     b=bin(d[ins[7:10]])[2:]
     b='0'*(16-len(b))+b
     c=bin(d[ins[10:13]])[2:]
     c='0'*(16-len(c))+c
     for i in range(16):
          if(b[i]=='0' and c[i]=='1'):
               a+='1'
          if(b[i]=='1' and c[i]=='0'):
               a+='1'
          else:
               a+='0'
     d[ins[13:16]]=decimal(a)
     
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst

     
def Or(pc,ins):
     global d
     a=''
     b=bin(d[ins[7:10]])[2:]
     b='0'*(16-len(b))+b
     c=bin(d[ins[10:13]])[2:]
     c='0'*(16-len(c))+c
     for i in range(16):
          if(b[i]=='0' and c[i]=='0'):
               a+='0'
          else:
               a+='1'
     d[ins[13:16]]=decimal(a)
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def And(pc,ins):
     global d
     a=''
     b=bin(d[ins[7:10]])[2:]
     b='0'*(16-len(b))+b
     c=bin(d[ins[10:13]])[2:]
     c='0'*(16-len(c))+c
     for i in range(16):
          if(b[i]=='1' and c[i]=='1'):
               a+='1'
          else:
               a+='0'
     d[ins[13:16]]=decimal(a)
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def invert(pc,ins):
     global d
     a=bin(d[ins[10:13]])[2:]
     a='0'*(16-len(a))+a
     b=''
     for i in a:
          if i=='1':
               b+='0'
          else:
               b+='1'
     d[ins[13:]]=decimal(b)
     d['111']='0'*16
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def Compares(pc,ins):
     global d
     if (d[ins[10:13]]<d[ins[13:16]]):
          d['111']='0'*12+'0100'
     elif (d[ins[10:13]]>d[ins[13:16]]):
          d['111']='0'*12+'0010'
     elif (d[ins[10:13]]==d[ins[13:16]]):
          d['111']='0'*12+'0001'
     pc+=1
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst

def unconditional(pc,ins):
     global d
     pc=decimal(ins[8:])
     d['111']='0'*16
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def jmp_ifLT(pc,ins):
     global d
     if d['111']=='0'*12+'0100':
          pc=decimal(ins[8:])
     else:
          pc+=1
     d['111']='0'*16
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst

def jmp_ifGT(pc,ins):
     global d
     if d['111']=='0'*12+'0010':
          pc=decimal(ins[8:])
     else:
          pc+=1
     d['111']='0'*16
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def jmp_ifEQ(pc,ins):
     global d
     if d['111']=='0'*12+'0001':
          pc=decimal(ins[8:])
     else:
          pc+=1
     d['111']='0'*16
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def halt(pc,ins):
     global d
     d['111']='0'*16
     lst=[pc,d['000'],d['001'],d['010'],d['011'],d['100'],d['101'],d['110'],d['111']]
     return lst
def strpc(val):
     data=bin(val)[2:]
     data='0'*(8-len(data))+data
     return data
def take_input():
     input_list=[]
     for line in sys.stdin:
        if(len(line[:-1])!=16):
             sys.stdout.write("ERROR: An unidentified line format has been detected.\n")
             exit()
        input_list.append(line[:-1])
        
     return input_list
def strreg(val):
     data=bin(val)[2:]
     data='0'*(16-len(data))+data
     return data

r0=0
r1=0
r2=0
r3=0
r4=0
r5=0
r6=0
flag='0'

    
d={'000':r0,'001':r1,'010':r2,'011':r3,'100':r4,'101':r5,'110':r6,'111':flag}


def main():
     global d
     getdata=take_input()
     PC=0
     
     output=[]
     mem={}
   #  d={'000':r0,'001':r1,'010':r2,'011':r3,'100':r4,'101':r5,'110':r6,'111':flag}
     halted=False
     while(not halted):
          instruction=getdata[PC]
          
          if (instruction[:5]=='01010'):
               halted=True
               pc=strpc(PC)
               lst=halt(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
               
               break
          elif(instruction[:5]=='10000'):
               pc=strpc(PC)
               lst=Addition(PC,instruction)
               PC=lst[0]
               
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
               
          elif(instruction[:5]=='10001'):
               pc=strpc(PC)
               lst=Subtraction(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
               

          elif(instruction[:5]=='10010'):

               pc=strpc(PC)
               lst=mov_imm(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='10011'):
               pc=strpc(PC)
               lst=mov_reg(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='10100'):
               pc=strpc(PC)
               if(instruction[8:] not in list(mem.keys())):
                    mem[instruction[8:]]=0
               lst=load(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='10101'):
               
               mem[instruction[8:]]=d[instruction[5:8]]               
               pc=strpc(PC)
               lst=store(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='10110'):
               pc=strpc(PC)
               lst=multiply(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='10111'):
               pc=strpc(PC)
               lst=divide(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11000'):
               pc=strpc(PC)
               lst=rshift(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11001'):
               pc=strpc(PC)
               lst=lshift(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11010'):
               pc=strpc(PC)
               lst=xor(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11011'):
               pc=strpc(PC)
               lst=Or(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11100'):
               pc=strpc(PC)
               lst=And(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11101'):
               pc=strpc(PC)
               lst=invert(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11110'):
               pc=strpc(PC)
               lst=Compares(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='11111'):
               pc=strpc(PC)
               lst=unconditional(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='01100'):
               pc=strpc(PC)
               lst=jmp_ifLT(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='01101'):
               pc=strpc(PC)
               lst=jmp_ifGT(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
          elif(instruction[:5]=='01111'):
               pc=strpc(PC)
               lst=jmp_ifEQ(PC,instruction)
               PC=lst[0]
               r0=strreg(lst[1])
               r1=strreg(lst[2])
               r2=strreg(lst[3])
               r3=strreg(lst[4])
               r4=strreg(lst[5])
               r5=strreg(lst[6])
               r6=strreg(lst[7])
               flag=lst[8]
               output.append([pc,r0,r1,r2,r3,r4,r5,r6,flag])
     if(len(output)+len(mem)>256):
          sys.stdout.write("ERROR: The Memory allocated is greater than 256 lines\n")
          exit()
     for i in range(len(output)):
          for j in output[i]:
               sys.stdout.write(j+" ")
          sys.stdout.write("\n")
     default=256-(len(getdata)+len(mem))
     mem_list=list(mem.keys())
     lst_sorted=[]
     for i in mem_list:
          lst_sorted.append(decimal(i))
     lst_sorted.sort()
     for i in range(len(mem_list)):
          mem_list[i]=strreg(lst_sorted[i])[8:]
     #countline=1
     for i in getdata:
          #sys.stdout.write(str(countline)+" : ")
          sys.stdout.write(i+"\n")
          #countline+=1
     for i in mem_list:
          #sys.stdout.write(str(countline)+" : ")
          sys.stdout.write(strreg(mem[i])+"\n")
          #countline+=1
     for i in range(default):
          #sys.stdout.write(str(countline)+" : ")
          sys.stdout.write("0"*16)
          sys.stdout.write("\n")
          #countline+=1
     
          
          
main()
