#Exercise 1: The King and the Wise man
rice = 1
weight = 0.03

for i in range(64):
    rice = rice * 2
    square_weight = weight * rice
    print("This square has " + str(rice) + " pieces of rice on it and weighs " + str(square_weight) + " grams.\n")


#Exercise 2 and 3
sample_text = (" As Python s creator I d like to say a few words about its "+
              "origins adding a bit of personal philosophy "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas My office "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus")

def get_words_starting_with(text, letter):
    word_list = text.split()
    output = []

    for word in word_list:
        word_ = word.lower()
        if (word_[0] == letter) and (word not in output):
            output.append(word)
    
    return output

print(get_words_starting_with(sample_text, 'a'))


#Exercise 4


#Exercise 5
def scalar_product(scalar, vector):
    for i in range(len(vector)):
        vector[i] = vector[i] * scalar
    return vector


def vector_addition(vector1, vector2):
    new_vector = vector1
    for i in range(len(vector1)):
        new_vector[i] = vector1[i] + vector2[i]
    return new_vector