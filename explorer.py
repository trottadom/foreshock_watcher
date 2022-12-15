#%%
from matplotlib import pyplot as plt
import sys
sys.path.append(r'C:\Users\trotta\Desktop\Shocks\ShockWatcher\foreshock_watcher\solo_swa_loader')
#sys.path.insert(0,r'C:\Users\trotta\Desktop\Shocks\ShockWatcher\solo_swa_loader')
#sys.path.append("C:/Users/trotta/Desktop/Shocks/ShockWatcher/solo_swa_loader")
print(sys.path)

#import os
#path = r'C:\Users\trotta\Desktop\Shocks\ShockWatcher\solo_swa_loader'
#os.environ['PATH'] += ':'+path
from solo_mag_loader import mag_load
from solo_epd_loader import epd_load
from solo_swa_loader import swa_load_grnd_mom
import datetime as dt
import numpy as np
import pandas as pd
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.dates as mdates
#%%