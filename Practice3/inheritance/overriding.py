class Person: #Parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



class Student(Person):#Child of Person class
    def __init__(self, fname, lname):
       self.fname= fname
       self.lname =lname #overriding parents init func