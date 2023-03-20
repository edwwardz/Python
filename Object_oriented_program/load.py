import time

load = '$'
count = 0

for t in range (101):
    time.sleep(0.1)
    print(f'\rloading {t}% [{load}]', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '$'

print('\nYou Aplication can acses')
