import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from vending_machine import VendingMachine

scenarios("features/insert_coin.feature")
scenarios("features/release_change.feature")
scenarios("features/buy_product.feature")


@given("I'm at a vending machine", target_fixture="vending_machine")
def given_vending_machine():
    vending_machine = VendingMachine()
    return vending_machine


@given(parsers.parse("a vending machine with {cents:d} cents"))
def given_starting_balance(vending_machine, cents) -> VendingMachine:
    assert cents >= 0
    assert type(cents) is int
    number_of_quarters: int = cents/25

    vending_machine.insert_coin(number_of_quarters)

    return vending_machine


@when("I insert a coin")
def insert_a_coin(vending_machine: VendingMachine):
    vending_machine.insert_coin(1)


@then(parsers.parse("the vending machine should have a total of {expected_payment:d} cents"))
def should_have_total_payment(vending_machine: VendingMachine, expected_payment):
    actual_payment = vending_machine.get_payment()
    assert actual_payment == expected_payment


@when("I buy a product")
def insert_a_coin(vending_machine: VendingMachine):
    vending_machine.buy_product()


@then("the vending machine should not dispense a product")
def should_not_dispense_product(vending_machine: VendingMachine):
    had_product = vending_machine.get_product()
    assert had_product == False


@then("the vending machine should dispense a product")
def should_dispense_product(vending_machine: VendingMachine):
    had_product = vending_machine.get_product()
    assert had_product == True

@when("I release change")
def release_change(vending_machine: VendingMachine):
    vending_machine.release_change()


@then(parsers.parse("the vending machine should release {expected_return:d} cents"))
def should_have_released_expected_change(vending_machine: VendingMachine, expected_return):
    actual_return = vending_machine.get_coin_return()
    assert actual_return == expected_return
