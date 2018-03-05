totalBill = float(raw_input("Total bill amount? "))
service = raw_input("Level of Service? ").lower()

if service == "good":
    tip = totalBill * .20
    print "Tip amount: $%.2f" %tip
elif service == "fair":
    tip = totalBill * .15
    print "Tip amount: $%.2f" %tip
elif service == "bad":
    tip = totalBill * .10
    print "Tip amount: $%.2f" %tip
else:
    print "Invalid input. They can't be that bad"