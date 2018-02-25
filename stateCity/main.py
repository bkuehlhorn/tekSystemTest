'''
create a program that returns both largest city and capital based on user input
 for state name or state abbreviation.
'''
from stateCity.states import States

states = States()

if __name__ == '__main__':
    print('please enter State Name or Abbreviation you wish to know the largest city and capital')

    while True:
        state_input = input('What state: ')
        if len(state_input) == 2:
            state = states.by_abbr(state_input)
        else:
            state = states.by_name(state_input)
        print('entered: ', state_input)
        if state:
            print('In State of {}'.format(state.name))
            print('Largest City:', state.largest_city)
            print('Capital:', state.capital)
        else:
            print('bad input')