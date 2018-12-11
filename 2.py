file = open("2.txt", "r")
ids = file.read().split("\n")

have2 = 0
have3 = 0

for word in ids:
    hasExactly2 = False
    hasExactly3 = False
    for char in word:
        # print("word: ", word)
        # print("char: ", char)
        # print("count: ", word.count(char))
        if word.count(char) == 2:
            hasExactly2 = True
        elif word.count(char) == 3:
            hasExactly3 = True
    if hasExactly2:
        have2 += 1
        # print("have2: ", have2)
    if hasExactly3:
        have3 += 1
        # print("have3: ", have3)

checksum = have2 * have3

print("checksum: ", checksum)

for word in ids:
    for otherWord in ids:
        diff = [i for i in range(len(word)) if word[i] != otherWord[i]]
        if len(diff) == 1:
            letters = [word[i] for i in range(len(word)) if word[i] == otherWord[i]]
            print("Common letters: ",''.join(letters))
