import filter as Filt

def prune(w:list[Filt.Filter], n: int) -> list[Filt.Filter]:
    """..."""
    return boring_prune(w,n)

    
def boring_prune(w, n):
    """Does something boring."""
    uniq_outs = [Filt.out(w[0])]

    keep = [0]
    
    res = []

    for i in range(1, len(w)):
        if Filt.out(w[i]) not in uniq_outs:
            uniq_outs.append(Filt.out(w[i]))
            keep.append(i)
            
    for i in range(0,len(keep)):
        res.append(w[keep[i]])
    return res

def cool_prune(w,n):
    """Does something cool."""
    return None

