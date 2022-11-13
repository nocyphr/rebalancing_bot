Feature: A Signal to buy or sell is sent based on an indicator

    As a Developer
    In order to tell my balancing bot what to do
    I want to have a framework to plug-in indicators

    Background: Indicators are recalculated at a set timeinterval
        Given I have a set Time Interval
        And I have an API to get OCHLV data for a specified timeframe

    Scenario: 
        Given the Indicator calculation is triggered
        When the signal-module is executed
        Then I receive a signal