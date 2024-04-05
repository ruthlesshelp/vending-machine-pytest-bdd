@skip
Feature: Step arguments
  Scenario: Arguments for given, when, then
    Given there are 7877 cucumbers

    When I eat 641 cucumbers
    And I eat 383 cucumbers

    Then I should have 6854 cucumbers