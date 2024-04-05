import pytest
from pytest_bdd import scenarios, given, when, then, parsers


scenarios("features/subtract.feature")


@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def given_cucumbers(start):
    return {"start": start, "eat": 0}


@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(cucumbers, eat):
    cucumbers["eat"] += eat


@then(parsers.parse("I should have {left:d} cucumbers"))
def should_have_left_cucumbers(cucumbers, left):
    assert cucumbers["start"] - cucumbers["eat"] == left


def pytest_bdd_apply_tag(tag, function):
    if tag == 'skip':
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    else:
        # Fall back to the default behavior of pytest-bdd
        return None