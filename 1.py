class MyClass():
    def __init__(self):
        self.str = ""

    def getstr(self):
        self.str = input()

    def reversestr(self):
        print(self.str[::-1])

str = MyClass()
getstr()
