from math import sqrt, ceil
def tetris(moves: list, n: int, m: int):
    sqrt_n = ceil(sqrt(n))
    xs = [0] * n
    max_hs = [0] * sqrt_n
    plain = [True] * sqrt_n
    for i, (x, w, h) in enumerate(moves):
        #print(i, x, w, h)
        x = x - 1
        if x == 0 : z = x + w 
        else: z = x + w -1
        x_start = x // sqrt_n # chunck iniziale
        x_end = (z - 0.001) // sqrt_n # chunk finale
        x_end = int(x_end)
        k = 0
        if x_start == x_end and w == sqrt_n:
            max_hs[x_start] = max_hs[x_start] + h
            plain[x_start] = True
            k = max_hs[x_start]
        elif x_start == x_end:
            k = max(xs[x:z+1])
            k += h
            for j in range(x, z + 1): # O(sqrt_n)
                xs[j] = k 
            if max_hs[x_start] < k: max_hs[x_start] = k
            plain[x_start] = False
        else:
            plain[x_start] = plain[x_end] = False
            for i in xs[x - 1: x_start * sqrt_n +1]:
                if i > k: k = i
            for i in max_hs[x_start : x_end ]:
                if i > k: k = i
            for i in xs[x_end * sqrt_n - 1: z + 1]:
                if i > k: k = i
            k += h
            for i in range(len(xs[x: x_start * sqrt_n + 1])):
                xs[x + i] = k 
            for i in range(len(max_hs[x_start + 1: x_end - 1])):
                max_hs[i + x_start + 1] = k 
                plain[i + x_start + 1] = True
            for i in range(len(xs[x_end * sqrt_n - 1: z +1])):
                xs[(x_end * sqrt_n) + i - 1] = k 

        if k > m: return i + 1
    
    return -1


print(tetris([(1,  3, 12), (6, 3, 3), (2, 5, 2), (8, 1, 5), (4, 2, 1), (2, 2, 0), (4, 3, 7)], 8, 16))
