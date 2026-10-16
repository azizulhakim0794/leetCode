myvar: float = 2 + 3j

print(type(myvar))
print(myvar)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "#" * (1 * i - 1))


class Pyramid:
    def draw(self, n):
        for i in range(1, n + 1):
            print(" " * (n - i) + "#" * (1 * i - 1))


pyramid = Pyramid()
pyramid.draw(5)


class Pyramid:
    def __init__(self, height):
        self.height = height

    def draw(self):
        for i in range(1, self.height + 1):
            spaces = " " * (self.height - i)
            hashes = "#" * (2 * i - 1)
            print(spaces + hashes)


pyramid = Pyramid(5)
pyramid.draw()
