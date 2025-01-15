import filter as Filt
import generate2 as Gene

n = 4
filt_test = Filt.make_empty_filter(n)
w = [filt_test]
#filt_test2 = Gene.extend(w, n)
#print(filt_test)
#print(len(w))
#print(filt_test2)


print(Gene.extend(w, n))