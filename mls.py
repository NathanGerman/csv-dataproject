import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mls.csv')

plt.figure(figsize=(15,10))
plt.plot(df['city'], df['joined'])
plt.xlabel('City')
plt.ylabel('Joined')
plt.xticks(rotation=45, ha='right')
plt.grid(True)  # I did this to make it easier to read
plt.savefig('chart1.png')

plt.figure(figsize=(15,10))
small = df[df['stadium_capacity'] < 10000]
plt.scatter(small['state'], small['stadium_capacity'], label='<10000')
large = df[df['stadium_capacity'] >= 10000]
plt.scatter(large['state'], large['stadium_capacity'], label='>=10000')
plt.grid(True)
plt.xlabel('State')
plt.ylabel('Stadium Capacity')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.savefig('chart2.png')
plt.show()
