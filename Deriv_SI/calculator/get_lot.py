from decimal import Decimal


def calculate_lot_risk(
    account_balance, entry_price, stop_price,
    risk_percent, lowest_allowable_lot
):
    if entry_price > stop_price:
        num_pips = entry_price - stop_price
    else:
        num_pips = stop_price - entry_price

    risk_allowed_amount = account_balance * (risk_percent / 100)
    lot = risk_allowed_amount / num_pips

    if lot <= lowest_allowable_lot:
        lot = lowest_allowable_lot
        total_risk = num_pips * lowest_allowable_lot
    else:
        total_risk = num_pips * lot

    # num_pips = num_pips.quantize(Decimal('0.02'))
    lot = lot.quantize(Decimal('0.003'))
    total_risk = total_risk.quantize(Decimal('0.02'))

    return lot, num_pips, total_risk
