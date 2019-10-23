#Python 3.6.2, Windows 10
#Fia Berggren Lindqvist
#Labbpartner: Kristina Ckalla

import geometri

def main():
    print("GeoTest: \n")
    p1 = geometri.Punkt(3, 4)
    p2 = geometri.Punkt(5, 2)
    print(str(p1))
    print(p2)
    print(p1 == p2)

    #Test the Circle-class
    c1 = geometri.Cirkel(7, 3, 4)
    c2 = geometri.Cirkel(11, 5, 2)
    c3 = geometri.Cirkel(7, 3, 4)
    print("The area of the circle =", c1.get_area())
    print("The circumference of the circle =", c1.get_circumference())
    print(c1 == c2)
    print(c1)
    print(c3)
    print(c1 == c3, "\n")

    #Test the Rectangle-class

    #defines the variables r1, r2 och r3
    r1 = geometri.Rektangel(3, 4)
    r2 = geometri.Rektangel(5, 2)
    r3 = geometri.Rektangel(3, 4)
    #prints the value of get_area och get_circumference
    print("The area of the rectangle = ",r1.get_area())
    print("The circumference of the rectangle = ", r1.get_circumference())
    #prints the value of __eq__ och __str__
    print(r1 == r2)
    print(r1)
    print(r3)
    print(r1 == r3, "\n")
    
    #Test the Triangle-class

    #defines the variables t1, t2 och t3
    t1 = geometri.Triangel(7, 3, 4)
    t2 = geometri.Triangel(11, 5, 2)
    t3 = geometri.Triangel(7, 3, 4)
    #prints the value of get_area och get_circumference
    print("The area of the triangle = ", t1.get_area())
    print("The circumference of the triangle = ", t1.get_circumference())
    #prints the value of __eq__ och __str__
    print(t1 == t2)
    print(t1)
    print(t3)
    print(t1 == t3, "\n")

if __name__ == "__main__":
    main()
