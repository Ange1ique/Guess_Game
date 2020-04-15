import json


### dict to start with for json file
# animals = {
#     'A': 'Heeft het dier 4 poten? ',
#     'B': 'olifant',
#     'C': {
#         'A': 'Kruipt het op bladeren? ',
#         'B': 'rups',
#         'C': 'huismus'
#     }
# }
# f = open("animals.json","w", encoding="utf-8")
# json = json.dumps(animals, ensure_ascii=False, indent=4)
# f.write(json)
# f.close()


# Open animals.json with all previous stored quesions and animals
with open("animals.json", "r", encoding="utf-8") as f:
    animals = json.load(f)
    f.close()


# Function to start the game
def game():
    print("Bot raadt een dier")
    print("Neem een dier in gedachten...")

    find_next_question(animals)


# Function to find the next question in the dictionary until there are no questions left and then guess for the animal
def find_next_question(d):
    answer = input(d.get('A'))
    if letter(answer) == 'B' and isinstance(d.get('B'), dict):
        find_next_question(d.get('B'))
    elif letter(answer) == 'B':
        rememberAnswer = 'B'
        answer = input("Is het dier een " + d.get('B') + "? ")
        ending(answer, d, rememberAnswer)
    elif letter(answer) == 'C' and isinstance(d.get('C'), dict):
        find_next_question(d.get('C'))
    else:
        rememberAnswer = 'C'
        answer = input("Is het dier een " + d.get('C') + "? ")
        ending(answer, d, rememberAnswer)


# Function to celebrate or to ask and store a new question and animal
def ending(answer, d, rememberAnswer):
    if letter(answer) == 'C':
        new_animal = input("Welk dier dacht je aan? ")
        new_question = input("Wat had ik moeten vragen om dat te raden? ")
        wrong_animal = d.get(rememberAnswer)
        d[rememberAnswer] = {'A': new_question, 'B': new_animal, 'C': wrong_animal}
        with open('animals.json', 'w', encoding='utf-8') as f:
            json.dump(animals, f, ensure_ascii=False, indent=4)
        f.close()
        answer = input("Okee, doe ik dat de volgende keer. Nogmaals proberen? ")
        again(answer)
    else:
        answer = input("Yay, Bot heeft het goed geraden! Nogmaals proberen? ")
        again(answer)


# Function to play again or end the game
def again(new_game):
    if letter(new_game) == 'B':
        game()
    else:
        return print("Tot de volgende keer!")


# Function to change the given answer into a letter (yes=B and no=C)
def letter(a):
    if any(letter in a for letter in ('j', 'J', 'y', 'Y')):
        return 'B'
    else:
        return 'C'


game()
