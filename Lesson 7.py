# Task 34

words = input()
vowel = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
parts = words.split()
temp = list()
for item in parts:
    x = 0
    for letter in item:
        if letter in vowel:
            x += 1
    temp.append((x))
if len(set(temp)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")

# Task 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for x in range(1, num_rows + 1):
#         nums = []
#         for y in range(1, num_columns + 1):
#             num = operation(x, y)
#             nums.append(num)
#         print('\t'.join([str(x) for x in nums]))
# print_operation_table(lambda x, y: x * y)