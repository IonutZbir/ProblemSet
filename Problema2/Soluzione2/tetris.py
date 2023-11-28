from math import sqrt, ceil
def tetris(moves: list, n: int, m: int) -> int:
    sqrt_n = ceil(sqrt(n))
    xs = [0] * n
    chunk = [[0, True]] * sqrt_n
    for i, (x, w, h) in enumerate(moves):
        #print(i, x, w, h)
        z = x + w - 1
        x_start = ceil(x / sqrt_n) # chunck iniziale
        x_end = ceil(z / sqrt_n) # chunk finale
        if x_start == x_end:
            max_h = max(xs[x:z+1])
            for j in range(x, z + 1): # O(sqrt_n)
                xs[j] = max_h
            chunk[x_start][0] = max_h
            chunk[x_start][1] = False

tetris([(1,  3, 12), (6, 3, 3), (2, 5, 2), (8, 1, 5), (4, 2, 3), (2, 2, 2), (4, 3, 7)], 8, 16)
    
