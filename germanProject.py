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
    number_to_translate = int(input('Guten Tag! Today we are going to learn our numbers (0-10) in German! What number would you like to learn first? '))

    if number_to_translate == 0:
        return 'null'
    elif number_to_translate == 1:
        return 'eins'
    elif number_to_translate == 2:
        return 'zwei'
    elif number_to_translate == 3:
        return 'drei'
    elif number_to_translate == 4:
        return 'vier'
    elif number_to_translate == 5:
        return 'funf - the u should have an umlaut (..) on top'
    elif number_to_translate == 6:
        return 'sechs'
    elif number_to_translate == 7:
        return 'sieben'
    elif number_to_translate == 8:
        return 'aucht'
    elif number_to_translate == 9:
        return 'neun'
    elif number_to_translate == 10:
        return 'zehn'
    else:
        return 'Please enter a number from 0 - 10'

numLearn = germanNumbers()
print(numLearn)
