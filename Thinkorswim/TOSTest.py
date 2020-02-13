import tosdb
import time
import csv
import numpy as np
import pandas as pd
from datetime import datetime
from tosdb.intervalize import ohlc
from timeit import default_timer

tosdb.init(dllpath=r"C:\TOSDataBridge\bin\Release\x64\tos-databridge-0.9-x64.dll")
block = tosdb.TOSDB_DataBlock(100000, True)
ohlcblock = ohlc.tosdb.TOSDB_ThreadSafeDataBlock(100000)
block.add_items("/MES:XCME", "/MYM:XCBT")
block.add_topics(
    "OPEN",
    "HIGH",
    "LOW",
    "bid",
    "ask",
    "volume",
    "LAST",
    "LASTX",
    "BIDX",
    "ASKX",
    "LAST_SIZE",
    "CUSTOM5",
    "CUSTOM9",
)
time.sleep(2)


def getLastPrice(symbol):
    return block.get(symbol, "LAST")
    # return block.get(symbol, "LAST", date_time=True)


def tosDBohlc():
    intrv = ohlc.TOSDB_OpenHighLowCloseIntervals(ohlcblock, 60)
    print(intrv.get("/ES:XCME", "OPEN"))
    tosdb.clean_up()


def tosOHLCMinute(symbol):
    val = block.get(symbol, "CUSTOM9", date_time=False)
    open, high, low, close = val.split("|")
    open = float(open.replace(",", ""))
    high = float(high.replace(",", ""))
    low = float(low.replace(",", ""))
    close = float(close.replace(",", ""))
    return open, high, low, close


def tosVolTrailingStopSTUDY(symbol):
    val, times = block.get(symbol, "CUSTOM5", date_time=True)
    if val == "1.0":
        return True
    elif val == "-1.0":
        return False
    tosdb.clean_up()


# def tosPlotChart():
#     pass

# def tosPlotChart():
#     pass

# def buyPos():
#     pass

# def sellPos():
#     pass

# def reversePos():
#     pass

# def flattenPos():
#     pass

# def writeCSV():
#     with open('tradelog.csv','a', newline='') as newFile:
#     newFileWriter = csv.writer(newFile)
#     newFileWriter.writerow([1, 'test'])


position_taken = 0  # Position is open or closed
trades_taken = 0  # How many trades taken long and short combined.
current_trade = ""  # Current position of long or trade closed
buy_price = 0
flatten_price = 0

if __name__ == "__main__":
    # tosPlotChart()
    ticker = "/MES:XCME"
    current_price = getLastPrice(ticker)

    while True:
        """
        if signal is long(True) and postion is not taken
        Increase trade count
        Take position
        Set the trade Long
        """
        if tosVolTrailingStopSTUDY(ticker) == True and position_taken != 1:
            trades_taken += 1
            position_taken = 1
            current_trade = "Long"
            buy_price = getLastPrice(ticker)
            print("Trade Taken")
            print(
                "Trades"
                + " | "
                + "Position"
                + " | "
                + "Current Signal"
                + " | "
                + "Buy Price"
            )
            print(trades_taken, position_taken, current_trade, buy_price)
            print(" ")

        """
        if signal is long(true) and postion is already taken
        output the positions
        """
        if tosVolTrailingStopSTUDY(ticker) == True and position_taken == 1:
            print("Existing Positions ")
            print(
                "Trades"
                + " | "
                + "Position"
                + " | "
                + "Current Signal"
                + " | "
                + "Buy Price"
            )
            print(trades_taken, position_taken, current_trade, buy_price)
            print(" ")

        """
        if signal is Short(False) and position is taken
        set position taken to closed 
        """
        if tosVolTrailingStopSTUDY(ticker) == False and position_taken == 1:
            position_taken = 0
            current_trade = "Trade Closed"
            flatten_price = getLastPrice(ticker)
            print("Short Signal Recieved, Trade Closed ")
            print(
                "Trades"
                + " | "
                + "Position"
                + " | "
                + "Current Signal"
                + " | "
                + "Flatten Price"
            )
            print(trades_taken, position_taken, current_trade, flatten_price)
            print(" ")

        """
        if signal is Short(False) and position is not taken
        output the positions 
        """
        if tosVolTrailingStopSTUDY(ticker) == False and position_taken != 1:
            buy_price = 0
            flatten_price = 0
            print("No Trade ")
            print("Trades" + " | " + "Position" + " | " + "Current Signal")
            print(trades_taken, position_taken, current_trade)
            print(" ")

        time.sleep(5)
