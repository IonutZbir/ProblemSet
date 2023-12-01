from math import sqrt, ceil
def tetris(moves: list, n: int, m: int) -> int:
    sqrt_n = ceil(sqrt(n))
    xs = [0] * n
    max_hs = [0] * sqrt_n
    plain = [True] * sqrt_n
    for l, (x, w, h) in enumerate(moves) :
        #print(i, x, w, h)
        x = x - 1
        z = x + w - 1
        x_start = x // sqrt_n # chunck iniziale
        x_end = (z) // sqrt_n # chunk finale
        k = 0
        if x_start == x_end and w == sqrt_n :
            max_hs[x_start] = max_hs[x_start] + h
            plain[x_start] = True
            k = max_hs[x_start]

        elif x_start == x_end :
            k = max(xs[x:z+1])
            k += h
            for j in range(x, z + 1) : # O(sqrt_n)
                xs[j] = k 
            if max_hs[x_start] < k : max_hs[x_start] = k
            plain[x_start] = False

        else:
            if plain[x_start] == True :
                k = max_hs[x_start]
            else:
                i = x
                while i < ((x_start + 1) * sqrt_n) :
                    if xs[i] > k :
                        k = xs[i]
                    i += 1

            i = x_start + 1
            while i < x_end :
                if max_hs[i] > k : k = max_hs[i]
                i += 1

            if plain[x_end] == True and k < max_hs[x_end] :
                k = max_hs[x_end]
            else:
                i = x_end * sqrt_n 

                while i <= z:
                    if xs[i] > k :
                        k = xs[i]
                    i += 1

            k += h

            i = x

            while i < ((x_start + 1) * sqrt_n) :
                xs[i] = k
                if xs[i] > max_hs[x_start] :
                    max_hs[x_start] = xs[i]
                i += 1

            i = x_start + 1
            while i < x_end :
                max_hs[i] = k
                plain [i] = True
                i += 1

            i = x_end * sqrt_n 
            while i <= z :
                xs[i] = k
                if xs[i] > max_hs[x_end] :
                    max_hs[x_end] = xs[i]
                i += 1

            plain[x_start] = plain[x_end] = False


        if k > m: return l + 1

    return -1


print(tetris([(1,  3, 12), (6, 3, 3), (2, 5, 2), (8, 1, 5), (4, 2, 3), (2, 2, 0), (4, 3, 7)], 8, 16))
