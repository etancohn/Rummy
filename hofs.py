
def filter(f, L):
    res = []
    for e in L:
        if f(e):
            res.append(e)
    return res


def map(f, L):
    res = []
    for e in L:
        res.append(f(e))
    return res

def foldl(g, z, L):
    if len(L) == 0:
        return z
    x = L[0]
    xs = L[1:]
    return foldl(g, g(x, z), xs)


 


