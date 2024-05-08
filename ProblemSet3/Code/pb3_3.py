import pprint as pp

def compute_opt(L):
    n = len(L)
    M = [[0] * (n) for _ in range(n)]

    for i in range(n):
        for j in range(n - i):
            if i == 0:
                M[i][j] = [0, L[j], None, None]
            elif i == 1:
                M[i][j] = [
                    M[i - 1][j][1] * M[i - 1][j + 1][1],
                    max(M[i - 1][j][1], M[i - 1][j + 1][1]),
                    (i - 1, j),
                    (i - 1, j + 1),
                ]
            else:
                k = 0
                min_0 = float("inf")
                while k < i:

                    val = (
                        M[k][j][0]
                        + M[i - k - 1][j + k + 1][0]
                        + (M[k][j][1] * M[i - k - 1][j + k + 1][1])
                    )

                    if val < min_0:

                        min_0 = val

                        M[i][j] = [
                            min_0,
                            max(M[k][j][1], M[i - k - 1][j + k + 1][1]),
                            (k, j),
                            (i - k - 1, j + k + 1),
                        ]

                    k += 1

    return M, M[n - 1][0][0]

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, OPT, n):
        #n = len(OPT[0])
        self.root = TreeNode()
        
        #print(OPT)
        #return
        sin = OPT[n - 1][0][2]
        des = OPT[n - 1][0][3]
        
        if sin is None and des is None:
            self.root.val = OPT[n - 1][0][1]
            return self
        
        si, sj = sin
        di, dj = des
        
        self.root.val = OPT[n - 1][0][0] - (OPT[si][sj][0] + OPT[di][dj][0])
        print(self.root.val)
        
        self.create_tree_recursive(OPT, self.root, si, sj)
        self.create_tree_recursive(OPT, self.root, di, dj)
        
        return self

    def create_tree_recursive(self, OPT, root, i, j):
        sin = OPT[i][j][2]
        des = OPT[i][j][3]
        v = TreeNode()
        if sin is None and des is None:
            v.val = OPT[i][j][1]
            root.children.append(v)
            print(v.val)
            return
        
        si, sj = sin
        di, dj = des
        
        v.val = OPT[i][j][0] - (OPT[si][sj][0] + OPT[di][dj][0])
        root.children.append(v)
        print(v.val)
        
        self.create_tree_recursive(OPT, v, si, sj)
        self.create_tree_recursive(OPT, v, di, dj)

    def print_tree(self, node, depth=0):
        if node is None:
            return
        print("  " * depth + str(node.val))
        for child in node.children:
            self.print_tree(child, depth + 1)

C = [1, 3, 4, 3, 2, 2, 3, 4, 5, 6, 2, 1, 2, 3]
M, OPT = compute_opt(C)
tree = Tree().create_tree(M, len(C))

print("Valore ottimo: ", OPT)
pp.pprint(M)


c = tree.root
    
tree.print_tree(tree.root)




