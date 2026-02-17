class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname






class Student(Person):
 def __init__(self, fname, lname,year):
      super().__init__(fname,lname) #super() makes the child's class inherit all the methods and properties from its parent
      self.graduationyear = year

