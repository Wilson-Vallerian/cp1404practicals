from operator import itemgetter
name_to_count = {}
text = input("Text: ")
words = text.strip().split(" ")
print(words)

for word in words:
    if word in name_to_count:
        name_to_count[word] += 1
    else:
        name_to_count[word] = 1

max_length = max([len(name) for name in list(name_to_count.keys())])

words = list(name_to_count.items())
words.sort(key=itemgetter(0), reverse=False)
for word in words:
    print(f"{word[0]:{max_length}} : {word[1]}")
