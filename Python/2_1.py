"""
class Employee:    
    Employee_Count = 0
    def __init__(self, name, salary):
        Employee.Employee_Count += 1
        
        self.name = name
        self.salary = salary
        self.number = (Employee.Employee_Count)
    
    def Employee_Number(self):
        print("Employee Number: " + str(self.number))
        print("")

    def Display_Info(self):
        print("Name: " + self.name)
        print("Employee Number: " + str(self.number))
        print("Salary: $" + str(self.salary))
        print("")
    

Person_1 = Employee("Reed", 1000)
Person_2 = Employee("Jimmy", 10000000000)

Person_1.Display_Info()
Person_2.Display_Info()


print(Person_1.name)
print(Person_1.salary)
print(Person_1.number)


class Employee:    
    Employee_Count = 0
    def __init__(self, name, salary):
        Employee.Employee_Count += 1
        
        self.name = name
        self.salary = salary
        self.number = (Employee.Employee_Count)

Person_1 = Employee("Reed", 1000)
Person_2 = Employee("Jimmy", 10000000000)

print(Person_1.name)
print(Person_1.salary)
print(Person_1.number)
"""












"""

class People:    
    Student_ID = 0
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        People.Student_ID += 1
        self.Student_ID = (People.Student_ID)

    

Person_1 = People("Reed", 50)

print(Person_1.name)
print(Person_1.grade)
print(Person_1.Student_ID)


Person_2 = People("Jimmy", 100)

print("")

print(Person_2.name)
print(Person_2.grade)
print(Person_2.Student_ID)




"""









class People:    
    Student_ID = 0
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        People.Student_ID += 1
        self.Student_ID = (People.Student_ID)
    
    def info(self):
        print(self.name)
        print(self.grade)
        print(self.Student_ID)

    

Person_1 = People("Reed", 50)
Person_2 = People("Jimmy", 100)


Person_1.info()
Person_2.info()








"""
Person_3 = People("Stanley", 95)
print("")

print(Person_3.name)
print(Person_3.grade)
print(Person_3.Student_ID)







"""





"""
def joe_mama(times):
    for num in range(times):
        print("joe_mama")

#joe_mama(5)
joe_mama(int(input("How many times?: ")))
"""

























def divide(a, b):
    return (str(a/b))

#print(divide(10, 5))









"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”

Python Knowledge Needed:
For loops
If/elif/else statements
Print

"""




def fizz_buzz(num):
    for i in range(1, num+1):
        if (i%3) == 0 and (i%5) == 0:
            print("FizzBuzz")
        elif ((i%5) == 0):
            print("Buzz")
        elif ((i%3) == 0):
            print("Fizz")
        else:
            print(i)

#fizz_buzz(100)

#query













def fizz_buzz():
    for i in range(0, 101):
        if (i%3) == 0:
            print("Fizz")
        elif (i%5) == 0:
            print("Buzz")
        elif (i%15) == 0:
            print("Fizz Buzz")
        else:
            print(i)

#fizz_buzz()




# pip install yfinance
"""

import yfinance as yf

# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Set the ticker
ticker = 'AMZN'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
print(data.tail())
"""











"""



# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot adjusted close price data
data['Adj Close'].plot()
plt.show()



"""