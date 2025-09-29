import matplotlib.pyplot as plt



class Utils:
    def __init__(self, data):
        self.data = data
        self.ticketers = []

    def plot(self, ticketer):

        enter = self.data["Decision"] == 1
        _exit = self.data["Decision"] == -1
        self.ticketers.append(ticketer)
        plt.plot(self.data["Date"], self.data["Close"], label=ticketer)
        plt.scatter(self.data["Date"][enter], self.data["Close"][enter], label="Enter")
        plt.scatter(self.data["Date"][_exit], self.data["Close"][_exit], label="Exit")

        plt.plot(self.data["Date"], self.data["SMA10"], label="SMA10")
        plt.plot(self.data["Date"], self.data["SMA50"], label="SMA50")
        plt.xlabel("Date")
        plt.ylabel("Price")



    def show(self):
        plt.title(f"Comparison of data of: {self.ticketers}")
        plt.legend()
        plt.savefig("chart.png")