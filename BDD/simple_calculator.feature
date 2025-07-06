Feature: A simple calculator
    performs basic math integer operations
Scenario: Adding two integers
    Given I have an integer <first>
    And I have another integer <second>
    When I add the two integers
    Then The result is <result>

Examples:
    | first | second | result |
    | 3     | 5      | 8   |
    | 10    | 15     | 25  |
    | -2    | 4      | 2   |

Scenario: Subtracting two integers
    Given I have an integer <first>
    And I have another integer <second>
    When I subtract the two integers
    Then The result is <result>
    
Examples:
  | first | second | result |
  | 3     | 5      | -2     |
  | 10    | 15     | -5     |
  | -2    | 4      | -6     |

Scenario: Multiplying two integers
    Given I have an integer <first>
    And I have another integer <second>
    When I multiply the two integers
    Then The result is <result>
    
Examples:
  | first | second | result |
  | 3     | 5      | 15     |
  | 10    | 15     | 150    |
  | -2    | 4      | -8     |




