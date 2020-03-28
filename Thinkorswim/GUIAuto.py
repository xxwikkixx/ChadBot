import time
import win32.win32gui as win32

def win32lib():
    hwnd = win32.FindWindow(None, "Main@thinkorswim [build 1962]")
    print(hwnd)
    win32.SetForegroundWindow(hwnd)
    win32.ShowWindow(hwnd, 9)


def getfore():
    # print(win32.GetWindowText(win32.GetForegroundWindow()))
    print(win32.GetForegroundWindow())
    

if __name__ == "__main__":
    win32lib()
    # while True:     
    #     win32lib()
    #     getfore()
    #     time.sleep(2)


# CREATE TABLE Stocks (
# 	DateInserted DATE NOT NULL,
# 	Symbol TEXT NOT NULL,
# 	Price DECIMAL NOT NULL,
# 	"Type" TEXT NOT NULL,
# 	Strike DECIMAL NOT NULL,
# 	ExpDate DATE NOT NULL,
# 	DTE INTEGER NOT NULL,
# 	Bid DECIMAL NOT NULL,
# 	Midpoint DECIMAL NOT NULL,
# 	Ask DECIMAL NOT NULL,
# 	"Last" DECIMAL NOT NULL,
# 	Volume INTEGER NOT NULL,
# 	OpenInt INTEGER NOT NULL,
# 	VolOI DECIMAL NOT NULL,
# 	IV DECIMAL(5,2),
# 	Time TIME NOT NULL
# );
