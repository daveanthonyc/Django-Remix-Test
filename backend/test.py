class Test:
    def __init__(self, thing):
        self.thing = thing

    def __str__(self):
        return self.thing

class David:
    def __init__(self, name):
        self.name = name

test = Test('hmm')
david = David('David')

print(test)
print(david)
