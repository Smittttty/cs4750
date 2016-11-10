
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

    P = [[{} for x in range(n + 1)] for y in range(n + 1)]

    for j in range(0, n):
        for i in range(j-1, -1, -1):
            for N in G.keys():
                P[j][i][N] = []
                print i, j
    for j in range(1, n):
        for N, R in G.items():
            for rule in R:
                if words[j] == rule:
                    print j, j-1
                    P[j][j-1][N].append((j, N + " -> " + rule))
    return P;

CNF = readCNF("g1.ecfg")
print CNF
print ckyParse("the dog bit the rat", CNF)