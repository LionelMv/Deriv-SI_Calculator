"""
This module defines a Django form class 'SICalculator'
used for input validation and handling
in the Synthetic Indices Risk Calculator application.
"""

from django import forms
from .choices import CHOICES


class SICalculator(forms.Form):
    """
    SICalculator class that provides input validation and handling of forms,
    in the Synthetic Indices Risk Calculator application.

    Attributes:
        vix (ChoiceField): A dropdown field for selecting a synthetic index
            from a list of choices provided by 'CHOICES'.
        account_balance (DecimalField): A decimal field for entering
            the account balance in USD, with a minimum value of 1.
        entry_price (DecimalField): A decimal field for entering
            the entry price.
        stop_price (DecimalField): A decimal field for entering
            the stop price.
        risk_percent (DecimalField): A decimal field for entering
            the percentage risk (0 - 100).
    """
    vix = forms.ChoiceField(choices=CHOICES, label='Synthetic Index')
    account_balance = forms.DecimalField(
        label='Account Balance (USD)',
        widget=forms.NumberInput(attrs={'placeholder': 'E.g. 1000'}),
        min_value=1
    )
    entry_price = forms.DecimalField(label='Entry Price:')
    stop_price = forms.DecimalField(label='Stop Price:')
    risk_percent = forms.DecimalField(
        label='Percentage Risk (%)',
        widget=forms.NumberInput(attrs={'placeholder': '0 - 100'}),
        min_value=0,
        max_value=100
    )
