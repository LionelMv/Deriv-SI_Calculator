from django.shortcuts import render
from .forms import SICalculator
from decimal import Decimal
from .get_lot import calculate_lot_risk


def Indice(request):
    lot = None
    num_pips = None
    total_risk = None

    if request.method == 'POST':
        form = SICalculator(request.POST)
        if form.is_valid():
            account_balance = form.cleaned_data['account_balance']
            entry_price = form.cleaned_data['entry_price']
            stop_price = form.cleaned_data['stop_price']
            risk_percent = form.cleaned_data['risk_percent']
            lowest_allowable_lot_str = form.cleaned_data['vix']
            lowest_allowable_lot = Decimal(lowest_allowable_lot_str)

            lot, num_pips, total_risk = calculate_lot_risk(
                account_balance, entry_price, stop_price,
                risk_percent, lowest_allowable_lot
            )
    else:
        form = SICalculator()

    context = {
        'form': form, 'lot': lot, 'num_pips': num_pips,
        'total_risk': total_risk
    }

    return render(request, 'calculator/home.html', context)
