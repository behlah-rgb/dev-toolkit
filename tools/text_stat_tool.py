text = input("Enter your text:\n")

words = []
char = 0

for x in text:
    if x == ' ':
        continue
    char += 1

words = text.split()
unique = set(words)

print("Words: ", len(words))
print("Characters: ", char)
print("Unique Words: ", len(unique))
