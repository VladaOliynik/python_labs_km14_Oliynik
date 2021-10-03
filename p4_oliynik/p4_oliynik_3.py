age = int(input("Enter your age: "))
if age < 0:
    print ("Error, please enter a number greater than 0")

dogYears = 0

if age >= 2:
    dogYears += 21
    age -= 2
elif age == 1:
    dogYears += 10.5
    age -= 1

dogYears += age*4

print(f"Dog`s years: {dogYears}")

