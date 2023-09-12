from django.shortcuts import render
from .forms import SICalculator
from .get_lot import calculate_lot_risk
from .choices import INSTRUMENTS, CHOICES


def Indice(request):
    """
    This view function, 'Indice', processes the risk calculation form
    and renders the results on a web page.

    Args:
        request (HttpRequest): The HTTP request object sent by the client.

    Returns:
        HttpResponse: An HTTP response containing
            the rendered risk calculation results page.
    """

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
            selected_instrument = form.cleaned_data['vix']

            lowest_allowable_lot = INSTRUMENTS.get(selected_instrument, 0)

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

    return render(request, 'calculator/calculator.html', context)


def about(request):
    """
    This view function, 'about', renders the "How to Use" page
    with information about Deriv and the Risk Calculator.

    Args:
        request (HttpRequest): The HTTP request object sent by the client.

    Returns:
        HttpResponse: An HTTP response containing the "How to Use" page.
    """

    my_dict = {}
    for choice in CHOICES[1:]:
        my_dict[choice[1]] = INSTRUMENTS[choice[0]]

    context = {'my_dict': my_dict}
    return render(request, 'calculator/about.html', context)

# def render_instruments_table(instruments):
#     # Define the table header
#     table_html = '<table><tr><th>Instrument</th><th>Value/
#                   (lowest lot)</th></tr>'

#     # Loop through the instruments and add them to the table
#     for instrument, value in instruments.items():
#         table_html += f'<tr><td>{CHOICES[instrument]}/
#                        </td><td>{value}</td></tr>'

#     # Close the table tag
#     table_html += '</table>'

#     return table_html
