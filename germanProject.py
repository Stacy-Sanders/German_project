# German practice


def germanGreeting():
    name = input("Hello, what is your name? ")
    timeofDay = input(f"Willkommen, {name}. What time is it: morning, afternoon, evening or night? ")
    timeOfDay = timeofDay.lower()

    if timeOfDay == 'morning':
        return f'Guten Morgen, {name}'

    elif timeOfDay == 'afternoon':
        return f'Guten Tag, {name}'

    elif timeOfDay == 'evening':
        return f'Guten Abend, {name}'

    elif timeOfDay == 'night':
        return f'Gute Nacht, {name}'

    else:
        return f'Sprechen sie Deutsch, {name}?'

greeting = germanGreeting()
print(greeting)


def germanGender():
    gender = input('Hallo and willkommen! Today we are learning Deutsch words. Would you like to learn words for female or male? ')
    age = input('Super! Would you like to learn the words for a child or an adult? ')

    if gender.lower() == 'female':
        if age.lower() == 'child':
            return 'Madchen'
        else:
            return 'Frau'
    else:
        if age.lower() == 'child':
            return 'Junge'
        else:
            return 'Mann'


genderAge = germanGender()
print(genderAge)


def germanNumbers():
    number_to_translate = input('Guten Tag! Today we are going to learn our numbers (0-10) in German! What number would you like to learn first? Press enter when done. ')
    num = int(number_to_translate)

    while num != "":

        if num == 0:
            return 'null'
        elif num == 1:
            return 'eins'
        elif num == 2:
            return 'zwei'
        elif num == 3:
            return 'drei'
        elif num == 4:
            return 'vier'
        elif num == 5:
            return 'funf - the u should have an umlaut (..) on top'
        elif num == 6:
            return 'sechs'
        elif num == 7:
            return 'sieben'
        elif num == 8:
            return 'acht'
        elif num == 9:
            return 'neun'
        elif num == 10:
            return 'zehn'
        else:
            return 'Please enter a number from 0 - 10'

    else:
        return ("Danke!")


numLearn = germanNumbers()
print(numLearn)
