
from backtesting import Backtest, Strategy
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf



# Step 1: Download financial data
# Here, we download historical stock data for the ETF "QQQ" (NASDAQ-100 Index) from Yahoo Finance.
data = yf.download("QQQ", start="1999-03-10", end="2024-05-18")
pd.set_option('display.max_columns', None)

# Step 2: Format the dataset
# Keep only the relevant columns: Open, High, Low, Close, Volume. Round OHLC to 2 decimal places.
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = data.columns.get_level_values(0)
data[['Open', 'High', 'Low', 'Close']] = data[['Open', 'High', 'Low', 'Close']].round(2)

print(data)



# Step 3: Define the mean reversion trading strategy with dynamic stop losses
class RollingIBSStrategy(Strategy):

    def init(self):
        # Compute rolling mean of (High - Low) over the last 25 days
        self.rolling_mean = self.I(
            lambda:pd.Series(self.data.High).rolling(window=25).mean() - pd.Series(self.data.Low).rolling(window=25).mean())

        # Compute IBS indicator: (Close - Low) / (High - Low)
        self.ibs = self.I(lambda: (self.data.Close - self.data.Low) / (self.data.High - self.data.Low))

        # Compute the lower band
        self.lower_band = self.I(
            lambda: pd.Series(self.data.High).rolling(window=10).max() - 2.5 * self.rolling_mean)

        # Compute SMA indicator over the last 300 days
        self.sma_300 = self.I(lambda: pd.Series(self.data.Close).rolling(window=300).mean())


    def next(self):
        if ((self.lower_band > self.data.Close) and self.ibs < 0.3):
                self.buy()

        if ((self.data.Close > self.data.High[-2]) or self.sma_300 > self.data.Close) :
                # if SMA is higher than the close, close the position
                self.position.close()

bt = Backtest(data, RollingIBSStrategy, cash = 100_000)

stats = bt.run()

bt.plot()
print(stats)



# Step 4: Plot results and compare strategy performance with buy-and-hold
# Plot the equity curve
strategy_equity = stats['_equity_curve']['Equity']

initial_cash = 100_000
buy_and_hold = data['Close'] / data['Close'].iloc[0] * initial_cash

buy_and_hold = buy_and_hold.reindex_like(strategy_equity)

plt.figure(figsize=(12, 6))
plt.plot(strategy_equity, label="Strategy", color='blue')
plt.plot(buy_and_hold, label="Buy & Hold", color='orange', linestyle='--')

plt.yscale("log")

plt.title("Performance: Dynamic Stop Losses Strategy vs. Buy & Hold (Log Scale)")
plt.xlabel("Time")
plt.ylabel("Equity (Log Scale)")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.savefig('performance_plot.png', dpi=300)

plt.show()



# Plot the drawdown
strategy_equity = stats['_equity_curve']['Equity']
strategy_equity.index = pd.to_datetime(strategy_equity.index)

strategy_peak = strategy_equity.cummax()
strategy_drawdown = (strategy_equity - strategy_peak) / strategy_peak

buy_and_hold = (data['Close'] / data['Close'].iloc[0]) * 100_000
buy_and_hold.index = pd.to_datetime(buy_and_hold.index)
buy_and_hold = buy_and_hold.reindex(strategy_equity.index, method='nearest')

buy_and_hold_peak = buy_and_hold.cummax()
buy_and_hold_drawdown = (buy_and_hold - buy_and_hold_peak) / buy_and_hold_peak

plt.figure(figsize=(12, 6))
plt.plot(strategy_drawdown, label="Strategy Drawdown", color='blue')
plt.plot(buy_and_hold_drawdown, label="Buy & Hold Drawdown", color='orange', linestyle='--')

plt.title("Drawdown: Dynamic Stop Losses Strategy vs. Buy & Hold")
plt.xlabel("Time")
plt.ylabel("Drawdown (%)")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)

plt.savefig('drawdown_plot.png', dpi=300)

plt.show()
