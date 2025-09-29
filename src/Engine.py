import numpy as np
import yfinance as yf
import pandas as pd

data = ""
cash = 0

class Engine():
    def __init__(self, tickers, cash, duration):
        self.iniCash = cash
        self.cash = cash
        self.tickers = tickers
        self.shares = {ticker: 0 for ticker in tickers}
        self.data = yf.download(tickers, period=duration)
        self.data.reset_index(inplace=True)
        pd.set_option('display.max_rows', 500)

    def buy(self, ticker, price):
        if self.cash < price:
            return
        self.shares[ticker] += 1
        self.cash -= price
        print(f"Bought 1 share {ticker} at {price:.2f}")

    def sell(self, ticker, price):
        if self.shares[ticker] <= 0:
            return
        self.shares[ticker] -= 1
        self.cash += price
        print(f"Sold 1 share {ticker} at {price:.2f}")

    def runSignals(self, ticker, signals):
        closes = self.data["Close"][ticker].tolist()
        for day, signal in enumerate(signals):
            price = closes[day]
            if signal == 1 and self.shares[ticker] == 0:
                self.buy(ticker, price)
            elif signal == -1 and self.shares[ticker] > 0:
                self.sell(ticker,price)
        print(f"Final cash: {self.cash}, shares: {self.shares[ticker]}")
        self.evaluation(closes)

    def evaluation(self, prices):

        totalRe = f"{(self.cash / self.iniCash) - 1}% return"

        peak = 0
        dailyReturn = []

        drawdown = []

        for i in range(len(prices)):

            # Sharpe Ratio
            if not i <= 0:
                dailyReturn.append((prices[i] - prices[i-1]) / prices[i-1])

            # Max Draw Down
            if prices[i] > peak:
                peak = prices[i]
            drawdown.append((prices[i] - peak) / peak)



        meanDaily = np.sum(dailyReturn) / len(dailyReturn)
        sharpeRatio = (meanDaily / np.std(dailyReturn)) * np.sqrt(252)

        maxDrawdown = np.min(drawdown)

        print(f"The total return is {totalRe}\n"
              f"The sharpe ratio is {sharpeRatio}\n"
              f"The maximum draw down is {maxDrawdown}")



    def getData(self):
        return self.data.copy()

