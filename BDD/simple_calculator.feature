Feature: A simple calculator
         performs basic math integer operations
    Scenario: Adding two integers
        Given I have an integer 40
        And I have another integer 2
        When I add the two integers
        Then The result is 42
