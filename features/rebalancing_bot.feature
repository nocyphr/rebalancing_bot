Feature: Serverbased Autorebalancing Bot based on a set of Indicators

    As an Investor
    In order to participate in the fluctuations of the cryptomarket more efficiently
    I want a rebalancing bot that outperforms the timeframe- and percentagechange-based bots that already exist
    
    Scenario Outline: The Bot buys or sells according to the provided signal
        Given an indicator
        When I receive a <trade> signal
        Then I <trade> BTC
    Examples: 
        | trade |
        | buy   |
        | sell  |
