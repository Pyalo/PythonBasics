# Functions
from numbers import result


def greet():
    print("Hello, welcome to Python!")

def greeting(user):
    print(f"Hello {user}, welcome to Python")

def area_circle(radius, precision=3):
    a = 22/7 * radius * radius
    result = round(a, precision)
    print(result)

def volume_cylinder(radius, height):
    v= 22/7 * radius**2 * height
    return v

print(volume_cylinder(373, 4.5))
res = volume_cylinder(3.5, 4.5)
print(round(res))



#named params
# area_circle(precision=3, radius=5)



area_circle(2.3, 3)
area_circle(6.3, 0)
area_circle(5)

# to use a function you must call
# greet()
# greet()
# greet()

#params/ args
# greeting("Jimi")
# greeting("Mohana")


