import math

def area_triangle():
    base = int(input("Give base of the triangle: ")) 
    height = int(input("Give height of the triangle: "))
    return 0.5*height*base

def area_rectangle():
    width = int(input("Give width of the rectangle: "))
    height = int(input("Give height of the rectangle: "))
    return width*height 

def area_circle():
    radius = int(input("Give radius of the circle: "))
    return math.pi*(radius**2)


def main():
    shapes = {"triangle": area_triangle, "rectangle": area_rectangle, "circle": area_circle}
    while True:
        usrin = input("Choose a shape (triangle, rectangle, circle): ")
        if usrin in shapes.keys():
            print(f"The area is {shapes[usrin]()}") 
        elif usrin == "":
            break 
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
