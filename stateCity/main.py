'''
create a program that returns both largest city and capital based on user input
 for state name or state abbreviation.
'''
from states import States

states = States()

if __name__ == '__main__':
    print('Please enter State Name or Abbreviation you wish to know the largest city and capital.')

    while True:
        state_input = input('What state? ("q" to quit): ')
        if state_input.lower() == 'q':
            exit()
        elif len(state_input) == 2:
            state = states.by_abbr(state_input)
        else:
            state = states.by_name(state_input)
        print('Entered: {}'.format(state_input))
        if state:
            print('In State of {}'.format(state.name))
            print('Largest City: {}'.format(state.largest_city))
            print('Capital: {}'.format(state.capital))
        else:
            print('Bad input, try again. ("q" to quit): ')
