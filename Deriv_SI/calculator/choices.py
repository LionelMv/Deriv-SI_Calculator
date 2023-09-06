"""
This module defines two related data structures:
- CHOICES: A list of tuples containing instrument choices for a dropdown menu.
Each tuple consists of a value and a display label.
- INSTRUMENTS: A dictionary that maps instrument values to their
corresponding lowest allowable lot values.

CHOICES is used to populate a dropdown menu in a web application,
allowing users to select a specific instrument.

INSTRUMENTS is used to associate each instrument value
with its lowest allowable lot size, providing data for risk calculations
based on user selections.

The data in these structures is used in the application
to facilitate instrument selection and risk calculation processes.

Example Usage:
- CHOICES: ('b1000', 'Boom 1000 Index') is an option in the dropdown where
'b1000' is the value and 'Boom 1000 Index' is the display label.
- INSTRUMENTS: 'b1000': 0.2 indicates that 'b1000' instrument
has a lowest allowable lot size of 0.2.

These structures help in providing a user-friendly interface and data integrity
for the Synthetic Indices Risk Calculator application.
"""


CHOICES = [
    ('', 'Choose from dropdown'),
    ('b1000', 'Boom 1000 Index'),
    ('b300', 'Boom 300 Index'),
    ('b500', 'Boom 500 Index'),
    ('c1000', 'Crash 1000 Index'),
    ('c300', 'Crash 300 Index'),
    ('c500', 'Crash 500 Index'),
    ('j10', 'Jump 10 Index'),
    ('j100', 'Jump 100 Index'),
    ('j25', 'Jump 25 Index'),
    ('j50', 'Jump 50 Index'),
    ('j75', 'Jump 75 Index'),
    ('r100', 'Range Break 100 Index'),
    ('r200', 'Range Break 200 Index'),
    ('si', 'Step Index'),
    ('v10(1s)', 'Volatility 10 (1s) Index'),
    ('v10', 'Volatility 10 Index'),
    ('v100(1s)', 'Volatility 100 (1s) Index'),
    ('v100', 'Volatility 100 Index'),
    ('v200(1s)', 'Volatility 200 (1s) Index'),
    ('v25(1s)', 'Volatility 25 (1s) Index'),
    ('v25', 'Volatility 25 Index'),
    ('v300(1s)', 'Volatility 300 (1s) Index'),
    ('v50(1s)', 'Volatility 50 (1s) Index'),
    ('v50', 'Volatility 50 Index'),
    ('v75(1s)', 'Volatility 75 (1s) Index'),
    ('v75', 'Volatility 75 Index'),
    ('v150(1s)', 'Volatility 150 (1s) Index'),
    ('v250(1s)', 'Volatility 250 (1s) Index')
]


INSTRUMENTS = {
    'b1000': 0.2,
    'b300': 0.1,
    'b500': 0.2,
    'c1000': 0.2,
    'c300': 0.5,
    'c500': 0.2,
    'j10': 0.01,
    'j100': 0.01,
    'j25': 0.01,
    'j50': 0.01,
    'j75': 0.01,
    'r100': 0.01,
    'r200': 0.01,
    'si': 0.1,
    'v10(1s)': 0.2,
    'v10': 0.3,
    'v100(1s)': 0.1,
    'v100': 0.2,
    'v200(1s)': 0.02,
    'v25(1s)': 0.005,
    'v25': 0.5,
    'v300(1s)': 1,
    'v50(1s)': 0.005,
    'v50': 3,
    'v75(1s)': 0.005,
    'v75': 0.001,
    'v150(1s)': 0.001,
    'v250(1s)': 0.001
}
