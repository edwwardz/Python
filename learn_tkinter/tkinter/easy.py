def tambah (a,b):
    return a + b

def kurang (a,b):
    return a - b

def kali (a,b):
    return a * b

def bagi (a,b):
    return a / b

print("1.Pengalian")
print("2.Pengurangan")
print("3.Pembagian")
print("4.Penambahan")
menu = int(input("Pick the meanu = "))

first = float(input("Enter the first number = "))
second = float(input('Enter the scond number = '))

if menu == 1:
    print(first, "X", second, kali(first,second))
elif menu == 2:
    print(first, '-', second, kurang(first, second))
elif menu == 3:
    print(first, '/', second, bagi(first, second))
elif menu == 4:
    print(first, '+', second, tambah(first, second))
