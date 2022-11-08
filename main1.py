#Ask name
name = ""
while name == "":
    name = input("What is your name ? ")

#Ask age
age = 0
while age == 0:
    age_str = input("What is your age ? ")
    try:
        age = int(age_str)
    except:
        print("ERROR: Enter your age.")






#Output
print("Your name is " + name + ", you are " + str(age) + " years old.")
print("Next year you will be " + str(age+1) + " years old, HAL.")


# n LOOPS_______________________
n = 0          # Create VARiable
#print(n)
# n = 10       # VARiable REAFFECTation
# print(n)
# print(n)
# print("START of While LOOP")
# while n < 10:                      # Boucle WHILE = "tnt que" ...
#     print("VALeur de n: " + str(n))
#     n = n + 1                            # INCREMENT (TO EXIT While LOOP)
# print("End of While LOOP")
#WHILE & W.Not LOOP________________________
# password = ""
# while not password == "pi":
#     password = input("What is your password ? ")
#     print("Correct password, access granted.")
#SUPPRIMER
#str-›int
#age : "30" / int(age) : 25 / age_next : "31"
# name = "Python"
#age = 30
# age = 31
# print(type(name))
# print(type(age))
# str(30) -› "30"
# print('Thank you, have a nice day !')
# else:
#FIN SUPPR._______________________________________________________________
