'''
x = 5
y = "jhone"
print(x)
print(y)
#out put is= 5 jhone (but out gaves downly)


#test
x , y , z = 10 ,20 , 30
print(x)
FN = "Dulsath"
LN = "Randeepana"
print(FN , LN)
#test 2
F = input("Enter your first name: ")
L = input("Enter your last name: ")
A = int(input("Enter your age: "))
print(F , L , A ) 
print("---------------------------------------------------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
'''
'''
#test 3
hi = "ndoowijowjowewekwmwewemdwmwemwem"
print(hi)

bi = "msmsqq"
print(bi)

print(hi + bi )
print("---------------------------------------------------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
'''
'''
#test 4
M = int(input("Type your marks: "))
if M >= 90:
    print("A+")
else:
    if M >= 75:
        print("A")
    else:
        if M >= 65:
            print("B")
        else:
            if M >= 55:
                print("C")
            else:
                if M >= 35:
                    print("S")
                else:
                    print("F") 
print("------------------------------------------------------------------------------------")
'''

#test 5
#making a movie site
print("------------------------------------------------------------------------------------")
name_user = input("Enter your name: ")
age_user = int(input(f'Enter your age: '))
sex = input("Male or Female: ")

print("")
print("dear",name_user , ", How can i help you today?")
'''
print(f"Hi{name_user},How can i help you today: ")
'''
MEG_2 = 1
DEAD_RACING_3 = 2
THE_LOST = 3 
SUN_FUN_RUN = 4

print("")
print(f'We have avalible to watch {MEG_2} , {DEAD_RACING_3} , {THE_LOST} , {SUN_FUN_RUN}')
user_choice = int(input("Enter your choise using only 1,2,3,4 : "))

print("")
if user_choice == 1:
    print("Meg 2")
else:
    if user_choice == 2:
        print("Dead Racing 3")
    else:
        if user_choice == 3:
            print("The Lost")
        else:
            user_choice == 4
            print("SUN FUN RUN")


'''
user_birthY = int(input("Enter your birth year: "))
user_birthM = input("Enter your birth month: ")
user_birthD = int(input("Enter your birth day: "))
'''
