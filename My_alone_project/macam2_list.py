# add member to list and use append
list2 = []
print ("isi list2 adalah = ", len(list2))
list2.append('angga') 
print("Know isi list adalah = ", len(list2), "item")
print ("yaitu = ", list2[0])

# add name to list use insert
list2.insert (0, 'siti')
print("this is member in list, yaitu = ", list2)

# copy the list
list3 = list2.copy()
print ("isi list 3 yaitu = ", list3)

# to combine the list
list2.extend(list3)
print("gabungan dari list 2 dan 3 adalah = ", list2)

# to delete the last item
list2.pop()
print (list2)
                   
# to make the list blank
list2.clear()
print(list2)

# to make the list sequantially 
my_team = ["angga", "castel", "edward", "reni"]
print (*my_team, sep='\n')

# use for in the list
for item in my_team : print(item.rjust(20), sep='\n')
print ("               angga")

# use to know how many item in the list
from collections import Counter
number = [1, 2, 3, 4, 1, 2, 1, 1, 1, 2, 3, 4, 5]
calculate = Counter(number)
print (calculate)
for Thisitem in calculate.items():
    print("number = ", Thisitem[0], "pop up: ", Thisitem[1], "kali")

# use to spel the sentence
print (tuple('angga'))


# function in list 
# 1. append -> add member to list
# 2. insert -> add member to list
# 3. copy -> copy the list
# 4. extend -> to combine the list
# 5. pop -> to delete the last item
# 6. clear -> to make the blank list
# 7. rjust -> use to shift(menggeser) the posision string to right 
# 8. counter -> to know how many item in the list
# 9. tuple -> to sple the sentence
#
#
