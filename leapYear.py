print("........To find Leap Year.........")
try:
    year = int(input("Enter the year : "))
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year = ",year,"Leap Year")
        else:
            print("Year = ",year," is not Leap Year")
    elif year % 4 == 0:\
        print("Year = ", year, "Leap Year")
    else:
        print("Year = ", year, "is not Leap Year")
except Exception as e:
    print("please enter interger number ",e)






