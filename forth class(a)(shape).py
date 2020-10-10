# letter i shape
for row in range(8):
    for column in range(5):
        if (row == 0) or (row == 7) or (column == 2):
            print("#", end="")
        else:
            print(end=" ")
    print()

# letter c shape
for row in range(7):
    for column in range(7):
        if (row == 0 and column > 2) or (row == 1 and column == 2) or (column == 1 and 1 < row < 5) \
                or (row == 5 and column == 2) or (row == 6 and column > 2):
            print("#", end="")
        else:
            print(end=" ")
    print()

# letter z shape
print()
for row in range(8):
    for column in range(8):
        if (row == 0) or (row == 1 and column == 6) or (row == 2 and column == 5) or (row == 3 and column == 4) \
                or (row == 4 and column == 3) or (row == 5 and column == 2) or (row == 6 and column == 1) or (row == 7):
            print("#", end="")
        else:
            print(end=" ")
    print()

# letter H shape with a acorn
print()
for row in range(15):
    for column in range(15):
        if (column == 2) or (column == 12) or (column == 0 and 1 < row < 13) or (
                column == 1 and 0 < row < 14) \
                or (column == 3 and 0 < row < 14) or (column == 4 and 1 < row < 13) or (
                column == 10 and 1 < row < 13) \
                or (column == 11 and 0 < row < 14) or (column == 13 and 0 < row < 14) or (
                column == 14 and 1 < row < 13) \
                or (row == 5) or (row == 6) or (row == 7):
            print("H", end="")
        else:
            print(end=" ")
    print()

# without simplification of the code
# print()
# for row in range(15):
#     for column in range(15):
#         if (column == 2) or (column == 12) or (column == 0 and row > 1 and row < 13) or (column == 1 and row > 0 and row < 14)\
#                 or (column == 3 and row > 0 and row < 14) or (column == 4 and row > 1 and row < 13) or (column == 10 and row > 1 and row < 13)\
#                 or (column == 11 and row > 0 and row < 14) or (column == 13 and row > 0 and row < 14) or (column == 14 and row > 1 and row < 13)\
#                 or (row == 5) or (row == 6) or (row == 7):
#             print("H", end="")
#         else:
#             print(end=" ")
#     print()
