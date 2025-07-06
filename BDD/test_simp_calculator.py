"""A simple calculator feature tests."""
import re
from pytest import fixture
from simple_calculator import SillyCalculator
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@fixture()
def silly_calculator():
    """Make a Silly Calculator"""
    return SillyCalculator()


# @scenario('simple_calculator.feature', 'Adding two integers')
def test_adding_two_integers():
    """Adding two integers."""
    pass

@given('I have an integer {first:d}')
def i_have_an_integer(context, first):
    context.first = first

@given('I have another integer {second:d}')
def i_have_another_integer(context, second):
    context.second = second

@when("I add the two integers")
def i_add_the_two_integers(context):
    """I add the two integers."""
    context.sum = context.first+context.second


@then('The result is {expected:d}')
def the_result_is(context,expected):
    assert context.sum == expected
