from cs50 import get_int

while True:
    height = get_int("Height: ")
    if (1 <= height <= 8):
        break

# prints newline
for j in range(height):

    # prints spaces
    for spaces in range(height-j-1):
        print(" ", end="")

    # prints hashes
    for i in range(j+1):
        print("#", end="")

    print()
