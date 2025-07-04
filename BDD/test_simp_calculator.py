"""A simple calculator feature tests."""

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


@given("I have an integer 40")
def i_have_an_integer_40(silly_calculator):
    """I have an integer 40."""
    silly_calculator.first_int = 40


@given("I have another integer 2")
def i_have_another_integer_2(silly_calculator):
    """I have another integer 2."""
    silly_calculator.second_int = 2


@when("I add the two integers")
def i_add_the_two_integers(silly_calculator):
    """I add the two integers."""
    silly_calculator.add()


@then("The result is 42")
def the_result_is_42(silly_calculator):
    """The result is 42."""
    assert 42 == silly_calculator.result
