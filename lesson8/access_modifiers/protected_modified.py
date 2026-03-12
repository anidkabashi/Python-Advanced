class MyClass:
    def __init__(self):
        self._protected_variable = "This is a protected varaible"

    def _protected_method(self):
        print("this is a protected method")

my_class = MyClass()

print(my_class._protected_variable)

my_class._protected_method()