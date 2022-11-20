from decimal import Decimal


def valuate_currency_in_usdt(balance, price):
    # to decimal to prevent rounding errors
    list_of_decimals = __convert_to_decimals([balance, price])
    decimal_balance, decimal_price = list_of_decimals[0], list_of_decimals[1]

    result = float(decimal_balance * decimal_price)
    return result


def calculate_positions(value_base_currency, value_quote_currency):
    list_of_decimals = __convert_to_decimals(
        [value_base_currency, value_quote_currency])
    decimal_value_base_currency, decimal_value_quote_currency = list_of_decimals[
        0], list_of_decimals[1]

    delta_raw = decimal_value_base_currency - decimal_value_quote_currency
    half_delta = float(delta_raw / 2)

    list_of_positions = __calculate_position_sizes(half_delta)
    return list_of_positions


def check_delta_is_valid(min_delta, position_size):
    is_valid = (position_size - min_delta) > 0
    return is_valid


def __calculate_position_sizes(half_delta):
    if half_delta < 0:
        return [abs(half_delta), half_delta]
    return [half_delta * (-1), half_delta]


def __convert_to_decimals(list_of_numbers):
    list_of_decimal_results = []
    for number in list_of_numbers:
        stringified_number = str(number)
        decimal_number = Decimal(stringified_number)
        list_of_decimal_results.append(decimal_number)
    return list_of_decimal_results
