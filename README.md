# Python Backtesting Code for Mean Reversion Strategy

## This repository contains python backtesting code for the article "A Mean Reversion Strategy with 2.11 Sharpe" presented by Quantitativo. 
I tried to reproduce the three strategies the author quantitativo used in his article. 

Here is the link to the article : [A Mean Reversion Strategy with 2.11 Sharpe](https://www.quantitativo.com/p/a-mean-reversion-strategy-with-211)

A **mean reversion strategy** is based on the assumption that asset prices will tend to revert to their historical averages over time, providing opportunities for profitable trades when prices deviate significantly from the mean.

The three python files include the first strategy experiment, followed by the market regime filter and finally the dynamic stop losses. The long&short strategy is not implemented due to lack of data in yahoo finance from 1999 to 2006 (which is crucial to stay consisten with the results obtained).


## User Instructions
Here is how to test this backtesting strategy : 
1. Create a virtual environment
2. Install the following modules in the terminal : 
```bash
pip install backtesting
pip install pandas
pip install matplotlib
pip install yfinance
```
3. To ensure compatibility with the backtesting code, downgrade Bokeh to version 3.1.0 by running:
```bash
pip install bokeh==3.1.0
```
4. Download or copy the three Python scripts and paste the code into separate files in the order listed below (order in the article) : 
- **`first_experiment.py`** – Contains the first strategy experiment.
- **`market_regime_filter.py`** – Implements the market regime filter.
- **`dynamic_stop_losses.py`** – Implements the dynamic stop loss strategy.
