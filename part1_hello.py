class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

me = Greeter("Rhodney Josh Olivar")
me.greet()
