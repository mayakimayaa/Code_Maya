"""A simple calculator feature tests."""
import re
from pytest import fixture
from simple_calculator import SillyCalculator
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)


@fixture
def memory():
    return {}

# @fixture()
# def silly_calculator():
#     """Make a Silly Calculator"""
#     return SillyCalculator()


@scenario('simple_calculator.feature', 'Adding two integers')
def test_adding_two_integers():
    """Adding two integers."""
    pass

@scenario('simple_calculator.feature', 'Subtracting two integers')
def test_adding_two_integers():
    """Subtracting two integers."""
    pass

@scenario('simple_calculator.feature', 'Multiplying two integers')
def test_adding_two_integers():
    """Multiplying two integers."""
    pass

@given(parsers.parse('I have an integer {first:d}'))
def i_have_an_integer(memory, first):
    memory['first'] = first

@given(parsers.parse('I have another integer {second:d}'))
def i_have_another_integer(memory, second):
    memory['second'] = second

@when("I add the two integers")
def i_add_the_two_integers(memory):
    """I add the two integers."""
    memory['result'] = memory['first'] + memory['second']

@when("I subtract the two integers")
def i_subtract_the_two_integers(memory):
    """I subtract the two integers."""
    memory['result'] = memory['first'] - memory['second']

@when("I multiply the two integers")
def i_multiply_the_two_integers(memory):
    """I multiply the two integers."""
    memory['result'] = memory['first'] * memory['second']

@then(parsers.parse('The result is {expected:d}'))
def the_result_is(memory,expected):
    assert memory['result'] == expected
