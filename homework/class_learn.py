class Animal:
    def poser(self):
        print("Я тебе щас въебу нахуй")

class Dog(Animal):
    def fight(self):
        print("Делаю вертушку и по ебалу")

d = Dog()

print(d.fight())
print(d.poser())

class Counter:
  def __init__(self, value):
    self.value = value

  def add_value(self, value):
    self.value += value


class SecondCounter(Counter):
  def add_value(self, value):
    self.value += 2*value

sc = SecondCounter(5)
sc.add_value(10)
print(sc.value)

