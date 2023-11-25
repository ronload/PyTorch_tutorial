# Test ``__call__()`` method

class Person:

    @staticmethod
    def __call__(name):
        print(f"__call__: Hello, {name}")

    @staticmethod
    def hello(name):
        print(f"Hello, {name}")

person = Person()  # System execute `Person.__init__(self)`
person("Python")  # System execute `person.__call__("Python")
person.hello("Pytorch")  # System execute `person.hello("Python")