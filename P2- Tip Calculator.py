# Tip Calculator in the restuarants and hotels to find total amount and some calculations
print("Welcome to tip Calculator of Laxmana ")
total_bill = float(input(" Enter the total bill by user = "))
tip_percentage=float(input(" Enter the tip percentage you want to give = "))
no_of_persons=int(input("Enter how many persons you are = "))

total_amount_to_pay = (total_bill *  float(100+tip_percentage)) / 100

print(f"total_amount = {total_amount_to_pay}")

amount_per_person = total_amount_to_pay/no_of_persons
print(f"amount_per_person = {amount_per_person}")