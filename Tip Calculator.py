print("welcome to the tip calculator")

Bill= int(input("What is the total bill ? : "))
Tip= float(input("How much percentage tip would you like to give 10,12,15 :"))
people= int(input("How many people to split the bill :"))
Per_person_bill =float(Bill*Tip/100 + Bill)/people
round(Per_person_bill,2)
print(" Bill per person is : " + str(Per_person_bill))