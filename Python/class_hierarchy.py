# definition of superclass "Triangles"
class Triangles(object):
      
    count = 0
      
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        Triangles.count+= 1
  
    def setName(self, name):
        self.name = name
  
    def setdim(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
  
    def getcount(self):
        return Triangles.count
  
    # superclass's version of display()
    def display(self):
        return 'Name: '+self.name+'\nDimensions: '+str(self.s1)+', '+str(self.s2)+', '+str(self.s3)
  
# definition of the subclass
# inherits from "Triangles"
class Peri(Triangles):
          
    def calculate(self):
        self.pm = 0
        self.pm = self.s1 + self.s2 + self.s3
         
    # extended method 
    def display(self):
          
        # calls display() of superclass 
        print (super(Peri, self).display())
          
        # adding its own properties 
        return self.pm
          
      
def main():
      
    # instance of the subclass
    p = Peri('PQR', 2, 3, 4)
      
    # call to calculate
    p.calculate()
      
    # one call is enough 
    print(p.display())
      
main()