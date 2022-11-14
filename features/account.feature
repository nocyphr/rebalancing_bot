Feature: Serverbased Autorebalancing Bot based on a set of Indicators

    As an investor
    In order to keep an eye on valuation and transactions of my portfolio
    I want a tool that shows historical balances, actions and transactions
    
    Background: API exists
        Given an API
        And an API key

    Scenario: Getting historical data from API
        When I check for <endpoint>
        Then I receive historical <data>
    Examples: 
        | endpoint      | data            |
        | balance       | datetimes       |
        | balance       | usd-balances    |
        | balance       | crypto-balances |
        | actions       | datetimes       |
        | actions       | crypto-amounts  |
        | actions       | prices          |
        | transactions  | datetimes       |
        | transactions  | prices          |
        | transactions  | crypto-amount   |
        | transactions  | usd-amount      |
