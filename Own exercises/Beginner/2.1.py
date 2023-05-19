numbers = [71, 3, 754, 23, 5, 71, 96, 75, 24, 754, 96]
uniques = []

numbers.sort()
for i in numbers:
    if i not in uniques:
        uniques.append(i)

print(uniques)
