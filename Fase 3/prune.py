import filter as Filt

def prune(w:list[Filt.Filter], n: int) -> list[Filt.Filter]:
    """..."""
    return boring_prune(w,n)

    
def boring_prune(w, n):
    """Does something boring."""
    keep = [True for i in range(0, len(w)+1)]
    pruned = []

    for i in range(0,len(w)):
        if keep[i]:
            pruned.append(w[i])
            for j in range(i,len(w)):
                if Filt.out(w[i]) == Filt.out(w[j]):
                    keep[j] = False
    return pruned

def cool_prune(w,n):
    """Does something cool."""
    return None

