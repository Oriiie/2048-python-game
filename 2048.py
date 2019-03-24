import random
import os
a1 = ['2','0','0','0']
a2 = ['0','0','0','0']
a3 = ['0','0','0','0']
a4 = ['0','0','0','0']
a = 5
def call():
    print (a1)
    print('\n')
    print (a2)
    print('\n')
    print (a3)
    print('\n')
    print (a4)
    print('\n')
def right():
    for u in range (3):
        for i in range (3):
            if (a1[0]=='0' or a1[1]=='0' or a1[2]=='0' or a1[3]=='0'):
                if (a1[i]!='0' and a1[i+1]=='0'):
                    a1[i], a1[i+1]= a1[i+1], a1[i]
            if (a2[0]=='0' or a2[1]=='0' or a2[2]=='0' or a2[3]=='0'):
                if (a2[i]!='0' and a2[i+1]=='0'):
                    a2[i], a2[i+1]= a2[i+1], a2[i]
            if (a3[0]=='0' or a3[1]=='0' or a3[2]=='0' or a3[3]=='0'):
                if (a3[i]!='0' and a3[i+1]=='0'):
                    a3[i], a3[i+1]= a3[i+1], a3[i]
            if (a4[0]=='0' or a4[1]=='0' or a4[2]=='0' or a4[3]=='0'):
                if (a4[i]!='0' and a4[i+1]=='0'):
                    a4[i], a4[i+1]= a4[i+1], a4[i]
def left():
    for u in range (3):
        for i in range (3):
            if (a1[0]=='0' or a1[1]=='0' or a1[2]=='0' or a1[3]=='0'):
                if (a1[3-i]!='0' and a1[2-i]=='0'):
                    a1[3-i], a1[2-i]= a1[2-i], a1[3-i]
            if (a2[0]=='0' or a2[1]=='0' or a2[2]=='0' or a2[3]=='0'):        
                if (a2[3-i]!='0' and a2[2-i]=='0'):
                    a2[3-i], a2[2-i]= a2[2-i], a2[3-i]
            if (a3[0]=='0' or a3[1]=='0' or a3[2]=='0' or a3[3]=='0'):
                if (a3[3-i]!='0' and a3[2-i]=='0'):
                    a3[3-i], a3[2-i]= a3[2-i], a3[3-i]
            if (a4[0]=='0' or a4[1]=='0' or a4[2]=='0' or a4[3]=='0'):        
                if (a4[3-i]!='0' and a4[2-i]=='0'):
                    a4[3-i], a4[2-i]= a4[2-i], a4[3-i]
def up():
    for u in range (3):
        for i in range (4):
                if (a3[i]=='0'):
                    if (a4[i]!='0'):
                        a4[i],a3[i]=a3[i],a4[i]
                if (a2[i]=='0'):
                    if (a3[i]!='0'):
                        a3[i],a2[i]=a2[i],a3[i]
                if (a1[i]=='0'):        
                    if (a2[i]!='0'):
                        a2[i],a1[i]=a1[i],a2[i]
def down():
        for u in range (3):
            for i in range (4):
                if (a2[i]=='0'):
                    if (a1[i]!='0'):
                        a2[i],a1[i]=a1[i],a2[i]
                if (a3[i]=='0'):
                    if (a2[i]!='0'):
                        a3[i],a2[i]=a2[i],a3[i]
                if (a4[i]=='0'):
                    if (a3[i]!='0'):
                        a4[i],a3[i]=a3[i],a4[i]
def connectleft():
        for i in range (3):
            if (a1[i]==a1[i+1]):
                a1[i],a1[i+1]=str(2*int(a1[i])),'0'
            if (a2[i]==a2[i+1]):
                a2[i],a2[i+1]=str(2*int(a2[i])),'0'
            if (a3[i]==a3[i+1]):
                a3[i],a3[i+1]=str(2*int(a3[i])),'0'
            if (a4[i]==a4[i+1]):
                a4[i],a4[i+1]=str(2*int(a4[i])),'0'
def connectright():
    for u in range (3):
        for i in range (3):
            if (a1[3-i]==a1[2-i]):
                a1[3-i],a1[2-i]=str(2*int(a1[3-i])),'0'
            if (a2[3-i]==a2[2-i]):
                a2[3-i],a2[2-i]=str(2*int(a2[3-i])),'0'
            if (a3[3-i]==a3[2-i]):
                a3[3-i],a3[2-i]=str(2*int(a3[3-i])),'0'
            if (a4[3-i]==a4[2-i]):
                a4[3-i],a4[2-i]=str(2*int(a4[3-i])),'0'
def connectup():
        for i in range (4):
            if (a2[i]==a1[i]):
                a1[i],a2[i]=str(2*int(a1[i])), '0'
            if (a3[i]==a2[i]):
                a2[i],a3[i]=str(2*int(a2[i])), '0'
            if (a4[i]==a3[i]):
                a3[i],a4[i]=str(2*int(a3[i])), '0'
def connectdown():
    for i in range (4):
        if (a4[i]==a3[i]):
            a4[i], a3[i]=str(2*int(a4[i])), '0'
        if (a3[i]==a2[i]):
            a3[i], a2[i]=str(2*int(a3[i])), '0'
        if (a2[i]==a1[i]):
            a2[i], a1[i]=str(2*int(a2[i])), '0'
call()
while (a):
    if (a1[0]=='2048' or a1[1]=='2048' or a1[2]=='2048' or a1[3]=='2048'):
        print('Congratulations, you won!')
        break
    if (a2[0]=='2048' or a2[1]=='2048' or a2[2]=='2048' or a2[3]=='2048'):
        print('Congratulations, you won!')
        break
    if (a3[0]=='2048' or a3[1]=='2048' or a3[2]=='2048' or a3[3]=='2048'):
        print('Congratulations, you won!')
        break
    if (a4[0]=='2048' or a4[1]=='2048' or a4[2]=='2048' or a4[3]=='2048'):
        print('Congratulations, you won!')
        break 
    b = input("Enter direction: ")
    os.system('cls')
    if (b=='up'):
        up()
        connectup()
        up()
        call()
    if (b=='down'):
        down()
        connectdown()
        down()
        call()
    if (b=='left'):
        left()
        connectleft()
        left()
        call()
    if (b=='right'):
        right()
        connectright()
        right()
        call()
    if (b=='stop'):
        break
    num = random.randint(1,16)
    if (num==1 and a1[0]=='0'):
        a1[0]='2'
    if (num==2 and a1[1]=='0'):
        a1[1]='2'
    if (num==3 and a1[2]=='0'):
        a1[2]='2'
    if (num==4 and a1[3]=='0'):
        a1[3]='2'
    if (num==5 and a2[0]=='0'):
        a2[0]='2'
    if (num==6 and a2[1]=='0'):
        a2[1]='2'
    if (num==7 and a2[2]=='0'):
        a2[2]='2'
    if (num==8 and a2[3]=='0'):
        a2[3]='2'
    if (num==9 and a3[0]=='0'):
        a3[0]='2'
    if (num==10 and a3[1]=='0'):
        a3[1]='2'
    if (num==11 and a3[2]=='0'):
        a3[2]='2'
    if (num==12 and a3[3]=='0'):
        a3[3]='2'
    if (num==13 and a4[0]=='0'):
        a4[0]='2'
    if (num==14 and a4[1]=='0'):
        a4[1]='2'
    if (num==15 and a4[2]=='0'):
        a4[2]='2'
    if (num==16 and a4[3]=='0'):
        a4[3]='2'
    
