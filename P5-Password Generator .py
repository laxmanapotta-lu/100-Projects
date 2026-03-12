# In this project with the help of code we will generate a password 

import random

lower_case=['a' ,'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
special_symbols=['~','!','@','#','$','%','^','&','*']

a=int(input(" Enter number of lower case letters you want :"))
b=int(input("Enter number of upper case letters you want :"))
c=int(input("Enter number of  digits you want :"))
d=int(input("Enter number of special symbols you want :"))



password=""

for char in range( 1,a+1):
    password+=random.choice(lower_case)

for char in range(1 ,b+1):
    password+=random.choice(upper_case)

for char in range(1 , c+1):
    password+=random.choice(digits)

for char in range(1,d+1):
    password+=random.choice(special_symbols)
print(f"Use this password this time : {password}")



