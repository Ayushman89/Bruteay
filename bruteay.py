                                                             
import string 

import random

print("made by Ayushman Dutta")

data_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
chardData = list(data_list)

password = str(input("password"))

myguess =""
while(myguess!=password):
 myguess = random.choices(chardData, k=len(password))
 print("".join(myguess))
 myguess = "" .join(myguess)
 print("")
