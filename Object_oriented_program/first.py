"""Pemrograman berorientasi objek atau dalam bahasa inggris disebut Object Oriented Programming (OOP) adalah 
paradigma atau teknik pemrograman di mana semua hal dalam program dimodelkan seperti objek dalam dunia nyata. 
Objek di dunia nyata memiliki ciri atau attribut dan juga aksi atau kelakuan (behaviour).
semua apapun itu diangap sebagai object, semuanya. 
example:
template -> class Hero -> Template dibagi menjadi 2:
1. atribut -> nama, power, defense. 
2. method -> sesuatu yang bisa dilakukan hero atau class(Hero) -> menyerang (), bertahan(), bergerak()
contoh lain adalah meja: 
meja adalah atribut dan methodnya adalah meja bisa dibalik dan didirikan.

object -> name of object or instance(Object mengambil semua Class hero, mulai dari atribut and method)

Kita misalkan sebuah mobil. Mobil memiliki ciri punya ban, stang, kursi, pedal gas, rem, dan lain sebagainya. Ada juga 
ciri warna, atau tahun keluaran berapa. Selain punya ciri, mobil juga punya aksi atau sesuatu yang bisa dilakukan 
olehnya. Misalnya, ketika pedal diinjak apa yang terjadi. Ketika di rem apa yang terjadi, dan lain sebagainya."""

class Hero: #Template
    pass

hero1 = Hero() # Object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.nama = "Sniper"
hero1.health = "100"

hero2.nama = "Van"
hero2.health = "200"

hero3.nama = "Angga"
hero3.health = "1000"

print(hero1)
print (hero1.__dict__)
print(hero1.nama)