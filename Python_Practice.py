print("Hello Wrold")
#ask user to provide score
score=int(input("what is your score, please round to 0 decimal places?"))
#evalue the score and print grade
#if score>=90:
#    print("Your Grade is an A.")
#else:
#    if score>=80:
#        print("Your grade is a B")
#    else:
#        if score>=70:
#            print("Your grade is a C")
#        else:
#            if score>=60:
#                print("Your grade is a D")
#            else:
#                print("Your grade is an F")
if score>=90:
    print("Your grade is an A.")
elif score>=80:
    print("Your grade is a B.")
elif score>=70:
    print("Your grade is a C.")
elif score>=60:
    print("Your gade is a D")
else:
    print("Your grade is a F")