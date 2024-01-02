from cards import *

figures=["ace","king","queen","ten","nine"]
suits=["spades","hearts" ,"diamonds","clubs"]

def CountF(set,figur):
    ret=0 
    for x in set:
        if(x.figure==figur): ret+=1
    return ret

def CountS(set,sui):
    ret=0 
    for x in set:
        if(x.suit==sui): ret+=1
    return ret

def High(set,figur):
    if(CountF(set,figur)>0): return True
    return False

def Pair(set,figur):
    if(CountF(set,figur)>1): return True
    return False

def LowStraight(set):
    tab=figures[1:]
    for f in tab:
        if not High(set,f): return False
    return True

def HighStraight(set):
    tab=figures[:-1]
    for f in tab:
        if not High(set,f): return False
    return True

def Three(set,figur):
    if(CountF(set,figur)>2): return True
    return False

def Full(set,fig1,fig2):
    if(Three(set,fig1) and Pair(set,fig2)): return True
    return False

def Flush(set,col):
    if(CountS(set,col)>=4): return True
    else: return False

def Four(set,figur):
    if(CountF(set,figur)>3): return True
    return False

def Poker(set,sui):
    tab=figures[1:]
    for f in tab:
        ret=0
        for a in set:
            if a.suit==sui and a.figure==f : ret=1
        if ret==0: return False
    return True

def PokerKing(set,sui):
    tab=figures[:-1]
    for f in tab:
        ret=0
        for a in set:
            if a.suit==sui and a.figure==f : ret=1
        if ret==0: return False
    return True


#\/\/\/\/\/\/\/exapmle of usage\/\/\/\/\/\/\/\/\/\/

# n=input()
# set_inp=[]

# for i in range(int(n)):
#     s=input().split()
#     inp=Card(str(s[0]),str(s[1]))
#     set_inp.append(inp)

# print(High(set_inp,"king"))
# print(Pair(set_inp,"queen"))
# print(LowStraight(set_inp))
# print(HighStraight(set_inp))
# print(Three(set_inp,"king"))
# print(Full(set_inp,"king","ten"))
# print(Flush(set_inp,"hearts"))
# print(Poker(set_inp,"hearts"))
# print(PokerKing(set_inp,"hearts"))
    

