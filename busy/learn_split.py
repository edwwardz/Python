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