#Exercise 1 - Part 1
def even_nums(str_nums):
    num_evens = 0
    nums_split = str_nums.split()
    for num in nums_split:
        int_num = int(num)
        if (int_num%2) == 0:
            num_evens += 1
    return "There are " + str(num_evens) + " even numbers."


#Exercise 1 - Part 2
def even_nums_listed(str_nums):
    num_list = ""
    num_evens = 0
    nums_split = str_nums.split()
    for num in nums_split:
        int_num = int(num)
        if (int_num%2) == 0:
            num_evens += 1
            num_list += num
            num_list += " "
    return "There are " + str(num_evens) + " even numbers: " + num_list


#Exercise 1 - Part 3
def distinct_even_nums(str_nums):
    num_list = ""
    distinct_evens = 0
    nums_split = str_nums.split()
    for num in nums_split:
        int_num = int(num)
        if (((int_num%2) == 0) and (num not in num_list)):
            distinct_evens += 1
            num_list += num
            num_list += " "
    return "There are " + str(distinct_evens) + " distinct even numbers: " + num_list


#Exercise 2 - Part 1
numbers = str(input("Please enter four numbers seperated by whiteapce: "))
num_list = []
for num in numbers:
    if num != (" "):
        num_list.append(int(num))
print(num_list)


#Exercise 2 - Part 2
board = []
for i in range(4):
    nums_list = []
    nums = str(input("Please enter four numbers seperated by whitespace: "))
    for num in nums:
        if num != (" "):
            nums_list.append(int(num))
    board.append(nums_list)


#Exercise 2 - Part 3 and 4
hline = '+-+-+-+-+\n'
output = hline
for row in board:
    for element in row:
        if element == 0:
            output += '| '
        else:
            output += '|'+str(element)
    output += '|\n'
    output += hline
print(output)


#Exercise 3
number = int(input('Enter a positive natural number: '))
binary = ''
while number > 1:
    binary = str(number % 2) + binary
    number = number // 2
binary = str(number) + binary
print(binary)

