from filter import *

n = 2
test_comp = Comp.make_comparator(0, 1)
test_filter = make_empty_filter(n)
test_filter = add(test_comp, test_filter)
print(is_sorting(test_filter))
print(test_filter)

