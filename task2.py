# Task 1

print("The number of books on the media: %s" % (int(float(input("Enter the storage capacity (in MB): ")) * 1048576) // (int(input("Number of bytes per character: ")) * int(input("Enter the number of characters per line: ")) * int(input("Enter the number of lines per page: ")) * int(input("Enter the number of pages in the book: ")))))

# Task 2

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

# Task 4

print()
paid_data = (500 - (float(input('Enter the speed in kb/s: ')) * float(input("Enter the download time: ")))) * float(input("Introduction the cost of one kilobyte: "))
print("You need to pay: %s" % paid_data if paid_data < 0 else "No payment is required")

# Task 5 (boring 😩)

print()
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimetr = length * width
print(perimetr)

# Task 6

print()
money = int(input("Enter the amount of money in the account: "))
add = int(input("Enter the number of percentages: ")) / 100
result = money * add
print("Percentages: %s") % result
print("After interest payment: %s") % money - result

# Task 7

print()
all_hour = int(input("Enter the number of hours: "))
days = all_hour // 24
hours = all_hour - (days * 24)
print("Days: %s") % days
print("Hours: %s") % hours

# Task 8

print()
list_players = ['Adam', 'Lucifer', 'God']
last_player = list_players[len(list_players)]
reestr = {'First': 'Adam', 'Second': 'Lucifer', 'Third': 'God'}
print("Last player: %s") % last_player
print("First player: %s") % reestr['First']

# Task 9

print()
fruits = ["яблоко", "банан", "опельсин", "виноград"]
incorrect_word = fruits[2]
correct_word = "а" + incorrect_word[1:]
fruits[2] = correct_word
print(fruits)