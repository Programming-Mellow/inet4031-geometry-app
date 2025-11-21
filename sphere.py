# inspiration code for Python Unit Testing Project
import math

def surfaceArea(rad):
    return 4.0 * math.pi * (rad ** 2)

def volume(rad):
    return (4.0 / 3.0) * math.pi * (rad ** 3)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    print("\nThe Surface Area of the Sphere = ", surfaceArea(radius))
    print("The Volume of the Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()
