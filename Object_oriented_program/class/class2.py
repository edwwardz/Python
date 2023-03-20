class mahasiswa (): # <- Make class
    name = 'name'  # <- atribut
    sleep = 'sleep'

    def __init__ (self):
        print ("this is init")

    def belajar (self, kondisi): # self digunakan untuk menentukan 
        print (self.name, "sedang belajar", kondisi) # -> fungction di dalam class disebut method
        return kondisi

    def tidur (self, kondisi):
        print (self.sleep, "Want to sleep", kondisi)

angga = mahasiswa() # angga->instenses
castellani = mahasiswa() # mahasiswa->class
budi = mahasiswa()


budi.sleep = "Vito Budi Bratta" 
castellani.name = "Maria Castellani Emerald"
angga.name = "Edward Anugrah Angga"

castellani.belajar("dengan giat") # after self we can use argumen:
budi.tidur("dengan pulas") # example = def belajar (self, argumen):
angga.belajar("tapi sedikit lazy")
