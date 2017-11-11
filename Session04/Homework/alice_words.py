path = 'E:/Python Document/alice_words.txt'
words_file = open(path,'r')
ignored_letter =  open('E:/Python Document/ignored_letters.txt','r')
import string
counts = {}
for line in words_file:
    words = line.split(" ")
    print(words)
    for word in words:
        for i in word:
            if i in list(ignored_letter):
                word = word.replace(i," ")
            word = word.lower()
            if word.isalpha():
                if word in counts:
                    counts[word] = counts[word] + 1
                else:
                    counts[word] = 1
keys = counts.keys()

out = open('alice_words.txt', 'w')
out.write("Word \t \t \t \t \t Count")
out.write("====================================")
for word in sorted(keys):
    out.write(word + "\t \t \t \t \t" + str(counts[word]))
    out.write('\n')
print("The world 'alice' appears ", str(counts['alice']), "times in the book.")

l = list(counts.keys())
longest = len(l[0])
for i in range(len(l)):
    if longest < len(l[i]):
        longest = len(l[i])
        posi = i
print("The longest word is", l[posi], "has", longest, "characters.")
