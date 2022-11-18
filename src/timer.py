from decimal import Decimal




def calculate_crypto_valuation(crypto_balance, crypto_price):
    # to decimal to prevent rounding errors
    decimal_crypto_balance = __convert_to_decimals(crypto_balance)
    decimal_crypto_price = __convert_to_decimals(crypto_price)

    result = float(decimal_crypto_balance * decimal_crypto_price)
    return result

def calculate_delta(fiat_value, crypto_value): 
    decimal_fiat_value = __convert_to_decimals(fiat_value)
    decimal_crypto_value = __convert_to_decimals(crypto_value)

    delta_raw = decimal_fiat_value - decimal_crypto_value

    half_delta = float(delta_raw / __convert_to_decimals(2))
    
    if half_delta < 0: 
        return [abs(half_delta), half_delta]
    return [half_delta * (-1), half_delta]













def __convert_to_decimals(number):
    stringified_number = str(number)
    decimal_number = Decimal(stringified_number)
    return decimal_number