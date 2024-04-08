# Vending Machine Kata with pytest-bdd

This repository is about testing a simple Vending Machine with `pytest-bdd`, a [behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) library for the `pytest` runner.

You will need Python 3.10+ and `pytest` 8+ 

NOTE: pytest is a third-party library, and you should use a virtual environment and `pip` to install it.
[Read here to learn how to use a virtual environment](VIRTUALENV.md)

## Getting Started - a pytest-bdd example

This is an example of how to install and run `pytest-bdd`, a BDD library for the `pytest` runner.

### 1. Install pytest-bdd

**NOTE**: Be sure you are in the root directory of the locally-clones repo; NOT a subdirectory.

```bash
$ pip install pytest-bdd
```

### 2. Run pytest

Running:
```bash
$ pytest getting_started/test_subtract.py
```

Returns:
```bash
===================================== test session starts =====================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-pytest-bdd/getting_started
configfile: pytest.ini
plugins: bdd-7.1.2
collected 1 item                                                                                                  

getting_started/test_subtract.py s                                                       [100%]

===================================== 1 skipped in 0.00s ======================================
```

### 3. Comment out the @skip tag

In the `getting_started/test_subtract.py` file, comment out the first line, with the `@skip` tag, like this:
```gherkin
# @skip
  Scenario: Arguments for given, when, then
    Given there are 7877 cucumbers

    When I eat 641 cucumbers
    And I eat 383 cucumbers

    Then I should have 6854 cucumbers
```

### 4. Rerun pytest

Running:
```bash
$ pytest getting_started/test_subtract.py
```

Returns a failing test:
```bash
===================================== test session starts =====================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-pytest-bdd/getting_started
configfile: pytest.ini
plugins: bdd-7.1.2
collected 1 item                                                                                                  

getting_started/test_subtract.py F                                                       [100%]

========================================== FAILURES ===========================================
___________________ test_arguments_for_given_when_then ________________________________________

fixturefunc = <function should_have_left_cucumbers at 0x101b3ef20>
request = <FixtureRequest for <Function test_arguments_for_given_when_then>>
kwargs = {'cucumbers': {'eat': 1024, 'start': 7877}, 'left': 6854}

    def call_fixture_func(
        fixturefunc: "_FixtureFunc[FixtureValue]", request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

.venv/lib/python3.11/site-packages/_pytest/fixtures.py:913: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cucumbers = {'eat': 1024, 'start': 7877}, left = 6854

    @then(parsers.parse("I should have {left:d} cucumbers"))
    def should_have_left_cucumbers(cucumbers, left):
>       assert cucumbers["start"] - cucumbers["eat"] == left
E       assert (7877 - 1024) == 6854

getting_started/test_subtract.py:20: AssertionError
==================================== short test summary info =============================================
FAILED getting_started/test_subtract.py::test_arguments_for_given_when_then - assert (7877 - 1024) == 6854
========================================= 1 failed in 0.02s ==============================================
```

### 5. Make the scenario pass

Notice that 7877 - 1024 = 6853. We need to fix the scenario's expectation.

To make the scenario pass, change the _Then_ statement (last line) to expect 6853 cucumbers.
```gherkin

    Then I should have 6853 cucumbers
```

Running:
```bash
$ pytest getting_started/test_subtract.py
```

Returns:
```bash
===================================== test session starts =====================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-pytest-bdd/getting_started
configfile: pytest.ini
plugins: bdd-7.1.2
collected 1 item                                                                                                  

getting_started/test_subtract.py .                                                       [100%]

====================================== 1 passed in 0.01s ======================================
```

That's it. We are now ready to test the Vending Machine with `pytest-bdd`.

# Run the Vending Machine Demo

Running:
```bash
$ pytest --verbose  vending/test_vending_machine.py
```

Returns:
```bash
==================================================== test session starts =====================================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0 -- /Users/ ... /vending-machine-pytest-bdd/.venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/ ... /vending-machine-pytest-bdd
configfile: pytest.ini
plugins: bdd-7.1.2
collected 9 items                                                                                                            

vending/test_vending_machine.py::test_inserting_1_coin_adds_25_cents_to_the_total PASSED                               [ 11%]
vending/test_vending_machine.py::test_inserting_2_coins_adds_50_cents_to_the_total PASSED                              [ 22%]
vending/test_vending_machine.py::test_releasing_change_without_inserting_money_returns_0 PASSED                        [ 33%]
vending/test_vending_machine.py::test_releasing_change_after_inserting_money_returns_change PASSED                     [ 44%]
vending/test_vending_machine.py::test_releasing_change_after_inserting_more_money_returns_all_change PASSED            [ 55%]
vending/test_vending_machine.py::test_releasing_change_after_buying_product_with_exact_money_returns_no_change PASSED  [ 66%]
vending/test_vending_machine.py::test_releasing_change_after_buying_product_with_extra_money_returns_change PASSED     [ 77%]
vending/test_vending_machine.py::test_buying_a_product_without_enough_money_should_not_dispense_a_product PASSED       [ 88%]
vending/test_vending_machine.py::test_buying_a_product_with_enough_money_should_dispense_a_product PASSED              [100%]

===================================================== 9 passed in 0.01s ======================================================
```