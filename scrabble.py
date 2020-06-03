# Create a scrabble.py point calculator

def scrabble_calc():
    string = input("Enter the word for Scrabble points ")
    points = 0

    for letter in string.lower():
        if letter in 'aeioulnstr':
            points += 1
        elif letter in 'dg':
            points += 2
        elif letter in 'bcmp':
            points += 3
        elif letter in 'fhvwy':
            points += 4
        elif letter == 'k':
            points += 5
        elif letter in 'jx':
            points += 8
        elif letter in 'qz':
            points += 10

    return points


print(scrabble_calc())