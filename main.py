
import math

def decimalToBinary(n):
    x = str(bin(binary(n)).replace("0b", ""))
    while(len(x) < 4):
        x = "0" + x
    return x

def binary(x):
    if(x.isupper()):
        return int(ord(x) - 55)
    else:
        return int(x)

def findCount(x):
    count = -1
    arr = []
    for i in x:
        arr.append(binary(i))
        count += 1
    return (count, arr)

def findK(L, n):
    ary = ((2 * n) + 1)
    k = math.ceil(L/math.log2(ary))
    print("(2n+1)^k >= 2^L => {}^k >= 2^{} => k = ceiling({}/LOG2({})) => ceiling({}/{}) => ceiling({}) = {}".format(ary, L, L, ary, L, "{:.3f}".format(math.log2(ary)), "{:.3f}".format(L/math.log2(ary)), k))
    return k

def findS(count, x):
    print("{} is equal to ".format(ES), end='')
    for i in x:
        print("{} ".format(decimalToBinary(str(i))), end='')
    print(", convert to decimal:")
    s = 0
    print("s = ", end='')
    for i in x:
        s += i * (16 ** count)
        print("{} * (16 ^ {} ) + ".format(i, count), end='')
        count = count - 1
    print(" = ", s, "\n")
    return s

def conToNArySystem(S):
    ary = ((2 * n) + 1)
    print("Now convert S to {}-ary system".format(ary))
    remainders = []
    print("S = ", end='')
    while(S > ary):
        print("{} = {} * {} + {}".format(S, ary, int(S / ary), int(S % ary)))
        remainders.append(int(S % ary))
        S = int(S / ary)
    print("{} = {} * {} + {}".format(S, ary, int(S / ary), int(S % ary)))
    remainders.append(int(S % ary))
    remainders.reverse()
    S = ""
    for i in remainders:
        S += str(i)
    S = int(S)
    print("S = {} => ".format(S), end='')
    cnt = len(remainders) - 1
    x = 0
    for i in remainders:
        x += i * (ary ** cnt)
        print("{} * {} ^ {} + ".format(i, ary, cnt), end='')
        cnt -= 1
    print(" = {}".format(x))
    return S

def getTable():
    length = int(input("length of table = "))
    table = []
    for i in range(length):
        table.append(int(input("enter table data: ")))
    return table

def getGs(table, n):
    newTable = []
    F = []
    for i in range(int(len(table)/n)):
        if len(table[0:n]) == 0:
            print(table[0:n])
            break
        newTable = table[0:n]
        del table[0:n]
        F.append(newTable)
    return F

def extract(x, ary, d):
    print("Extraction: ")
    print("F({}) = ".format(x), end='')
    index = 1
    f = 0
    for i in x:
        f += i * index
        print("{} * {} + ".format(i, index), end='')
        index += 1
    f = f % ary
    print("mod {} = {} ".format(ary, f), end='')
    if f == d:
        print("OK")
    else:
        print("NOT OK")


def clacFG(x, d, n, round):
    ary = ((2 * n) + 1)
    print("F(G{}) = ".format(round+1), end='')
    mult = 1
    FG = 0
    for i in x:
        FG += i * mult
        print("{} * {} + ".format(i, mult), end='')
        mult = mult + 1
    print("mod {} => {} mod {} = ".format(ary, FG, ary), end='')
    FG = FG % ary
    print("{}".format(FG))
    s = (d - FG) % ary
    print("S = {} - {} mod {} = {}".format(d, FG, ary, s))
    if s == 0:
        print("S = 0, hence no pixel value is changed.")
    elif s != 0 and s <= n:
        print("S != 0 and S <= {} => value of g{} += 1 => ".format(n, s), end='')
        print(x)
        try:
            x[s-1] += 1
        except IndexError:
            print("{} mod {} = {}".format(-s, ary, -s % ary))
            s = -s % ary
            x[s - 1] += 1
        print(x)
        extract(x, ary, d)
    else:
        print("S != 0 and S is not <= {} => value of g(2n+1-s) -= 1 => ".format(n), end='')
        pos = (2 * n) + 1 - s
        try:
            x[pos-1] -= 1
        except IndexError:
            print("{} mod {} = {}".format(-pos, ary, -pos % ary))
            pos = -pos % ary
            x[pos - 1] -= 1
        print(x)
        extract(x, ary, d)
    return x

def calcPixels(F, S, n):
    finalTable = []
    S = str(S)
    round = 0
    for arr in F:
        finalTable.append(clacFG(arr, int(S[round]), n, round))
        round += 1
    print("FINAL TABLE ")
    for i in finalTable:
        print("{}".format(i))
    return finalTable



# CHANGE THE TABLE (enter values of rows after each other from left to right)
table = [102, 112, 210, 211, 111, 113, 114, 210]

L = int(input("Input L = "))
n = int(input("Input n = "))
ES = input("Input Embed Secret = ")
k = findK(L, n)
count, arr = findCount(ES)
S = findS(count, arr)
S = conToNArySystem(S)
F = getGs(table, n)
finalTable = calcPixels(F, S, n)



