import pytest
from assertpy import assert_that
from src.timer import *


list_parameters_valuation = [
  (3, 0.456, 1.368),
  (25.02338, 0.456, 11.41066128),
  (16518.12, 19.0, 313844.28),
  (225460.5, 15.165, 3419108.4825),
]
@pytest.mark.parametrize('crypto_price, crypto_balance, expected', list_parameters_valuation)
def test_that_crypto_valuation_is_calculated(crypto_price, crypto_balance, expected): 
    # Act
    result = calculate_crypto_valuation(crypto_balance, crypto_price)

    # Assert
    assert_that(result).is_equal_to(expected)

list_parameters_delta = [
    (500, 578.238, [39.119, -39.119]),
    (578.238, 500, [-39.119, 39.119]), 
]
@pytest.mark.parametrize('fiat_value, crypto_value, expected', list_parameters_delta)
def test_(fiat_value, crypto_value, expected):
    # Act
    result = calculate_delta(fiat_value, crypto_value)

    # Assert
    assert_that(result).is_equal_to(expected)




# better var names
# <data_type>_<contents_used>_<for>