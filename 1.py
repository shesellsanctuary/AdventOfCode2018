
file = open("1.txt", "r")
freq = file.read().split("\n")

frequency = 0
loop = []
loop.append(frequency)
foundDupl = False

for num in freq:
    frequency = frequency + int(num)
print("final frequency: ",frequency)

frequency = 0
d = {}

while foundDupl == False:
    for num in freq:
        frequency = frequency + int(num)
        if frequency in d:
            print("first duplicate: ", frequency)
            foundDupl = True
            break
        d[frequency] = False

