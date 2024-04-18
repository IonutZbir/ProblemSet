def compute_opt(scac):
    cols = len(scac[0])
    rows = len(scac)
    last_col = cols - 1

    print("Cols: ", cols, "\nRows: ", rows)
    # [val_ncomb, val_comb]
    OPT = [[0] * (cols + 1) for _ in range(4)]

    OPT[0][last_col] = [scac[0][last_col], scac[0][last_col] + scac[2][last_col]]
    OPT[1][last_col] = scac[1][last_col]
    OPT[2][last_col] = [scac[2][last_col], scac[0][last_col] + scac[2][last_col]]
    OPT[3][last_col] = max(
        OPT[0][last_col][0], OPT[1][last_col], OPT[2][last_col][0], OPT[2][last_col][1]
    )

    for i in range(last_col - 1, -1, -1):
        for j in range(rows):
            if j == 0:
                # non combinato
                OPT[j][i] = []
                OPT[j][i].append(
                    max(OPT[j + 1][i + 1], OPT[j + 2][i + 1][0], OPT[3][i + 2])
                    + scac[j][i]
                )
                # combinato
                OPT[j][i].append(
                    max(OPT[j + 1][i + 1], OPT[3][i + 2]) + scac[j + 2][i] + scac[j][i]
                )
            elif j == 1:
                OPT[j][i] = (
                    max(
                        OPT[j - 1][i + 1][0],
                        OPT[j + 1][i + 1][0],
                        OPT[j + 1][i + 1][1],
                        OPT[3][i + 2],
                    )
                    + scac[j][i]
                )
            else:
                OPT[j][i] = []
                # non combinato
                OPT[j][i].append(
                    max(OPT[j - 1][i + 1], OPT[j - 2][i + 1][0], OPT[3][i + 2])
                    + scac[j][i]
                )
                # combinato
                OPT[j][i].append(
                    max(OPT[j - 1][i + 1], OPT[3][i + 2]) + scac[j - 2][i] + scac[j][i]
                )
        OPT[3][i] = max(OPT[0][i][0], OPT[1][i], OPT[2][i][0], OPT[2][i][1])

    for r in OPT:
        print(r)

    return OPT[3][0]


scacchiera = [
    [3, 10, 10, 15, 6, 5, 30, 2, 500],
    [7, 2, 10, 1, 1, 2, 1, 3, 1],
    [1, 5, 8, 12, 30, 6, 30, 4, 500],
]

opt = compute_opt(scacchiera)
print("OPT = ", opt)
