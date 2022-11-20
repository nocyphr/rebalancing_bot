import pytest
from assertpy import assert_that
from src.timer import *


list_parameters_valuation = [
  (3, 0.456, 1.368),
  (25.02338, 0.456, 11.41066128),
  (16518.12, 19.0, 313844.28),
  (225460.5, 15.165, 3419108.4825),
]
@pytest.mark.parametrize('price_in_usdt, balance, expected', list_parameters_valuation)
def test_that_currency_valuation_is_calculated(price_in_usdt, balance, expected): 
    # Act
    result = valuate_currency_in_usdt(balance, price_in_usdt)

    # Assert
    assert_that(result).is_equal_to(expected)

list_parameters_delta = [
    (500, 578.238, [39.119, -39.119]),
    (578.238, 500, [-39.119, 39.119]), 
]
@pytest.mark.parametrize('value_base_currency, value_quote_currency, expected', list_parameters_delta)
def test_that_positions_are_correctly_calculated(value_base_currency, value_quote_currency, expected):
    # Act
    list_of_positions = calculate_positions(value_base_currency, value_quote_currency)

    # Assert
    assert_that(list_of_positions).is_equal_to(expected)

list_parameters_delta = [
    (15, 39.119, True),
    (19, 9.119, False),
]
@pytest.mark.parametrize('min_delta, position, expected', list_parameters_delta)
def test_that(min_delta, position, expected):
    # Act
    result = check_delta_is_valid(min_delta, position)

    # Assert
    assert_that(result).is_equal_to(expected)
