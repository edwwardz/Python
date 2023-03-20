gudang = []
hasil = ''

a = input("")


i = 0   
while i < len(gudang) :
    if gudang[i] == '/' :
        gudang.pop(i)
        hasil = gudang.pop(i-1)/gudang.pop(i-1)
        gudang.insert(i-1, hasil)
        i = 0
        i+=1
            