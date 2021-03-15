#can't run in vscode to keep code simple

banned = "qwyskzxvm" #this will vary depending on what you decide is not able to be displayed

f = open("words.txt", "r")
words = f.read()
words = words.split("\n")

longest_word = ""

for word in words:
    for letter in word:
        if letter in banned:
            break
    else: #only runs if 'for letter in word' doesn't break
        if len(word) > len(longest_word):
            longest_word = word

print(longest_word)
