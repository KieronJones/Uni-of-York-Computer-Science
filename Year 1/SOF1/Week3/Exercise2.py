# Program 1
num =  int(input("Please enter a positive integer: "))
sum = 0

for i in range(num+1):
    sum += i

print(sum)


#Program 2
num2 = int(input("Please enter a positive integer: "))

for i in range(13):
    print(str(num2) + " x " + str(i) + " = " + (str(num2 * i)))


#Program 3
num3 = int(input("Please enter a positive integer: "))
factorial = 1

for i in range(1, num3 + 1):
    factorial *= i

print(factorial)