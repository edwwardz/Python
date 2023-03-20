a_var = 10 # variabel global
b_var = 15
e_var = 25

def a_func (a_var):
	print ("dalam a_func a_var =", a_var)
	b_var = 100 + a_var
	d_var = 2 * a_var
	e_var = 100 / 50 # variabel local
	print ("dalam a_func b_var =", b_var)
	print ("dalam a_func d_var =", d_var)
	print ("dalam a_func e_var =", e_var)
	return b_var + 10
	return d_var * 2

c_var = b_var # c variabel didapatkan dari b_var= (115, di return atau dikeluarkan dan ditambah 10), hasilnya 
d_var = 10			  # sama dengan 125
print ("a_var =", a_var)
print ("b_var =", b_var)
print ("c_var =", c_var)
print ("d_var =", d_var)
print ("e_var =", e_var)


#b var = 110,120
#d var = 20
#e var = 25
#c 
#
#
#
#
