class one():
    def __init__(self):
        self.__a=1
    def method_one(self):
        print("method one from class one")
class two():
    def __init__(self):
        self.__b=1
    def method_one(self):
        print("method one from class two")
c= two()
c.method_one()

"""
Output:
method one from class two


"""