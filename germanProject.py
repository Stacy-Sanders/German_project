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

