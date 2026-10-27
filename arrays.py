# store lot data


# data structures allows to store data
# list, set, tuple, dictionary

people = ["Jane", "Kim", "Maria", "Pyalo", "Ramien"]
scores = [47, 23, 74, 50, 90, 100]

# print(people[3])
# print(scores[0])
#
# print(scores[-1]) #prints the last value
#
# people.append("Jane")
# print(people)
#
# scores.append(90)
# print(scores)

# people.sort()
# scores.sort(reverse=True)
# print(people)
# print(scores)
#
# print(scores[0], scores[-1])
# print(sum(scores)/ len(scores))

scores.sort()
#slicing
# print(scores)
# print(scores[-2:])
# print(scores[:3])

# set -- removes duplicates
numbers = {87, 37,94, 77, 87, 46, 77, 18}
print(numbers)

# Tuple -- immutable data

days = ("Mon", "Tue", "Fri")

# dictionary, contain key and value
person = {"name": "Zillow", "city": "Marsabit", "age": 14}
print(person["name"])

# data structures + algorithms
print(sum(numbers))

watu = [{"name": "Sila", "age": 22},
        {"name": "Jalas", "age": 33},
        {"name": "Omolo", "age": 88}]
print(watu)
print(watu[0]["name"])

#loops