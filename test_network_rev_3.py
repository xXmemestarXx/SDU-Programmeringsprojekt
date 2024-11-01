from network import *
import comparator_rev_4 as Comp
import random
print(f"------- test 1 start -------")
Net_1 = empty_network()
Com_1 = Comp.make_comparator(0,1)
Com_2 = Comp.make_comparator(1,2)
Com_3 = Comp.make_comparator(0,2)
append(Com_1,Net_1)
append(Com_2,Net_1)
append(Com_3,Net_1)

v=[1,2,0,4]
print(f"List listi contains before: {v}\n")
print(f"List listi contains after: {apply(Net_1,v)}")
print(f"------- test 1 end -------")
print(" ")
print(f"------- test 2 start -------")
Net_2 = empty_network()
u=[10,9,8,7,6,5,4,3,2,1,0]
lengd=len(u)
for i in range(lengd-1):
    for j in range(lengd-1):
        Com_4 = Comp.make_comparator(j,j+1)
        append(Com_4,Net_2)

#append(Comp.make_comparator(lengd,lengd-1),Net_2)
print(f"List listi contains before: {u}\n")
print(f"List listi contains after: {apply(Net_2,u)}")
print(f"------- test 2 end -------")
print(" ")




print(f"------- test 3 start -------")
Net_2 = empty_network()
u=[]
for i in range(25):
    u.append(random.randint(0,100))
lengd=len(u)
for i in range(lengd-1):
    for j in range(lengd-1):
        Com_4 = Comp.make_comparator(j,j+1)
        append(Com_4,Net_2)
print(Net_2)
print(f"List listi contains before: {u}\n")
print(f"List listi contains after: {apply(Net_2,u)}")
print(f"------- test 3 end -------")



print(f"------- test 4 start -------")
print(f"This is the network and list from the first project introduction")
print(" ")
Net_4 = empty_network()
Com_10 = Comp.make_comparator(0,1)
Com_20 = Comp.make_comparator(2,3)
Com_30 = Comp.make_comparator(0,2)
Com_40 = Comp.make_comparator(1,3)
Com_50 = Comp.make_comparator(3,4)
Com_60 = Comp.make_comparator(1,2)
Com_70 = Comp.make_comparator(1,3)
Com_80 = Comp.make_comparator(2,3)
Com_90 = Comp.make_comparator(1,2)
append(Com_10,Net_4)
append(Com_20,Net_4)
append(Com_30,Net_4)
append(Com_40,Net_4)
append(Com_50,Net_4)
append(Com_60,Net_4)
append(Com_70,Net_4)
append(Com_80,Net_4)
append(Com_90,Net_4)

t=[5,1,7,3,2,13]
print(f"List listi contains before: {t}\n")
print(f"List listi contains after: {apply(Net_4,t)}")
print(f"------- test 4 end -------")