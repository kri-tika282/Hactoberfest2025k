def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

print("Choose the shape to calculate the area:")
print("1. Square")
print("2. Rectangle")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    side = float(input("Enter the side of the square: "))
    print(f"The area of the square is: {area_square(side)}")
elif choice == '2':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"The area of the rectangle is: {area_rectangle(length, width)}")
else:
    print("Invalid choice. Please choose 1 or 2.")
