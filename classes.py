print("Millicent WAANIKU");
class Employee:
    """This is an example of an employee class"""

    # class variable whose value is shared among all instances of a this class
    empCount = 0

    #class constructor or initialization method that
    # Python calls when you create a new instance of this class.
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

    def displayCount(self):
     print("Total Employee %d" % Employee.empCount);

    def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary);


"""This would create first object of Employee class"""
emp1 = Employee("Zara", 2000)
print(emp1.displayCount());
"""This would create second object of Employee class"""
emp2 = Employee("Manni", 5000)

print("my employess count:", Employee.empCount);
