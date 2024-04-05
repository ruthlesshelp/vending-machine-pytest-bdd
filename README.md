# Vending Machine Kata with pytest-bdd

This repository is about testing a simple Vending Machine with `pytest-bdd`, a [behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) library for the `pytest` runner.

You will need Python 3.10+ and `pytest` 8+ 

NOTE: pytest is a third-party library, and you should use a virtual environment and `pip` to install it.
[Read here to learn how to use a virtual environment](VIRTUALENV.md)

# Testing addition - pytest-bdd example

This is an example of how to install and run `pytest-bdd`, a BDD library for the `pytest` runner.

## Install pytest-bdd

**NOTE**: Be sure you are in the root directory of the locally-clones repo; NOT a subdirectory.

```bash
$ pip install pytest-bdd
```

## Run pytest

Running:
```bash
$ pytest getting_started/test_subtract.py
```

Returns:
```bash
=============================================== test session starts ===============================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-pytest-bdd/getting_started
configfile: pytest.ini
plugins: bdd-7.1.2
collected 1 item                                                                                                  

getting_started/test_subtract.py s                                                                          [100%]

=============================================== 1 skipped in 0.00s ================================================
```

# Comment out the @skip tag

In the `getting_started/test_subtract.py` file, comment out the first line, with the `@skip` tag, like this:
```gherkin
# @skip
Feature: Step arguments
  Scenario: Arguments for given, when, then
    Given there are 7877 cucumbers

    When I eat 641 cucumbers
    And I eat 383 cucumbers

    Then I should have 6854 cucumbers
```

## Run pytest

Running:
```bash
$ pytest getting_started/test_subtract.py
```

Returns a failing test:
```bash
=============================================== test session starts ===============================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-pytest-bdd/getting_started
configfile: pytest.ini
plugins: bdd-7.1.2
collected 1 item                                                                                                  

getting_started/test_subtract.py F                                                                          [100%]

==================================================== FAILURES =====================================================
_______________________________________ test_arguments_for_given_when_then ________________________________________

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
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cucumbers = {'eat': 1024, 'start': 7877}, left = 6854

    @then(parsers.parse("I should have {left:d} cucumbers"))
    def should_have_left_cucumbers(cucumbers, left):
>       assert cucumbers["start"] - cucumbers["eat"] == left
E       assert (7877 - 1024) == 6854

getting_started/test_subtract.py:20: AssertionError
============================================= short test summary info =============================================
FAILED getting_started/test_subtract.py::test_arguments_for_given_when_then - assert (7877 - 1024) == 6854
================================================ 1 failed in 0.02s ================================================
```

## Make the scenario pass

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
=============================================== test session starts ===============================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-pytest-bdd/getting_started
configfile: pytest.ini
plugins: bdd-7.1.2
collected 1 item                                                                                                  

getting_started/test_subtract.py .                                                                          [100%]

================================================ 1 passed in 0.01s ================================================
```

That's it. We are now ready to test the Vending Machine with `pytest-bdd`.
