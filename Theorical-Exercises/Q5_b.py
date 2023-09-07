import pandas as pd
from scipy.stats import expon  
import matplotlib.pyplot as plt
import numpy as np

# Load latest blocks data from Blockchain explorer
df = pd.read_html('https://www.blockchain.com/explorer/blocks/btc')[0]

# Extract datetime column  
timestamps = df['Block Timestamp (UTC)'].dropna() 

# Convert to datetime and calculate diff
timestamps = pd.to_datetime(timestamps)
block_times = timestamps.diff().dt.total_seconds()  

# Empirical CDF
x = np.sort(block_times.values)  
y = np.linspace(0,1,len(x))
plt.plot(x,y,'.', label='Empirical CDF')

# Exponential model  
λ = 1/600
x_model = np.linspace(0,max(x))
y_model = 1 - np.exp(-λ*x_model)  
plt.plot(x_model,y_model,'--',label='Exponential model')

plt.legend()
plt.xlabel('Inter-block time (seconds)')
plt.ylabel('CDF')
plt.show()