# Program 1
num = int(input("Please enter a number: "))
nums = []
nums.append(num)

while (num > 0):
    num = int(input("Please enter a number: "))
    nums.append(num)

print(sum(nums))


# Program 2
num2 = int(input("Please enter a number: "))
nums2 = []
nums2.append(num2)

while (num2 > 0):
    num2 = int(input("Please enter a number: "))
    nums2.append(num)

print((sum(nums2)/len(nums2)))


# Program 3
num3 = int(input("Please enter a number: "))
nums3 = []
nums3.append(num3)
even_nums = []

while (num3 > 0):
    num3 = int(input("Please enter a number: "))
    nums3.append(num3)

for number in nums3:
    if (number%2) == 0:
        even_nums.append(number)

print(len(even_nums))