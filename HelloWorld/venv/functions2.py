def square(number):
    return number * number  # Return em python

print(square(3))

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

msg = input(">")
result = emoji_converter(msg)
print(result)