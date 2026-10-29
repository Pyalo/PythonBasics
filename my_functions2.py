def add(a, b, c):
    return a+b+c


def addition(w, *nums):
    # total = sum(nums)
    total = 0
    for num in nums:
        total += num
    return total

def save(**data):
    with open("values.txt", "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")


def some_function(name, *score, **details):
    pass

def cylinder(r, h):
    """
    calculates the volume and surface area of a cylinder
    parameters:
    radius and height of the cylinder
    returns: volume and surface area
    """
    v = 22/7 * r * h
    sa = 22/7 * r **2 *2 + 22/7 *r * 3 *h
    return sa, v

surf_area, volume = cylinder(20,12)

print(surf_area, volume)

sum({2,3,4})


#lambda functions
#they are anonymus functions
# def divide(a, b):
#     return a/b

divider = lambda x, y : x/y

area_circle = lambda radius: 22/7 * radius * radius

print(divider(10, 3))


# some_function(name="Mugo", score=50, details={})
# save(dob='20000-02-18', gender='male', race='African', name='Pyalo', club='Chelsea Fc')

# print(addition(28,37,5859,484,47487,6320,7584,3537,344,))
# print(addition(620,484))



# result = add(1,2,3) # 3 args/params
# print(result)

# data = {"name":"Ken", "gender":"male"}
# for key, value in data.items():
#     print(f"{key}: {value}")