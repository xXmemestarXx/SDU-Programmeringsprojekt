import comparator as Comp
import network as Netw
import filter as Filt
import generate as Gene

print(f"")
print(f"------- test filter.py -------")
print(f"")
print(f"------- test 1 begin -------")
print(f"")
print(f"Testing make_empty_filter()")
print(f"")

filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
print(f"{filt_test} => {filt_test}")
print(f"{filt_test2} => {filt_test2}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"------- test 2 begin -------")
print(f"")
print(f"Testing net()")
print(f"")

comp_test = Comp.make_comparator(0, 1)
filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
filt_test2 = Filt.add(comp_test, filt_test2)
print(f"{filt_test} => {Filt.net(filt_test)}")
print(f"{filt_test2} => {Filt.net(filt_test2)}")
print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"------- test 3 begin -------")
print(f"")
print(f"Testing out()")
print(f"")

filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
print(f"{filt_test} => {Filt.out(filt_test)}")
print(f"{filt_test2} => {Filt.out(filt_test2)}")
print(f"")
print(f"------- test 3 end -------")
print(f"")

print(f"------- test 4 begin -------")
print(f"")
print(f"Testing get_size()")
print(f"")

filt_test = Filt.make_empty_filter(0)
filt_test2 = Filt.make_empty_filter(2)
print(f"{filt_test} => get_size(filter) => {Filt.get_size(filt_test)}")
print(f"{filt_test2} => get_size(filter) => {Filt.get_size(filt_test2)}")
print(f"")
print(f"------- test 4 end -------")
print(f"")

print(f"------- test 5 begin -------")
print(f"")
print(f"Testing is_redundant()")
print(f"")

filt_test = Filt.make_empty_filter(3)

filt_test2 = Filt.make_empty_filter(3)
filt_test2 = Filt.add(2, filt_test)

print(f"{filt_test} => Testing a single comparator is_redundant(2, filter) => {Filt.is_redundant(2, filt_test)}")
print(f"{filt_test2} => Testing duplicated comparators is_redundant(2, filter) => {Filt.is_redundant(2, filt_test2)}")
print(f"")
print(f"------- test 5 end -------")
print(f"")

print(f"------- test 5 begin -------")
print(f"")
print(f"Testing add()")
print(f"")

filt_test = Filt.make_empty_filter(2)
filt_test2 = Filt.make_empty_filter(2)
filt_test2 = Filt.add(2, filt_test2)

print(f"{filt_test} => add(2, filter) => {filt_test2}")

print(f"------- test 5 end -------")
print(f"")

print(f"------- test 6 begin -------")
print(f"")
print(f"Testing is_sorting()")
print(f"")

filt_test = Filt.make_empty_filter(4)
filt_test = Filt.add(2, filt_test)
filt_test = Filt.add(5, filt_test)
filt_test = Filt.add(8, filt_test)

filt_test2 = Filt.make_empty_filter(3)
filt_test2 = Filt.add(2, filt_test2)
filt_test2 = Filt.add(5, filt_test2)
filt_test2 = Filt.add(8, filt_test2)

print(f"{filt_test} => is_sorting(filter) => {Filt.is_sorting(filt_test)}")
print(f"{filt_test2} => is_sorting(filter) => {Filt.is_sorting(filt_test2)}")

print(f"------- test 6 end -------")
print(f"")

print(f"")
print(f"------- test generate.py -------")
print(f"")
print(f"------- test 1 begin -------")
print(f"")
print(f"Testing combine()")
print(f"")

a = [1, 2, 3]
b = [3, 2, 1]

print(f"List a {a}, list b {b} => combine(a,b) => {Gene.combine(a, b)}")

print(f"")
print(f"------- test 1 end -------")
print(f"")

print(f"------- test 2 begin -------")
print(f"")
print(f"Testing check_and_add()")
print(f"")

filt_test = Filt.make_empty_filter(3)

filt_test2 = Filt.make_empty_filter(3)
filt_test2 = Filt.add(2, filt_test)

print(f"{filt_test} => check_and_add(2, filter) => {Gene.check_and_add(2, filt_test)}")
print(f"")
print(f"Added a comparator before calling chech_and_add function")
print(f"{filt_test2} => check_and_add(3, filter ) => {Gene.check_and_add(3, filt_test2)}")

print(f"")
print(f"------- test 2 end -------")
print(f"")

print(f"------- test 3 begin -------")
print(f"")
print(f"Testing extend()")
print(f"")

n = 2
filt_test = Filt.make_empty_filter(n)
std_comp = Comp.std_comparators(n)
w = [filt_test]
filt_test2 = Gene.extend(w, n)
print(f"The standard comparators that is used {std_comp}, and n = {n}")
print(f"{filt_test} => extend(w, n) => {filt_test2}")
print(f"")

n = 3
filt_test = Filt.make_empty_filter(n)
std_comp = Comp.std_comparators(n)
w = [filt_test]
filt_test2 = Gene.extend(w, n)
print(f"The standard comparators that is used {std_comp}, and n = {n}")
print(f"{filt_test} => extend(w, n) => {filt_test2}")

print(f"")
print(f"------- test 3 end -------")
print(f"")




