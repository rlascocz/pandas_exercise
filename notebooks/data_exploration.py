#import Data science libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Test print package
x="andres"
print(F"Hola: {x}")

# Create a sample DataFrame
data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Revenue': [50000, 3000, 60000, 50000, 100000]}

df = pd.DataFrame(data)

# Plot the data using Pandas
df.plot(x='Year', y='Revenue', kind='line', marker='o', linestyle='-', color='b', figsize=(8, 6))

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.title('Revenue Over Time')

# Show the plot
plt.grid(True)
plt.show()
