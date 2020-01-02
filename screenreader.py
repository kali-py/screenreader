import wx
import warnings


warnings.filterwarnings("ignore")  # Deprive all warnings
wxapp = wx.App()  # Need to create an App instance before doing anything

from lib_screenreader import screen_reader

# Interval for the amount of screen shots that are to be taken in that interval
# Interval=0 or not specified: Means only one screenshot
# wx = wx library after app has been initialized

print("[+] ScreenReader initialized!")

screen_reader(wx=wx, interval=1)
