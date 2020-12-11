import random
def accept(): # enter msg m = 111110001111 and r : (2^r >= m+r+1)
    msg = input("Enter data = ")
    r = int(input("Enter r = "))
    return msg,r
def calculateR(msg,rmain):
    msglist = list(msg)
    msglist.insert(len(msglist), 999) # pahila -1 position la 999 direct add kela
    for i in rmain[1:]: # position-1 la add karat raha take it as it is
        msglist.insert(-i+1, 999)
    # msglist = ['1', 999, '1', '1', '1', '1', '0', '0', '0', 999, '1', '1', '1', 999, '1', 999, 999]
    
    # to understand from this
    Rmain = []
    for i in rmain:
        R = []
        k = i
        while(k<=len(msglist)):
            j=0
            while(k<=len(msglist) and j<i):
                R.append(msglist[-k])
                k=k+1; j=j+1
            k=k+i
        Rmain.append(R)
    # till this read Hamming code expt 09 with comments
    # this basically returns list inside list for r1, r2, r3,... lists
    # Rmain = [[999, '1', '1', '1', '0', '0', '1', '1', '1'], [999, '1', '1', '1', '0', '0', '1', '1'], [999, '1', '1', '1', '1', '1', '1', '1'], [999, '0', '0', '0', '1', '1', '1', '1'], [999, '1']]
    
    Rall = []
    for i in Rmain:
        if(i.count('1') % 2 == 0): # if even parity add 0
            Rall.append('0')
        else: # for odd parity add 1
            Rall.append('1')
    # Rall will contain r1, r2, r4,.. bits
    # Rall = ['0', '1', '1', '0', '1']
    
    # to substitute Rall in msglist(which previously contains 999)
    for i in range(r):
        msglist[-(2**i)] = Rall[i]
    return ''.join(msglist) # at the end msglist would contain all data with r1, r2, r4,... bits situated in it.
def transmitting(sendmsg):
    print("Data to be transmitted = ",sendmsg)
def errorgeneration(sendmsg):
    slist = list(sendmsg)
    errorlist = random.sample(range(0,len(slist)),1)
    for i in errorlist:
        if (slist[i] == '1'):
            slist[i] ='0'
        elif (slist[i] == '0'):
            slist[i] = '1'
    return ''.join(slist)
def receiving(errormsg,rmain):
    print("Data received = ",errormsg)
    
    # from this 
    errormsglist = list(errormsg)
    Rmain = []
    Rindex = []
    for i in rmain:
        R = []
        Ri = []
        k = i
        while(k<=len(errormsglist)):
            j=0
            while(k<=len(errormsglist) and j<i):
                R.append(errormsglist[-k])
                Ri.append(k)
                k=k+1; j=j+1
            k=k+i
        Rmain.append(R)
        Rindex.append(Ri)
    # to this r1, r2, r4,... lists are calculated.
    
    # from this
    Rall = []
    for i in Rmain:
        if(i.count('1') % 2 == 0):
            Rall.append('0')
        else:
            Rall.append('1')
    # till this r1, r2, r3,... bits are calculated
    
    Errors = []
    for i in range(r):
        D = []
        if (Rall[i] == '1'):
            for j in range(r):
                if i==j:
                    pass
                elif Rall[j] == '0':
                    D.append(list(set(Rindex[i]) - set(Rindex[j])))
                elif Rall[j] == '1':
                    D.append(list((set(Rindex[i])).intersection(set(Rindex[j]))))
        if (len(D)!=0):
            Errors = Errors + list(set.intersection(*map(set, D)))
    Errors = list(set(Errors))
    if(len(Errors)==0):
        print("Error cannot be detected by Hamming code method")
    else:
        print("Errors can be detected by Hamming code method\nErrors Detected at bits = ",Errors)
msg,r = accept()
rmain = [2**i for i in range(r)] # rmain = [1, 2, 4, 8, 16, ...]
sendmsg = calculateR(msg,rmain) # calculateR returns msg containing parity bits r1,r2,r4,etc
transmitting(sendmsg)
errormsg = errorgeneration(sendmsg)
receiving(errormsg,rmain)
