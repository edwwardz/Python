menupesananA = []#price
menupesananB = []#name order
menupesananC = []#Total price
menupesananD = []#amount 
menu = 0
while menu != 9:
    print("-_-_-_-_-_-_-_-_-_-_-_-")
    print("Welcome to online supermarket")
    print("PLEASE ENTER YOU OPTION")
    print("1. Troli ")
    print("2. Online supermarket")
    print("3. Delete your package form troli")
    print("4. change you package")
    print("5. Paying")
    print("press 9 to stop")
    menu = int(input ("enter you option = "))
    if menu == 1:
        current = 1
        if len(menupesananB) > 0:
            while current < len(menupesananB):
                print(current, "=>",menupesananB[current], "=>", "Rp.",menupesananA[current], "Amount = ", menupesananD[current],"Total price = ", menupesananC[current])
                current = current + 1
        else:
            print ("T-R-O-L-I-")
            print("K-O-S-O-N-G") 





    elif menu == 2:
        print("1. snack => Rp.7.000")
        print("2. sprite => Rp.5.000")
        print("3. french fries => Rp.9.000 ")
        pesanan = input ("enter masukan nama pesanan-mu = ")
        if pesanan == 'snack':
            harga = 7000
            your_money = int(input("enter you money = "))
            amount = int(input("Enter you amount = "))
            if your_money < harga*amount:
                print("Sorry you money is lacking")
            elif your_money >= harga*amount:
                print("You want to buy ",pesanan,"amount is = ", amount,"dengan harga",harga)
                print("you total buy  = ", amount*harga)
                print("your change  = ", your_money-harga*amount)
                menupesananB.append(pesanan)
                menupesananA.append(harga)
                menupesananC.append(amount*harga)
                menupesananD.append(amount)
    
        elif pesanan == 'sprite':
            harga = 5000
            your_money = int(input("enter you money = "))
            amount = int(input("Enter you amount = "))
            if your_money < harga*amount:
                print("Sorry you money is lacking")
            elif your_money >= harga*amount:
                print("You want to buy ",pesanan,"amount is = ", amount,"dengan harga",harga)
                print("you total buy  = ", amount*harga)
                print("your change  = ", your_money-harga*amount)
                menupesananB.append(pesanan)
                menupesananA.append(harga)
                menupesananC.append(amount*harga)
                menupesananD.append(amount)
           
        elif pesanan == 'french fries':
            harga = 9000
            your_money = int(input("enter you money = "))
            amount = int(input("Enter you amount = "))
            if your_money < harga*amount:
                print("Sorry you money is lacking")
            elif your_money >= harga*amount:
                print("You want to buy ",pesanan,"amount is = ", amount,"dengan harga",harga)
                print("you total buy  = ", amount*harga)
                print("your change  = ", your_money-harga*amount)
                menupesananB.append(pesanan)
                menupesananA.append(harga)
                menupesananC.append(amount*harga)
                menupesananD.append(amount)
            
    if menu == 3:
        del_item = input ("enter The groceires you want to delete = ")
        if del_item in menupesananB:
            item_number = menupesananB.index(del_item)
        price = input("enter the price of the item =  ")
        if price in menupesananA:
            item_number = menupesananA.index(price)
        del menupesananB[item_number]
        del menupesananA[item_number]
        print("okay you package is delete...")
    



    if menu == 4:
        old = input("enter the groceires you want to change = ")

        if old in menupesananB:
            item_number = menupesananB.index(old)
        old_price = input("enter the price of you item = ")
        if old_price in menupesananA:
            item_number = menupesananA.index(old_price)
        old_amount = input("enter the amount of item = ")
        if old_amount in menupesananD:
            item_number = menupesananD.index(old_amount)
            old_total = (" ", old_amount*old_price)
            if old_total in menupesananC:
                item_number = menupesananC.index()
    

        print("1. snack => Rp.7.000")
        print("2. sprite => Rp.5.000")
        print("3. french fries => Rp.9.000 ")
        new = input ("enter the new item you want to buy = ")
        if new == 'snack':
            harga = 7000
            money = int(input("enter you money = "))
            jumlah = int(input("enter you amount = "))
            if money < harga*jumlah:
                print("Your money is lacking....")
                print("please enter the price as stated")
            elif money >= harga*jumlah:
                print("you want to buy", new, "The price", harga, "and the total",jumlah)
                print("You total buy is ", harga*jumlah)
                print("You change is = ", money-harga*jumlah)
                menupesananB[item_number] = (new)
                menupesananA[item_number] = (harga)
                menupesananC[item_number] = (jumlah*harga)
                menupesananD[item_number] = (jumlah)

        elif new == 'sprite':
            harga = 5000
            money = int(input("enter you money = "))
            jumlah = int(input("enter you amount = "))
            if money < harga*jumlah:
                print("Your money is lacking....")
                print("please enter the price as stated")
            elif money >= harga*jumlah:
                print("you want to buy", new, "The price", harga, "and the total",jumlah)
                print("You total buy is ", harga*jumlah)
                print("You change is = ", money-harga*jumlah)
                menupesananB[item_number] = (new)
                menupesananA[item_number] = (harga)
                menupesananC[item_number] = (jumlah*harga)
                menupesananD[item_number] = (jumlah)           
              
        elif new == 'french fries':
            harga = 9000
            money = int(input("enter you money = "))
            jumlah = int(input("enter you amount = "))
            if money < harga*jumlah:
                print("Your money is lacking....")
                print("please enter the price as stated")
            elif money >= harga*jumlah:
                print("you want to buy", new, "The price", harga, "and the total",jumlah)
                print("You total buy is ", harga*jumlah)
                print("You change is = ", money-harga*jumlah)
                menupesananB[item_number] = (new)
                menupesananA[item_number] = (harga)
                menupesananC[item_number] = (jumlah*harga)
                menupesananD[item_number] = (jumlah)




        


