# Python Backtesting Code for Mean Reversion Strategy

## This repository contains python backtesting code for the article "A Mean Reversion Strategy with 2.11 Sharpe" presented by Quantitativo. 

I tried to reproduce the three strategies the author quantitativo used in his article. 

Here is the link to the article : https://www.quantitativo.com/p/a-mean-reversion-strategy-with-211

The three python files include the first strategy experiment, followed by the market regime filter and finally the dynamic stop losses. The long&short strategy is not implemented due to lack of data in yahoo finance from 1999 to 2006.


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
3. Downgrade bokeh:
```bash
pip install bokeh==3.1.0
```
4. Copy and paste the code, in different files, **`first_experiment.py`** then   **`market_regime_filter.py`** followed by **`dynamic_stop_losses.py`** in the article order.
