#opening statement
print("Welcome to Kodi's tip calculator\n")

#take in the total bill amount.
billInput = float(input("What was the total bill amount?\n$"))

#unit tests below
print("start test billStr")
print(billInput)
print(type(billInput))
print("end test")

#grab the percentage, again we only want a number
tip = int(input("What percentage tip would you like to give? The usual is 10, 12 and 15%.\n"))

#heres where we make a head count to split the calculated percentage
headCount = int(input("How many people will split this bill?\n"))

#Lets get into some simple math, we got this! turn the tip into a percentage.
tipPercent = tip / 100

#here we multiply the bill with the tip percent to find the actual value
totalTip = billInput * tipPercent

#add the total tip to the total bill
totalBill = billInput + totalTip

#nowwww divide it by how many people are paying
billPerPerson = totalBill / headCount

#we're not a gastation in america we dont use five decimal places and round, make it output only to the fourth place
finalAmount = round(billPerPerson, 2)

#now print it out! so theres a string with the variable inserted and formatted with :.2f to always print to the second decimal to the right
print(f"Each person should pay ${finalAmount:.2f}")

