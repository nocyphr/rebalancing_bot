Feature: Every x units of time calculate valuation and deltas of portfolio

    As a developer
    In order to execute the signal module only when needed
    I want to check if i exceed the minimum delta for a trade


    Scenario Outline: valuate a currencies
        Given <currency>
        When I check their valuation
        Then I receive it's Value in USDT
    Examples: 
        | currency |
        | USDT     |
        | ETH      |
        | BTC      |

    Scenario: calculate the position size for each currency
        Given the valuations of two currencies
        When I calculate the position size
        Then I receive the position size for each currency

    Scenario: calculate delta
        Given the position size of a currency
        When i take the absolute value of the position
        Then i receive the current delta

    Scenario Outline: Check if delta is big enough for a trade
        Given the <min_delta> of a currency
        And a <current_delta>
        When I compare the two deltas
        Then I am <able_to_trade>
        And I call the Signal Module
    Examples: 
        | min_delta | current_delta | able_to_trade |
        | 19        | 91            | True          | 
        | 19        | 9             | False         |
