name = "Pyalo"

sentence = "My home is \"Chepsir\""     #escape character

print(sentence)


# operations -> functions

print(name.upper())
print(name.lower())

sentence = sentence.upper()

print(sentence)
print(sentence.capitalize())
print(sentence.title())

print(name.count("a"))   #call a function ---using, parameter

print(len(name))

replaced_sentence = sentence.lower().replace("chepsir", "kiserian")

print(replaced_sentence)

k = "34343"
sentence.isnumeric()


print(name.isnumeric())
print(sentence.isupper())
# print(sentence.isalnum())