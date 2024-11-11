from rest_framework import serializers
from .utils.get_lot import calculate_lot_risk
from .utils.instrument_map import CHOICES, INSTRUMENTS


class RiskCalculationSerializer(serializers.Serializer):
    synthetic_index = serializers.ChoiceField(choices=CHOICES)
    account_balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    entry_price = serializers.DecimalField(max_digits=10, decimal_places=5)
    stop_price = serializers.DecimalField(max_digits=10, decimal_places=5)
    risk_percent = serializers.DecimalField(max_digits=5, decimal_places=2)

    # Output-only fields
    lot = serializers.DecimalField(
        max_digits=10, decimal_places=3, read_only=True)
    num_pips = serializers.DecimalField(
        max_digits=10, decimal_places=5, read_only=True)
    total_risk = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)

    def to_representation(self, instance):
        # Get input data for calculation
        account_balance = self.validated_data['account_balance']
        entry_price = self.validated_data['entry_price']
        stop_price = self.validated_data['stop_price']
        risk_percent = self.validated_data['risk_percent']
        synthetic_index = self.validated_data['synthetic_index']

        # Perform calculation
        lowest_allowable_lot = INSTRUMENTS.get(synthetic_index, 0)
        lot, num_pips, total_risk = calculate_lot_risk(
            account_balance,
            entry_price,
            stop_price,
            risk_percent,
            lowest_allowable_lot
        )

        # Return results without saving
        return {
            'synthetic_index': synthetic_index,
            'account_balance': account_balance,
            'entry_price': entry_price,
            'stop_price': stop_price,
            'risk_percent': risk_percent,
            'lot': lot,
            'num_pips': num_pips,
            'total_risk': total_risk
        }
