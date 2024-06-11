# Task 1

mode = int(input("Enter mode number (0 = up, 1 = down, 2 = down with right): "))
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
if mode == 0:
    print("*" * start)
    for i in range(start + 1, end + 1):
        print("*" * i)
elif mode == 1:
    print("*" * end)
    for i in range(end - 1, start - 1, -1):
        print("*" * i)
elif mode == 2:
    print("*" * end)
    for i in range(end - 1, start - 1, -1):
        print((" " * (end - i)) + ("*" * i))

# Task 2

list_mountains = [2580, 4860, 7860, 7160, 6900]
print(max(list_mountains))

# Task 3
name_mountains = ['Аконкагуа', 'Эльбрус', 'Монблан', 'Казбек', 'Нордент', 'Народная', 'Макалу', 'Чогори', 'Джомолунгма']

list_mountains = [6962, 5642, 4810, 5033, 4609, 1895, 8463, 8611, 8848]
print(name_mountains[list_mountains.index(max(list_mountains))])

# Task 4
field = [
    ["X", "0", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]
for i in field:
    f =""
    for n in i:
        f+=n + " "
    print(f)