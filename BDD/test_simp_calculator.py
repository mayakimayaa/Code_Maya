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

@given('I have an integer <first>')
def i_have_an_integer(silly_calculator, first):
    silly_calculator.first_int = int(first)


@given('I have another integer <second>')
def i_have_another_integer(silly_calculator, second):
    silly_calculator.second_int = int(second)


@when("I add the two integers")
def i_add_the_two_integers(silly_calculator):
    """I add the two integers."""
    silly_calculator.add()


@then('The result is <sum>')
def the_result_is(silly_calculator,sum):
    assert sum == silly_calculator.result
