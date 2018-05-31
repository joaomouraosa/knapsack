#!/usr/bin/env python2

import random

def keygen(k):
    privateKeyTuple = getPrivateKey(k)
    s = privateKeyTuple[0]
    total = privateKeyTuple[1]
    var = random.randint(2,9)
    m = random.randint(total+1,var*total)

    while(True):
        n = random.randint(2,m)
        if (isCoprime(m,n)):
            break
        
    p = getPublicKey(s,n,m)

    return (p,s,m,n)

def cipher(msg, p):
    k = len(p)
    tmp = 0
    cipherMsg = []
    l = 0
    
    for i in range(0,len(msg)):
        if (l>=k):
            l=0
            cipherMsg.append(tmp)
            tmp=0
            
        if (msg[i]==1):
            tmp += p[l]
            
        l+=1
        
    cipherMsg.append(tmp)

    return cipherMsg

def decipher(msg, s, m, n):
    decipherMsg = []
    key = []
    r = getModInverse(n,m)
    
    for k in msg:
        total = k * r % m
        tmpList = []
        
        for i in range(len(s)-1,-1,-1):
            if (s[i]<=total):
                total = total-s[i]
                tmpList.append(1)
            else:
                tmpList.append(0)

        tmpList.reverse()
        decipherMsg = decipherMsg + tmpList
        index = len(decipherMsg)-len(tmpList)                

    for i in range(index,len(decipherMsg)):
        if (i>0):
            if (len(s)%i==0):
                if(all(x == decipherMsg[i] and x==0 for x in decipherMsg[i:])):
                    decipherMsg[i:] = []
                    break
                
    return decipherMsg

def getPrivateKey(k):
    s = []
    first = random.randint(2,19)
    s.append(first)
    total = first

    for number in range(1,k):
        var = random.randint(2,19)
        nextN = random.randint(total+1,var*total)
        total += nextN
        s.append(nextN)
        
    return (s,total)

def getPublicKey(s,n,m):
    p = ['None'] * len(s)

    for i in range(0,len(s)):
        p[i]=s[i] * n % m
        
    return p

def isCoprime(arg1, arg2):
    return (gcd(arg1, arg2)==1)

def gcd(arg1, arg2):
    while (arg2>0):
        tmp = arg1
        arg1= arg2
        arg2= tmp%arg2
        
    return arg1

def getModInverse(arg1, arg2):
    a, d = 1,1
    b, c = 0,0
    n = arg2
    
    while (arg2 != 0):
        quo  = arg1 // arg2
        tmp  = arg1
        arg1 = arg2
        arg2 = tmp % arg2
        tmpA = a
        tmpC = c
        a = b
        b = tmpA - quo*b
        c = d
        d = tmpC - quo*d
            
    if (arg1==1):
        return a%n
