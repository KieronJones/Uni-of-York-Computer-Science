# Exercise 1

num_stones = int(input("Please enter a number."))
num_pounds = int(input("Please enter a number of pounds."))

num_kilos = (num_stones * 6.35029318) + (num_pounds * 0.45359237)

print(str(num_stones) + " stone and " + str(num_pounds) + " pounds in kilos is " + str(num_kilos) + " kg.")


num_kilos = int(input("Please enter a number of kilos."))
