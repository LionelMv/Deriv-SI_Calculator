"""
This module contains a function that calculates the following
for a trading position:
    - lot size
    - number of pips
    - total risk
"""

from decimal import Decimal


def calculate_lot_risk(
    account_balance, entry_price, stop_price,
    risk_percent, lowest_allowable_lot
):
    """
    This function calculates the lot size, number of pips, and total risk
    for a trading position based on the provided parameters.

    Args:
        account_balance (Decimal): The account balance in USD.
        entry_price (Decimal): The entry price for the trading position.
        stop_price (Decimal): The stop price for the trading position.
        risk_percent (Decimal): The percentage of risk (0 - 100)
            for the trading position.
        lowest_allowable_lot (Decimal): The lowest allowable lot size
            for the selected instrument.

    Returns:
        tuple: A tuple containing three Decimal values in the following order:
            - Lot size for the trading position.
            - Number of pips between entry and stop prices.
            - Total risk in USD for the trading position.
    """

    if entry_price > stop_price:
        num_pips = entry_price - stop_price
    else:
        num_pips = stop_price - entry_price

    risk_allowed_amount = account_balance * (risk_percent / 100)
    lot = Decimal(str(risk_allowed_amount / num_pips))
    lowest_allowable_lot = Decimal(str(lowest_allowable_lot))

    if lot <= lowest_allowable_lot:
        lot = lowest_allowable_lot
        total_risk = num_pips * lowest_allowable_lot
    else:
        total_risk = num_pips * lot

    # num_pips = num_pips.quantize(Decimal('0.02'))
    lot = lot.quantize(Decimal('0.003'))
    total_risk = total_risk.quantize(Decimal('0.02'))

    return lot, num_pips, total_risk
