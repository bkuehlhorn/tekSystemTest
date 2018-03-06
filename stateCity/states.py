'''
Load States data and return a State by name or abbr
'''
from collections import namedtuple
import requests


class States(object):
    '''
    Data format from webService is:
    {
      "country" : "USA",
      "name" : "Alabama",
      "abbr" : "AL",
      "area" : "135767SKM",
      "largest_city" : "Birmingham",
      "capital" : "Montgomery"
    }
    '''
    webService = 'http://services.groupkt.com/state/get/USA/all'

    State = namedtuple('State', 'id,country, name, abbr, area, largest_city, capital')
    states = {} # state: State
    stateAbbr = {} # abbr: state


    def __init__(self):
        '''
        Load State details
        '''
        self.response = requests.get(self.webService)

        for state in self.response.json()['RestResponse']['result']:
            self.states[state['name']] = self.State(**state)
            self.stateAbbr[state['abbr']] = state['name']


    def by_abbr(self, abbr):
        '''
        Use abbr to find largest city and capital
        More complex access to states would use self.by_name
        Upper case input

        Could refactor to one line or lambda
        :param abbr:
        :return: state matching abbr or None
        '''
        stateName = self.stateAbbr.get(abbr.upper(), None)
        if stateName is None:
            return None
        state = self.states.get(stateName, None)
        return state


    def by_name(self, name):
        '''
        Use name to find largest city and capital
        capitalize input

        Could refactor to one line or lambda
        :param name:
        :return: state matching abbr or None
        '''
        state = self.states.get(name.title(), None)
        return state
