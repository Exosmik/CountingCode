# This code makes you input a number. If the number is above 67 it will 
# create a string saying the number in terms of 67 and remainder. e.g if you input 135 it will say 67+67+1. If the number is below 67 it will
# subtract the number from 67 and give the same result. e.g if you input 50 it will say 67-17.

SelectedNumber = int(input("Enter the next number: "))
if SelectedNumber < 67:
    BelowResult = 67 - SelectedNumber
    print("The result is: 67-", BelowResult)
elif SelectedNumber == 67:
    print("The result is: 67")
elif SelectedNumber > 67:
    Aboveresult = ""
    while SelectedNumber >= 67:
        Aboveresult = Aboveresult + "67+"
        SelectedNumber = SelectedNumber - 67
    if SelectedNumber > 0:
        Aboveresult = Aboveresult + str(SelectedNumber)
    else:
        Aboveresult = Aboveresult.rstrip("+")
    print("The result is:", Aboveresult)