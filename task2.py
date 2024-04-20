#Task 1

print("The number of books on the media: %s" % (int(float(input("Enter the storage capacity (in MB): ")) * 1048576) // (int(input("Number of bytes per character: ")) * int(input("Enter the number of characters per line: ")) * int(input("Enter the number of lines per page: ")) * int(input("Enter the number of pages in the book: ")))))

#Task 2

print() #I use this to make space between tasks😜
match input("Enter calc mode(circle, square): "):
    case "circle":
        radius = float(input("Enter the radius(may in float)😁: "))
        print("Area: %s " % float(3.1415 * radius ** 2.0))
        print("Length: %s" % float(2.0 * 3.1415 * radius))
    case "square":
        side = float(input("Enter the radius(may in float)😉: "))
        print("Perimeter: %s " % float(4 * side))
        print("Area: %s" % float(side ** 2))

# Task 3

print()
print('0' * 20 + '1' * 50 + '2' * 30)

#Task 4

print()
paid_data = (500 - (float(input('Enter the speed in kb/s: ')) * float(input("Enter the download time: ")))) * float(input("Introduction the cost of one kilobyte: "))
print("You need to pay: %s" % paid_data if paid_data < 0 else "No payment is required")

#Task 5 (boring 😩)

lenght = float(input("Enter lenght: "))
width = float(input("Enter wigth: "))
perimetr = lenght * width

#Task 6

