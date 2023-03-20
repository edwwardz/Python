menu_item = 0
namelist = []
while menu_item != 5:
    print("------------------------")
    print("1. Print list")
    print("2. add name to list")
    print("3. delete name from list")
    print("4. Mengubah data dalam list")
    print("5. get out")
    menu_item = int(input ("chose the menu = "))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print (current, "=>", namelist[current])
                current = current + 1
        else:
            print("List kosong")
        
    elif menu_item == 2:
        name = input ("Enter name = ")
        namelist.append(name)
    elif menu_item == 3:
        del_name = input ("masukan nama yang ingin di hapus = ")
        if del_name in namelist:
            # namelist.remove(del_name) dapat digunakan
            item_number = namelist(del_name)
            del namelist [item_number]
            #kode di atas hanya menhapus nama yang ada
            # kode di bawah ini menghapus semua nama
            # while del_name in namelist:
            # item_number = namelist.index(del_name)
            # del namelist [item_number] 
        else:
            print(del_name, "tidak ditemukan")
    elif menu_item == 4:
        old_name = input ("nama apa yang ingin diubah = ")

        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input ("new name = ")
            namelist[item_number] = new_name
        else:
            print(old_name, "Tidak ditemukan!")

print("sayonara")       
