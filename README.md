# Synthetic_Indices_Calculator
#### A risk calculator to calculate the lot size for Deriv's Synthetic Indices.

![image](https://github.com/LionelMv/Deriv-SI_Calculator/assets/102690076/51cf7c51-5b1c-436d-8d8b-94391ff0260f)


## About
This is a risk calculator for Deriv's Synthetic Indices. It calculates the lot size, number of pips and the total risk (USD) for a user's trade based on these parameters:
* The pair chosen.
* Account Balance
* Entry price
* Stop loss price
* Percentage Risk (%)

Deriv is an online broker that offers CFDs and other derivatives on forex, stocks & indices, cryptocurrencies, commodities, and derived to millions of registered users across the globe.

## Installation
### Prerequisites
Python3 and pip should be installed in your system.
### Create a virtual environment.
* Windows
```
  pip install virtualenv
  virtualenv .venv
  .venv/Scripts/activate.bat
````
* Linux
```
  sudo apt install python3-virtualenv
  virtualenv .venv
  source .venv/bin/activate
```
### Install Django
```
  pip install Django
```
### Clone the repository locally
```
git clone https://github.com/LionelMv/SI_Risk_Calculator.git
```
### Start up server
```
  python ./SI_RC/manage.py runserver
```
The application should be available at http://localhost:8000/ through your browser

## Authors
* Lionel Mwangi, [LinkedIn](https://www.linkedin.com/in/lionelmwangi/)
* Rose Njeri, [LinkedIn](https://www.linkedin.com/in/rose-njeri-558732228)