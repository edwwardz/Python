def pembalik (teks):
    list1 = []
    score = ''
    for i in range(len(teks)):
        list1.append(teks[i])
    while list1 != []:
        score += list1.pop()
    return score
a = input("enter you text = ")
print("Hasil = ", pembalik(a))