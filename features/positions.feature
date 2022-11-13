Feature: I calculate the correct amount to buy or sell based on current valuations

    As a Developer
    In order to  rebalance the current portfolio correctly
    I want to calculate the correct position size to buy or sell

    Background: an indicator delivers tradesignals
        Given I received a signal

    Scenario Outline: calculate delta
        Given <usd_amount>
        And <crypto_value>
        And I have a single unit of the crypto-currency
        When I subtract both from each other
        Then I receive <position_size> 
    Examples:
    | usd_amount  | crypto_value  | position_size |
    | 1000.00000  | 1025.00000    |  0.01220      |
    | 1050.00000  | 1000.00000    |  0.02500      |
    
    Scenario Outline: Check if a trade can be placed
        Given <position_size>
        And <minimum_position_size>
        When I check if i have a valid trade
        Then I receive <result>
    Examples: 
        | position_size | minimum_position_size | result | 
        | 1             | 2                     | False  |
        | 2             | 2                     | True   |
        | 999           | 1                     | True   |
