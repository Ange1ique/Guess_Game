animals = {
    1: 'Heeft het dier 4 poten? ',
    2: 'olifant',
    3: {
        1: 'Kruipt het op bladeren? ',
        2: 'rups',
        3: 'huismus'
    }
}


# Function to start the game
def game():
    print("Bot raadt een dier")
    print("Neem een dier in gedachten...")

    find_next_question(animals)


# Function to find the next question in the dictionary until there are no questions left and then guess for the animal
def find_next_question(d):
    answer = input(d.get(1))
    if number(answer) == 2 and isinstance(d.get(2), dict):
        find_next_question(d.get(2))
    elif number(answer) == 2:
        answer = input("Is het dier een " + d.get(2) + "? ")
        ending(answer, d)
    elif number(answer) == 3 and isinstance(d.get(3), dict):
        find_next_question(d.get(3))
    else:
        answer = input("Is het dier een " + d.get(3) + "? ")
        ending(answer, d)


# Function to celebrate or to ask and store a new question and animal
def ending(answer, d):
    if number(answer) == 3:
        new_animal = input("Welk dier dacht je aan? ")
        new_question = input("Wat had ik moeten vragen om dat te raden? ")
        wrong_animal = d.get(2)
        d[2] = {1: new_question, 2: new_animal, 3: wrong_animal}
        answer = input("Okee, doe ik dat de volgende keer. Nogmaals proberen? ")
        again(answer)
    else:
        answer = input("Yay, Bot heeft het goed geraden! Nogmaals proberen? ")
        again(answer)


# Function to play again or end the game
def again(new_game):
    if number(new_game) == 2:
        game()
    else:
        return print("Tot de volgende keer!")


# Function to change the given answer into a number (yes=2 and no=3)
def number(a):
    if any(letter in a for letter in ('j', 'J', 'y', 'Y')):
        return 2
    else:
        return 3


game()
