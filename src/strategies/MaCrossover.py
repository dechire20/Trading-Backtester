from strategies.Strategy import Strategy

class MaCrossover(Strategy):
    def __init__(self, data):

        self.shortWindow = 10
        self.longWindow = 50

        super().__init__(data)


    def calculate(self):

        self.data["SMA10"] = self.data["Close"].rolling(self.shortWindow).mean()
        self.data["SMA50"] = self.data["Close"].rolling(self.longWindow).mean()

    def genSignals(self):
        self.data["Decision"] = 0

        self.data.loc[self.data["SMA10"] > self.data["SMA50"], "Decision"] = 1
        self.data.loc[self.data["SMA10"] < self.data["SMA50"], "Decision"] = -1

