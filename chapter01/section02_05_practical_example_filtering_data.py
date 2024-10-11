# List of ages
ages = [22, 35, 17, 40, 15, 27, 30]

# Filter ages greater than or equal to 18
adult_ages = []
for age in ages:
    if age >= 18:
        adult_ages.append(age)

print("Adults:", adult_ages)
