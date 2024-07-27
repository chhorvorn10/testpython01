# weight = float(input("Input your weight: "))
# height = float(input("Input your height: "))
# bmi = weight // height ** 2
# print("Your BMI = ", int(bmi))


print("====Welcome to the Tip Calculator====")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give?"))
num_people = int(input("How many people to split the bill? "))
tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount
amount_per_person = total_amount / num_people
print(f"Each Person should pay: ${amount_per_person}")
