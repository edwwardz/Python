a = int(input("chose the month = "))

month = ['january', 'febuary', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december']

if 1 <= a <= 12:
    print("Bulan", month[a - 1])