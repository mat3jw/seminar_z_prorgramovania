def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def main():
    r = int(input("Enter the radius: "))
    area_of_circle = calculate_area(r)
    print(f"The area of the circle is: ",area_of_circle)

    return main