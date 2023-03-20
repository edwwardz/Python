print("Selamat Datang di ATM saya")
print("Pilih Option :")
print("1. Check Saldo saya")
print("2. Ambil uang saya")
print("3. Tabung uang saya")
option=int(input("Silahkan Pilih option :"))
if option==1:
	print("Uang kamu sekarang berjumlah Rp.2.000.000")
elif option==2:
	print("Uang kamu Berjumlah Rp.2.000.000")
	print("1. Rp.100.000")
	print("2. Rp.200.000")
	print("3. Rp.300.000")
	print("4. Rp.400.000")
	Uang_kamu=2000000
	option2=int(input("Option :"))
	if option2==1:
		hasil=Uang_kamu-100000
		print("Uang kamu sekarang berjumlah :",hasil)
	elif option2==2:
		hasil2=Uang_kamu-200000
		print("Uang kamu sekarang berjumlah :",hasil2)
	else:
		print("Anda harus memsukan option Angka!")
elif option==3:
	Uang_kamu=2000000
	print("Uang berjumlah Rp.2.000.000, Mau nabung berapa?")
	option3=int(input("Masukan Jumlah Uang yang mau ditabung :"))
	hasil3=Uang_kamu+option3
	print("Jumlah uang kamu Sekarang adalah :",hasil3)
	 


