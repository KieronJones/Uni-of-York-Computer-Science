#Exercise 1
def sum_digits(number):
    number = str(number)
    sum = 0
    for num in number:
        num_int = int(num)
        sum += num_int
    return sum


#Exercise 2
def pairwise_digits(number_a, number_b):
    output = ""
    str_a = str(number_a)
    str_b = str(number_b)
    search_string = ""

    if len(str_a) > len(str_b):
        search_string = str_b
    else:
        search_string = str_a

    for i in range(len(search_string)):
        if str_a[i] == str_b[i]:
            output += "1"
        else:
            output += "0"
    
    num_zeros = abs(len(str_a) - len(str_b))

    for i in range(num_zeros):
        output += "0"

    return output


#Exercise 3
def to_base10(binary):
    return int(str(binary), 2)


#Exercise 4
def right_angled_triangle(rows):
    add_1 = True
    output = ""
    for row in range(rows):
        if row%2 == 0:
            add_1 = True
        else:
            add_1 = False

        for index in range(row+1):
            if add_1:
                output += "1"
            else:
                output += "0"
            add_1 = not add_1
        
        output += '\n'

    return output


#Exercise 5
def sum_lists(list_2D):
    output =[]
    for row in list_2D:
        total = 0
        for val in row:
            total += val

        output.append(total)
    print(output)