
#---------------------------------------------------------------
# Customizing Object Representation
# str and repr methods
# These methods allow you to define how your objects are represented as strings:
#---------------------------------------------------------------
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"


book = Book("1984", "George Orwell", 328)
print(str(book))  # Output: 1984 by George Orwell
print(repr(book))  # Output: Book('1984', 'George Orwell', 328)

# ---------------------------------------------------------------
# Implementing Custom Container Behavior
# len and getitem methods
# These methods allow your objects to behave like containers:
# ---------------------------------------------------------------
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]


playlist = Playlist("My Favorites", ["Song1", "Song2", "Song3"])
print(len(playlist))  # Output: 3
print(playlist[1])  # Output: Song2

#---------------------------------------------------------------
# Operator Overloading
# add and mul methods
# These methods allow you to define custom behavior for operators:
#---------------------------------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: Vector(4, 6)
print(v1 * 3)  # Output: Vector(3, 6)

#---------------------------------------------------------------
# Customizing Attribute Access
# getattr and setattr methods
# These methods allow you to control attribute access and assignment:
#---------------------------------------------------------------
class SafeDict:
    def __init__(self):
        self._data = {}

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        if name == '_data':
            super().__setattr__(name, value)
        else:
            self._data[name] = value


safe_dict = SafeDict()
safe_dict.key = "value"
print(safe_dict.key)  # Output: value
print(safe_dict.nonexistent)  # Output: None

#---------------------------------------------------------------
# Making Objects Callable
# call method
# This method allows you to make instances of your class callable:
#---------------------------------------------------------------
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15