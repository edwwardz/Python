score = 0
score1 = [] # nama 
score2 = [] # token

while score != 4:
    print('-_-'*20)
    print ("Hello")
    print("Selamat datang di tempat penerimaan rapot online")
    print ("Ini merupakan pilahanya")
    print ("mohon setelah selesai melihat nilai rapor tolong segera absen")
    print("1. Nama anak dan nomor token")
    print("2. nama anak yang sudah melihat rapor")
    print("3. nilai rapor")
    score = int(input("Silahkan masukan option = "))
    if score == 1:
        def nama (name,token):
            print("Nomor token",name, "adalah", token)
        nama('Rudi', 1234)
        nama('Angga', 1256)
        nama('Castellani', 1278)
    
    elif score == 2:
        current = 0
        if len(score1) > 0:
            while current < len(score1):
                print(current,'-> nama anak anda adalah', score1[current],'dengan nomor token', score2)
                current = current + 1
        else:
            print ("M-A-A-F")
            print("M-A-S-I-H  K-O-S-O-N-G")
    
    elif score == 3:
        print ("Haloo welcome")
        token = int(input("Silahkan masukan token anak anda = "))
        if token == 1234:
            name = input ("Silahkan Masukan nama anak anda = ")
            def nama (ipa=90,ips=80,bahasa=70):
                print ("Anak anda",name,"mendapatkan nilai di UTS adalah sebagai berikut:")
                print ("nilai Ipa anak anda adlah",ipa)
                print ("nilai Ips anak anda adlah",ips)
                print ("nilai bahasa anak anda adalah",bahasa)
                print ("rata rata nilai UTS anak anda adalah",(ipa+ips+bahasa)/3)
            nama()
            score1.append(name)
            score2.append(token)
            
        elif token == 1256:
            name = input("Masukan nama anak anda")
            def nama (ipa=80,ips=90,bahasa=85):
                print ("Anak anda",name,"mendapatkan nilai di UTS adalah sebagai berikut:")
                print ("nilai Ipa anak anda adlah",ipa)
                print ("nilai Ips anak anda adlah",ips)
                print ("nilai bahasa anak anda adalah",bahasa)
                print ("rata rata nilai UTS anak anda adalah",(ipa+ips+bahasa)/3)
            nama()
            score1.append(name)
            score2.append(token)

        elif token == 1278:
            name = input("Masukan nama anak anda = ")
            def nama (ipa=85,ips=80,bahasa=90):
                print ("Anak anda",name,"mendapatkan nilai di UTS adalah sebagai berikut:")
                print ("nilai Ipa anak anda adlah",ipa)
                print ("nilai Ips anak anda adlah",ips)
                print ("nilai bahasa anak anda adalah",bahasa)
                print ("rata rata nilai UTS anak anda adalah",(ipa+ips+bahasa)/3)
            nama()
            score1.append(name)
            score2.append(token)
        else:
            print ("Maaf nama/token anda tidak ditemukan silahkan coba lagi")
        
print("T-E-R-I-M-A  K-A-S-I-H")
print("G-O-O-D  B-Y-E")
        

    
    


                
        

