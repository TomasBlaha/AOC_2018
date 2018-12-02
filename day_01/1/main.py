frequency = 0
frequencyChanges = open("./1.input", "r").read().splitlines()

for change in frequencyChanges:
    frequency += int(change)

print(frequency)
