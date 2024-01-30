from art import tprint


class Hello:
    def __init__(self, string):
        self.string = string


class Bek(Hello):
    def art(self):
        tprint('Hello World ' + self.string)


b = Bek("Python")
