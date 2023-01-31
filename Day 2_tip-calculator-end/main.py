'''
Welcome to the tip calculator
What was the total bill? $124.56
What percentage tip would you like to give? <Any positive integer>
How many people to split the bill? 7
Each person should pay: <Total tip/Number of people>
'''

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent =  int(input("What percentage tip would you like to give? "))
no_of_people = int(input("How many people to split the bill? "))
total_tip = (tip_percent / 100.0)*bill
total_bill = total_tip + bill
print(f"Each person should pay: ${round(total_bill/no_of_people, 2)}")