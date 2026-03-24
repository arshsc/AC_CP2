# inheritance (is a)
# parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vroom!")

# child classes
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()



# aggregate classes (has a)
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    
    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("That book isn't in the catalog.")
    
    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib = Library("Provo Library")
lib.add_book(Book("The Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("The Fellowship of the Ring", "J.R.R. Tolkien"))
lib.add_book(Book("The Last Battle", "C.S. Lewis"))
lib.add_book(Book("The Great Hunt", "Robert Jordan"))

lib.view_catalog()



# composition
class Engine:
    def __init__(self, cylinders):
        self.cylinders = cylinders

    def __str__(self):
        return self.cylinders

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.engine = Engine("V8")

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()
print(car.engine)