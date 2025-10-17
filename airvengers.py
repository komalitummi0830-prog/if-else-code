age=int(input("enter the person's age:"))
if age <0:
    print("invalid age ,please enter a valid age.")
elif age<=1:
    print("the person is an infant.")
elif age<=12:
    print("The person is a Child.")
elif age <= 19:
    print("The person is a Teenager.")
else:
    print("The person is an Adult.")




