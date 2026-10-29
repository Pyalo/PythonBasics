#oop2
class Circle:
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return 22/7 * self.radius * self.radius

    def get_perimeter(self):
        return 22/7 * (self.radius * 2)

    def print_details(self):
        print("Radius:", self.radius)
        print("Perimeter:", self.get_perimeter())
        print("Area:", self.get_area())

c1 = Circle(13)
c2 = Circle(48.11)

c1.print_details()
print(c1.get_area())


# Copy branch
# push
# raise Pull Request
# accept the code then merge
# deploy to server automatic
