# Write your code here :-)
# German practice


def germanGreeting():
    name = input("Hello, what is your name? ")
    timeOfDay = input(f"Willkommen, {name}. What time is it: morning, afternoon, evening or night? ")
    if timeOfDay == 'morning':
        print(f'Guten Morgen, {name}')

    elif timeOfDay == 'afternoon':
        print(f'Guten Tag, {name}')

    elif timeOfDay == 'evening':
        print(f'Guten Abend, {name}')

    elif timeOfDay == 'night':
        print(f'Gute Nacht, {name}')

    else:
        print(f'Sprechen sie Deutsch, {name}?')

germanGreeting()
