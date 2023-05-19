def smile_converter(comment):
    words = comment.split(" ")
    emojis = {
        ":)": "and I sense you are happy.",
        ":(": "and I sense you are sad."
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(smile_converter(message))
