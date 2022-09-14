message = input(">")
words = message.split(" ")
print(words)

emojis = {
    ":)": "and I sense you are happy.",
    ":(": "and I sense you are sad."
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
    print(output)
