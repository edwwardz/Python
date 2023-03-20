# | -> atau
import re
import random

a = ["Hallo to", "Hello", "How are you"]


while True:
    x = input("User\t:")
    if re.findall(r'Hello|hai|halo', x):
        print("Bot\t:",random.choice(a))
    else:
        print("Bot:\t Sorry eror")
        break