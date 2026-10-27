score = int(input("Enter score: "))

# we are using if statement and it only executes when the a statement is true

if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("A-")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("B-")
elif 50 <= score <= 59:
    print("C")
elif 40 <= score <= 49:
    print("C-")
elif score >= 30 and score <= 39:
    print("D")
elif score >= 20 and score <= 29:
    print("D-")
else:
    print("E")

# if score >= 90:
#     print("AMAZING")
# else:
#     print("AMAZING")