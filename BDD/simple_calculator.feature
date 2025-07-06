Feature: A simple calculator
    performs basic math integer operations
Scenario: Adding two integers
    Given I have an integer <first>
    And I have another integer <second>
    When I add the two integers
    Then The result is <sum>

Examples:
    | first | second | sum |
    | 3     | 5      | 8   |
    | 10    | 15     | 25  |
    | -2    | 4      | 2   |
