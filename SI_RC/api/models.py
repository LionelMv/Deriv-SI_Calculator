"""
If you need to save the calculations, this is a sample model.
If you uncomment this, changes are needed on the serializer and
the views.
"""

# from django.db import models


# class RiskCalculation(models.Model):
#     class SyntheticIndex(models.TextChoices):
#         CHOOSE = '', 'Choose from dropdown'
#         BOOM_1000 = 'b1000', 'Boom 1000 Index'
#         BOOM_300 = 'b300', 'Boom 300 Index'
#         BOOM_500 = 'b500', 'Boom 500 Index'
#         CRASH_1000 = 'c1000', 'Crash 1000 Index'
#         CRASH_300 = 'c300', 'Crash 300 Index'
#         CRASH_500 = 'c500', 'Crash 500 Index'
#         JUMP_10 = 'j10', 'Jump 10 Index'
#         JUMP_100 = 'j100', 'Jump 100 Index'
#         JUMP_25 = 'j25', 'Jump 25 Index'
#         JUMP_50 = 'j50', 'Jump 50 Index'
#         JUMP_75 = 'j75', 'Jump 75 Index'
#         RANGE_100 = 'r100', 'Range Break 100 Index'
#         RANGE_200 = 'r200', 'Range Break 200 Index'
#         STEP = 'si', 'Step Index'
#         VOLATILITY_10_1S = 'v10(1s)', 'Volatility 10 (1s) Index'
#         VOLATILITY_10 = 'v10', 'Volatility 10 Index'
#         VOLATILITY_100_1S = 'v100(1s)', 'Volatility 100 (1s) Index'
#         VOLATILITY_100 = 'v100', 'Volatility 100 Index'
#         VOLATILITY_200_1S = 'v200(1s)', 'Volatility 200 (1s) Index'
#         VOLATILITY_25_1S = 'v25(1s)', 'Volatility 25 (1s) Index'
#         VOLATILITY_25 = 'v25', 'Volatility 25 Index'
#         VOLATILITY_300_1S = 'v300(1s)', 'Volatility 300 (1s) Index'
#         VOLATILITY_50_1S = 'v50(1s)', 'Volatility 50 (1s) Index'
#         VOLATILITY_50 = 'v50', 'Volatility 50 Index'
#         VOLATILITY_75_1S = 'v75(1s)', 'Volatility 75 (1s) Index'
#         VOLATILITY_75 = 'v75', 'Volatility 75 Index'
#         VOLATILITY_150_1S = 'v150(1s)', 'Volatility 150 (1s) Index'
#         VOLATILITY_250_1S = 'v250(1s)', 'Volatility 250 (1s) Index'

#     synthetic_index = models.CharField(
#         max_length=50,
#         choices=SyntheticIndex.choices,
#         verbose_name="Synthetic Index"
#     )
#     account_balance = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         verbose_name="Account Balance (USD)"
#     )
#     entry_price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         verbose_name="Entry Price"
#     )
#     stop_price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         verbose_name="Stop Price"
#     )
#     risk_percent = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         verbose_name="Percentage Risk (%)"
#     )
#     lot = models.DecimalField(
#         max_digits=10,
#         decimal_places=3,
#         null=True,
#         blank=True,
#         verbose_name="Lot Size"
#     )
#     num_pips = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         verbose_name="Number of Pips"
#     )
#     total_risk = models.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         verbose_name="Total Risk (USD)"
#     )

#     def __str__(self):
#         return f"{self.synthetic_index} - {self.account_balance} USD"
