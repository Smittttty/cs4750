
def readCNF(fileName):
    f = file(fileName)
    CNF = {};
    for line in f:
        parts = line.split("->")
        nonterminalKey = parts[0].strip()
        terminals = parts[1].strip()
        terminals = terminals.strip("\"")
        if not CNF.has_key(nonterminalKey):
            CNF[nonterminalKey] = []
        CNF[nonterminalKey].append(terminals)

    return CNF



def ckyParse(s, G):
    words = s.split()
    n = len(words)
    P = [[{} for x in range(n)] for y in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            for N, R in G.items():
                P[i][j][N] = []

    for i in range(0, n):
        for N, R in G.items():
            for rule in R:
                if(rule == words[i]):
                    P[0][i][N].append((0, i, rule))

        change = True
        while change:
            change = False
            for N, R in G.items():
                if(len(P[0][i][N]) != 0):
                    for N1, R1 in G.items():
                        for rule in R1:
                            if N == rule and not (0, i, N) in P[0][i][N1]:
                                P[0][i][N1].append((0, i, N))
                                change = True

    for i in range(2, n + 1):
        for j in range(1, n-i+2):
            for k in range(1, i):
                for N, R in G.items():
                    for rule in R:
                        parts = rule.split()

                        if not len(parts) == 2:
                            continue
                        A = parts[0]
                        B = parts[1]
                        if(len(P[k-1][j-1][A]) > 0 and len(P[i-k-1][j+k-1][B]) > 0):
                            P[i-1][j-1][N].append((k-1, j-1, i-k-1, j+k-1, rule))
            change = True
            while change:
                change = False
                for N, R in G.items():
                    if (len(P[i-1][j-1][N]) != 0):
                        for N1, R1 in G.items():
                            for rule in R1:
                                if N == rule and not (i-1, j-1, N) in P[i-1][j-1][N1]:
                                    P[i-1][j-1][N1].append((i-1, j-1, N))
                                    change = True

    return P

def printParse(P, l = None):
    if(l == None):
        n = len(P)
        if(len(P[n-1][0]['S']) == 0):
            print "No valid parse"

        for n in P[n-1][0]['S']:
            if len(n) == 5:
                rules = n[4].split();
                t1 = (n[0], n[1], rules[0])
                t2 = (n[2], n[3], rules[1])
                print t1, t2
                print "[S " + printParse(P, t1) + " " + printParse(P, t2) + "]"
            if len(n) == 3:
                print "[S " + printParse(P, n) + "]"
    else:

      #  print l[0], l[1]
        index = 2;
        if len(l) == 5:
            index = 4
        for n in P[l[1]][l[0]][l[index]]:
           # print l
           # print n
            if len(n) == 5:
                rules = n[4].split();
                t1 = (n[0],n[1], rules[0])
                t2 = (n[2], n[3], rules[1])
               # print t1, t2
                return "[" + l[2] + " " + printParse(P, t1) + " " + printParse(P, t2) + "]"
            if len(n) == 3:
                print n
                return "[" + l[2] + " " + printParse(P, n) + "]"
    return ""

# def ckyParse(s, G):
#     words = s.split()
#     n = len(words)
#     P = [[{} for x in range(n)] for y in range(n)]
#     for j in range(0, n):
#         for i in range(j, -1, -1):
#             for N, R in G.items():
#                 P[i][j][N] = []
#
#     for j in range(0, n):
#         for N, R in G.items():
#             for rule in R:
#                 if words[j] == rule:
#                     P[j][j][N].append((j, rule))
#         change = True
#         while change:
#             change = False
#             for N, R in G.items():
#                 if(len(P[j][j][N]) != 0):
#                     for N1, R1 in G.items():
#                         for rule in R1:
#                             if N == rule and not (j, N) in P[j][j][N1]:
#                                 P[j][j][N1].append((j, N))
#                                 change = True
#
#     for j in range(1, n):
#         for i in range(j, -1, -1):
#             for k in range(i + 1, j - 1):
#                 for N, R in G.items():
#                     for rule in R:
#                         parts = rule.split()
#                         if len(parts) == 2:
#                             A = parts[0]
#                             B = parts[1]
#                             if(j == 1 and i == 1):
#                                 print (i, k), (k, j)
#                                 #print A, B
#                                # print (i, k, len(P[i][k][A]) > 0), (k, j, len(P[k][j][B]) > 0)
#                             if len(P[i][k][A]) > 0 and len(P[k][j][B]) > 0:
#                                 P[i][j][N].append((k, A + " " + B))
#             change = True
#             while(change):
#                 change = False
#                 for N, R in G.items():
#                     if len(P[i][j][N]) != 0:
#                         for N1, R1 in G.items():
#                             for rule in R1:
#                                 if N == rule and not (j, N) in P[i][j][N1]:
#                                     P[i][j][N1].append((j, N))
#                                     change = True
#
#     return P


CNF = readCNF("g1.ecfg")
P = ckyParse("the dog bit the rat", CNF)
printParse(P);
print P
line = "   "
for x in range(0, len(P[0])):
    line += " " + str(x) + " "
print line
for y in range(0, len(P)):
    line = str(y) + ": ";
    for x in range(len(P[0])):
        sum = 0;
        for N in P[y][x].values():
            sum += len(N)
        line += " " + str(sum) + " "

    print line

while True:
    input = raw_input("Location: ")
    vals = input.split()
    A = P[int(vals[0])][int(vals[1])]
    for N, R in A.items():
        if len(R) > 0:
            for rule in R:
                print N + " -> " + str(rule)
