import pytest
from assertpy import assert_that
from src.timer import *

@given(u'the valuations of two currencies')
def step_impl(context):
    context.val_1 = 19
    context.val_2 = 91
    context.expected = [36, -36]


@when(u'I calculate the position size')
def step_impl(context):
    context.result = calculate_positions(context.val_1, context.val_2)


@then(u'I receive the position size for each currency')
def step_impl(context):
    assert_that(context.result).is_equal_to(context.expected)

##########################################################################

@given(u'the position size of a currency')
def step_impl(context):
    context.position_size = -36
    context.expected = 36

@when(u'i take the absolute value of the position')
def step_impl(context):
    context.result = abs(context.position_size)


@then(u'i receive the current delta')
def step_impl(context):
    assert_that(context.result).is_equal_to(context.expected)

##########################################################################

@given(u'the {min_delta:g} of a currency')
def step_impl(context, min_delta):
    context.min_delta = min_delta

@given(u'a {current_delta:g}')
def step_impl(context, current_delta):
    context.current_delta = current_delta
    

@when(u'I compare the two deltas')
def step_impl(context):
    context.result = str(check_delta_is_valid(context.min_delta, context.current_delta))


@then(u'I am {able_to_trade}')
def step_impl(context, able_to_trade):
    assert_that(context.result).is_equal_to(able_to_trade)


@then(u'I call the Signal Module')
def step_impl(context):
    pass


##########################################################

@given(u'{currency}')
def step_impl(context, currency):
    context.currency = currency
    context.api_call_simulation = {
        'USDT': 1, 
        'BTC' : 12000, 
        'ETH' : 1000,
    }
    context.expected = context.api_call_simulation[currency]


@when(u'I check their valuation')
def step_impl(context):
    balance = 1
    price = context.api_call_simulation[context.currency]
    context.result = valuate_currency_in_usdt(balance, price)
    
@then(u'I receive it\'s Value in USDT')
def step_impl(context):
    assert_that(context.result).is_equal_to(context.expected)