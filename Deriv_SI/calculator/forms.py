from django import forms
from .choices import CHOICES


class SICalculator(forms.Form):
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
