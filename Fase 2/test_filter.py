import filter as filt
import network as Netw
import comparator as Comp

n = int(input("n: "))
filt_test = filt.make_empty_filter(n)
filt_test = filt.add(2, filt_test)
filt_test = filt.add(5, filt_test)
filt_test = filt.add(8, filt_test)
print(filt_test)
# for i in range(len(filt_test.n)):
#     print(f"Comparator i: {Comp.min_channel(filt_test.n[i])}, Comparator j: {Comp.max_channel(filt_test.n[i])}")
# print(filt.is_sorting(filt_test))

print(filt.is_any_sorting(filt_test))