print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10,12 or 15? \n"))
split = int(input("How many people to split the bill?\n"))

result = (bill/split)*(1+(tip/100))
final_result = round(result, 2)
final_result = "{:.2f}".format(result)
print("Each person will have to pay Rs",final_result)
