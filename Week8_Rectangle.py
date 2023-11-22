#Dwayne Winn CIS261 Rectangle

from dataclasses import dataclass
    
@dataclass
class Rectangle():#setup object class
    height: int
    width: int


    #Caculate perimeter
    def getPerimeter(self):
        perimeter = self.height * 2 + self.width * 2
        return perimeter


    #Caulate area
    def getArea(self):
        area = self.height * self.width
        return area


    #setup rectangle for display
    def getStr(self):
        s = ""
        w = "* " * self.width + "\n"          
        s += w
        for i in range(self.height - 2):
            s += "* "
            s += "  " * (self.width - 2)
            s += "* \n"
        s += w
        return s


# start of main function
def main():
  
    print("Rectangle Calculator")
    print()
    cont = 'y'
    #loop of display rectangle
    while cont.lower() == "y":
          #get rectangle user input  
          height = int(input("The height of rectangle: "))
          width = int(input("The width of rectangle: "))
          if width == height:
              print("Sorry thats a sorry thats a square please try again")#just had to!
              main()
          rectangle = Rectangle(height,width)
          print("Perimeter:", rectangle.getPerimeter())
          print("Area: ", rectangle.getArea())
          print(rectangle.getStr())
          cont = input("Continue? (y/n): ")
          print()
          
    print("Thank you")
    
if __name__ == "__main__":
   main()
