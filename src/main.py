import yfinance as yf
import Engine
import strategies.MaCrossover as MaCrossover
import pandas as pd
import Utils





def main():

    tickers = ["PLTR"]

    engine = Engine.Engine(tickers, 10000, "6mo")

    data = engine.getData()

    strategy = MaCrossover.MaCrossover(data)
    signals = tuple(strategy.getData()["Decision"])

    engine.runSignals("PLTR", signals)

    utils = Utils.Utils(strategy.getData())

    print(strategy.getData())

    utils.plot(tickers[0])
    utils.show()















if __name__ == "__main__":
    main()