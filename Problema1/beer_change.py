def beer_change(bar: list):
    # bar lista di liste
    # [['M', 'A'], ['F', 'B'], ['M', 'A']]
    N = len(bar)
    AUX = [-1] * N
    m = 0
    f = 1

    for i in range(N):
        if bar[i][0] == 'M' and bar[i][1] == 'A':
            AUX[m] = i
            m += 2
        elif bar[i][0] == 'F' and bar[i][1] == 'B':
            AUX[f] = i
            f += 2

    k = 0
    while k < N and AUX[k] != -1:
        if AUX[k + 1] < AUX[k]:
            AUX[k + 1], AUX[k] = AUX[k], AUX[k + 1]

        u = AUX[k]
        v = AUX[k + 1] - 1

        while u < AUX[k + 1]:
            temp = bar[u][1]
            bar[u][1] = bar[u + 1][1]
            bar[u + 1][1] = temp
            u += 1

        while v > AUX[k]:
            temp = bar[v][1]
            bar[v][1] = bar[v - 1][1]
            bar[v - 1][1] = temp
            v -= 1

        k += 2
       
    print(AUX)
    return bar

#istanza = [['M', 'B'], ['M', 'A'], ['F', 'B'], ['M', 'B'], ['F', 'A'], ['M', 'B'], ['M', 'B'], ['F', 'B'], ['F', 'A'], ['M', 'A'], ['F', 'A']]
#istanza = [['M', 'B'], ['M', 'B'], ['F', 'A'], ['M', 'B'], ['F', 'A'], ['M', 'B'], ['M', 'B'], ['F', 'A'], ['F', 'A'], ['M', 'B'], ['F', 'A']]
istanza = [['M', 'A'], ['M', 'A'], ['F', 'B'], ['M', 'A'], ['F', 'B'], ['M', 'A'], ['M', 'A'], ['F', 'B'], ['F', 'B'], ['M', 'A'], ['F', 'B'], ['F', 'B']]

#print(beer_change(istanza))
print(beer_change(istanza))
