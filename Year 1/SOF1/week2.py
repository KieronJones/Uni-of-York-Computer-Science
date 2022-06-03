# Exercise 1 & 2
def stones_and_pounds_to_kilos(stones, pounds):
    num_kilos = (stones * 6.35029318) + (pounds * 0.45359237)
    message = (str(stones) + " stone and " + str(pounds) + " pounds in kilos is " + str(num_kilos) + " kg.")
    return message


def kilos_to_stones_and_pounds(kilos):
    stones = kilos // 6.35029318
    pounds = (((kilos / 6.35029318) % 1) * 14)
    message = (str(kilos) + " kilos in stones and pounds is " + str(stones) + " and " + str(pounds) + " pounds.")
    return message


#Exercise 3
def bananas_to_cost(kilos):
    order = (kilos*3) + 4.99
    if order > 50:
        order -= 1.50
    return order


#Exercise 4
def training_zone(age, rate):
    m = 208 - (0.7 * age)
    if (rate >= (0.9*m)):
        print("Interval Training")
    elif ((0.7 * m) <= rate < (0.9 * m)):
        print("Threshold Training")
    elif ((0.5 * m) <= rate < (0.7 * m)):
        print("Aerobic Training")
    else:
        print("Couch Potato")


#Exercise 5
def length_to_area(a, b, c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
