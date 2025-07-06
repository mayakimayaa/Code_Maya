Feature: A simple calculator
    performs basic math integer operations
Scenario: Adding two integers
    Given I have an integer <first>
    And I have another integer <second>
    When I add the two integers
    Then The result is <sum>
