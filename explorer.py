#%% Setu some classics
from matplotlib import pyplot as plt
import sys
sys.path.append(r'C:\Users\trotta\Desktop\Shocks\ShockWatcher\foreshock_watcher\solo_swa_loader')
print(sys.path)
#%% Setup more classics + the custom serpentinish stuff
from solo_mag_loader import mag_load
from solo_epd_loader import epd_load
import solo_swa_loader as SWA_load
import datetime as dt
import numpy as np
import pandas as pd
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import matplotlib.dates as mdates
import importlib
#importlib.reload(solo_swa_loader)
#%%
path = r'C:\Users\trotta\Desktop\Shocks\Data\Explorer'  # Directory for the downloaded data in this project
plt.rcParams.update({'font.size': 12})  # increase font size for matplotlib
#from solo_swa_loader import swa_load_grnd_mom
startdate = dt.date(2021, 11, 2)
enddate   = dt.date(2021, 11, 4)
df_mag_burst = mag_load(startdate, enddate, level='l2', data_type='burst', frame='rtn', path=path)
#%%
#from solo_swa_loader import swa_load_grnd_mom
importlib.reload(solo_swa_loader)
df_swa = SWA_load.swa_load_grnd_mom(startdate, enddate, path=path)
# %%
