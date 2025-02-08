import os
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import matplotlib.pyplot as plt
import logging

def source_data(periods = ["1y", "2y", "5y", "max"]) -> list:
    paths = []

    logging.info("Reading tickers from file")
    with open("./tickers.txt", 'r') as f:
        tickers = f.read().splitlines()
        logging.info(f"Loaded {len(tickers)} tickers")
    
    if os.path.exists("./data") == False:
        os.mkdir("./data")
        logging.info("Created data directory")

    for TICKER in tickers:
        if os.path.exists(f"./data/{TICKER}") == False:
            os.mkdir(f"./data/{TICKER}")
            logging.info(f"Created {TICKER} directory")
    
        for PERIOD in periods:
            FILE_PATH = f"./data/{TICKER}/{TICKER}_{PERIOD}_data.csv"
            cmd = f"indicators {TICKER} -p {PERIOD} -o {FILE_PATH}"
            os.system(cmd)
            logging.info(f"Downloaded {TICKER} {PERIOD} data")
            
            if os.path.exists(FILE_PATH):
                paths.append(FILE_PATH)
    
    return paths

def load_data(path: str) -> pd.DataFrame:
    logging.info(f"Loading data from {path}")
    return pd.read_csv(path)

def plot_trend(data: pd.DataFrame, ticker: str, period: str):
    if df.empty:
        logging.warning(f"Dataframe is empty")
        return

    TITLE = f"Seasonal Decompose of {TICKER} ETF - {PERIOD} Trend"

    fig, ax = plt.subplots(4, 1, figsize=(12, 10))

    periods = int(len(df["close"]) / 6)
    decompose = seasonal_decompose(df["close"], model="additive", period=periods)

    SAVE_PATH = f"./plots/{TICKER}_{PERIOD}_trend.png"
    ax[0].set_title(TITLE)
    ax[0].plot(df["close"])
    ax[0].grid(True)

    ax[1].plot(decompose.trend)
    ax[1].grid(True)

    ax[2].plot(decompose.seasonal)
    ax[2].grid(True)

    ax[3].scatter(x=range(0,len(decompose.resid)) ,y=decompose.resid, s = 0.7)
    ax[3].grid(True)
    plt.savefig(SAVE_PATH)
    plt.close()
    logging.info(f"Saved {TICKER} {PERIOD} trend plot to {SAVE_PATH}")

def plot_diff(data: pd.DataFrame, ticker: str, period: str):
    if df.empty:
        logging.warning(f"Dataframe is empty")
        return

    SAVE_PATH = f"./plots/{TICKER}_{PERIOD}_diff.png"
    fig, ax = plt.subplots(2, 1, figsize=(12, 10))

    TITLE = f"{TICKER} Close Price - Differenced once - {PERIOD} Trend"
    ax[0].set_title(TITLE)
    ax[0].plot(df["close"].diff().dropna())
    ax[0].grid(True)

    TITLE = f"Partial AutoCorrelation of differencing once"
    plot_pacf(df["close"].diff().dropna(), ax=ax[1]);
    ax[1].set_title(TITLE)
    ax[1].grid(True)

    plt.savefig(SAVE_PATH)
    plt.close()
    logging.info(f"Saved {TICKER} {PERIOD} differenced plot to {SAVE_PATH}")

def plot_corr(data: pd.DataFrame, ticker: str, period: str):
    if df.empty:
        logging.warning(f"Dataframe is empty")
        return

    SAVE_PATH = f"./plots/{TICKER}_{PERIOD}_corr.png"
    fig, ax = plt.subplots(2, 1, figsize=(12, 10))

    TITLE = f"Autocorrelation of {TICKER} ETF - {PERIOD} Trend"
    plot_acf(df["close"], ax=ax[0]);
    ax[0].set_title(TITLE)
    ax[0].grid(True)

    TITLE = f"Partial Autocorrelation of {TICKER} ETF - {PERIOD} Trend"
    plot_pacf(df["close"], ax=ax[1]);
    ax[1].set_title(TITLE)
    ax[1].grid(True)

    plt.savefig(SAVE_PATH)
    plt.close()
    logging.info(f"Saved {TICKER} {PERIOD} correlation plot to {SAVE_PATH}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    paths = source_data()

    if os.path.exists("./plots") == False:
        os.mkdir("./plots")
        logging.info("Created plots directory")
    
    for path in paths:
        df = load_data(path)
        df = df.dropna()
        TICKER = path.split("/")[2]
        PERIOD = path.split("_")[1]
        
        plot_trend(df, TICKER, PERIOD)
        plot_diff(df, TICKER, PERIOD)
        plot_corr(df, TICKER, PERIOD)