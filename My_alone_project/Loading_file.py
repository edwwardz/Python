number = 0
while number < 101:
	a = input(" Masukan Kode : ")
	if a == "start":
		for i in range (0,101,1):
			print("Aplikasi sedang loading....",i,"Loading")
			if i == 100:
				print("Aplikasi siap di jalankan...",i,"Loading")
