# Synthetic Indices Position Size Calculator
#### A risk calculator to calculate the lot size for Deriv's Synthetic Indices.

![image](https://github.com/LionelMv/Deriv-SI_Calculator/assets/102690076/51cf7c51-5b1c-436d-8d8b-94391ff0260f)


## About
This is a risk calculator for Deriv's Synthetic Indices. It calculates the lot size, number of pips and the total risk (USD) for a user's trade based on these parameters:
* The pair chosen.
* Account Balance
* Entry price
* Stop loss price
* Percentage Risk (%)

[Deriv](https://deriv.com/) is an online broker that offers CFDs and other derivatives on forex, stocks & indices, cryptocurrencies, commodities, and derived to millions of registered users across the globe.

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
(Django version == 4.2.4)
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

### How to use the app
Check out this link: https://www.iatlion.tech/calculator/about/

## The Story
Most professional traders always manage their risk for every trade position they enter be it in stocks, forex and even other investments. Synthetic Indices' trading is not any different.

While for stocks and forex there are good risk calculators that you can calculate the lot sizes easily and risk for each trade, no efficient risk calculators have been developed for synthetic indices. Many calculators developed require a user to calculate the pip value for each instrument and then feed the value to the calculator. This is a pain to a user since every instrument has different pip value. All calculators so far also do not offer a way to calculate lot size based on the risk you would like for each trade. In an industry where time is key when taking a trade, this was very inefficient. This brought the need for a risk calculator that you could easily calculate your lot size and risk based on your entry price and stop price.

While it looked easy on paper to implement, each instrument having different minimum lot sizes that you can trade posed a challenge. Creating the logic to fit the calculations well and letting no room for error (since this is people's money we are playing with) led to every day creating many logical mathematical calculations and python functions before getting the simplified template that is this project. 

## Authors
* Lionel Mwangi, [LinkedIn](https://www.linkedin.com/in/lionelmwangi/)
* Rose Njeri, [LinkedIn](https://www.linkedin.com/in/rose-njeri-558732228)