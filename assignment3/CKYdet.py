
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
    for j in range(0, n):
        for i in range(j, -1, -1):
            for N, R in G.items():
                P[i][j][N] = []

    for j in range(0, n):
        for N, R in G.items():
            for rule in R:
                if words[j] == rule:
                    P[j][j][N].append((j, rule))
        change = True
        while change:
            change = False
            for N, R in G.items():
                if(len(P[j][j][N]) != 0):
                    for N1, R1 in G.items():
                        for rule in R1:
                            if N == rule and not (j, N) in P[j][j][N1]:
                                P[j][j][N1].append((j, N))
                                change = True

    for j in range(0, n):
        for i in range(j, -1, -1):
            for k in range(i, j + 1):
                for N, R in G.items():
                    for rule in R:
                        parts = rule.split()
                        if len(parts) == 2:
                            A = parts[0]
                            B = parts[1]
                            print A, B
                            print (i, k, len(P[i][k][A]) > 0), (k, j, len(P[k][j][B]) > 0)
                            if len(P[i][k][A]) > 0 and len(P[k][j][B]) > 0:
                                P[i][j][N].append((k, A + " " + B))
            change = True
            while(change):
                change = False
                for N, R in G.items():
                    if len(P[i][j][N]) != 0:
                        for N1, R1 in G.items():
                            for rule in R1:
                                if N == rule and not (j, N) in P[i][j][N1]:
                                    P[i][j][N1].append((j, N))
                                    change = True

    return P


CNF = readCNF("g1.ecfg")
P = ckyParse("the dog bit the rat", CNF)

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
