# functions
from os import write

with open("data.txt", "w") as file:
    # file.write("99\n")
    # file.write("34\n")
    for temp in range(10): file.write(str(temp)+ "\n")



with open("data.txt", "r") as file:
        content = file.read()
        print(content)

#install
# use

