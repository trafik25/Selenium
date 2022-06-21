class Person:
  def __init__(obj1, name, age):
    obj1.name = name
    obj1.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()