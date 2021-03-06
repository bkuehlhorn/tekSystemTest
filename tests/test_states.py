'''


'''
import pytest
from stateCity.states import States

def test_default_initialt():
    states = States()
    assert states


@pytest.fixture(scope='session')
def init_states():
    states = States()
    return states

def test_request_object_status_code_200(init_states):
    assert init_states.response.status_code == 200


def test_get_state_name_Illinois(init_states):
    assert init_states.by_name('Illinois')


def test_get_state_name_illinois(init_states):
    assert init_states.by_name('illinois')


def test_get_state_name_Xxxx(init_states):
    assert init_states.by_name('Xxxx') is None


def test_get_state_abbr_IL(init_states):
    assert init_states.by_abbr('IL')


def test_get_state_abbr_il(init_states):
    assert init_states.by_abbr('il')


def test_get_state_abbr_ny(init_states):
    assert init_states.by_abbr('ny')


def test_get_state_abbr_XX(init_states):
    assert init_states.by_abbr('XX') is None

def test_get_55_states(init_states):
    assert len(init_states.states) is 55
