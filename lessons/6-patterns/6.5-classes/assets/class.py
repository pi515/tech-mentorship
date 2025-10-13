from abc import ABC, abstractmethod


class Plant(ABC):
  """This is an abstract class for all plant based classes.
  """
  name = "plant"  # class variable

  def __init__(self):
    self.height = 0  # instance variable

  @abstractmethod
  def grow(self):
    # abstractmethod force us to define a subclass to specify the concrete method
    pass

  # class methods allow accessing class variables
  @classmethod
  def rename(cls, new_name):
    cls.name = new_name
    #cls.height = 0 # this is not the same as instance height; we essentially created a new variable

  @staticmethod
  def add(a, b):
    #name = "abc"  # different variables from cls.name or self.height
    #height = 0
    return a + b

  def __repr__(self):
    return f"Name: {self.name}, Height: {self.height}"


class Grass(Plant):
  name = "grass"

  def grow(self):
    self.height += 2


class Corn(Plant):
  name = "corn"

  def grow(self):
    self.height += 1


if __name__ == "__main__":
  p1 = Grass()
  p2 = Grass()
  p3 = Corn()
  p4 = Corn()

  p2.grow()
  p3.grow()

  print(p1)
  print(p2)
  print(p3)
  print(p4)

  # class method
  p3.rename("hybrid")
  print(p3)
  print(p4)

  # alternative way to call a class method
  Corn.rename("corn")
  print(p3)

  # static method
  print(p1.add(3, 4))
  print(p1)  # name and height are not changed
