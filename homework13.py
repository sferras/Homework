import random
seed = random.randint(1, 10)
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = input("What is the text to encode?")
text = text.lower()
encoded = ""
for c in text:
    pos = alphabet.find(c)
    if pos == -1:
        encoded = encoded + c
        continue
    new_pos = (pos + seed) % 26
    encoded = encoded + alphabet[new_pos]
print("The encoded text is:", encoded)
print("The decoded text is: ", text)