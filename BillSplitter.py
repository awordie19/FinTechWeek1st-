# MVP = 
import math
 
 
subTotal = input("What is the total of your bill?\n")
people = input("How many people are you dining with? Include yourself.\n")
tip = input("Would you like to provide a gratituity?\n")
chosenTipPercentage = input("What percentage for gratituity would you like to give? Example: 15% is 15.\n")

if tip[0].lower() == "y":
    numericalTip = (int(chosenTipPercentage)/100) 
    tipTotal = int(subTotal) * int(numericalTip)
else: 
    tipTotal = 0 
    print("Okay, Mr. Krabs. We see you.")

finalTotal = int(subTotal) + int(tipTotal)
CostPerPerson = int(finalTotal)/int(people)
print ("Each person needs to pay $" + str(CostPerPerson) + ".")

  

# final = math.ceil(totalCostWithTax)
# print ("Each person must pay $" + ".")
