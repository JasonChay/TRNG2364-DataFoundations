import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/steps.csv')
try:
    user_input = int(input("How many days of data would you like to analyze (1-7)?\n"))
    df = df.iloc[0:user_input]
except ValueError:
    print("invalid input")


# Statistics using numpy
np_arr = df.to_numpy()
print("Average steps:", np_arr[:, 1].mean()) # selecting all rows and only column 1
print("Maximum steps:", np_arr[:, 1].max())
print("Minimum steps:", np_arr[:, 1].min())

# print(df['Steps'].mean())
# print(df['Steps'].max())
# print(df['Steps'].min())

mask = df['Steps'] == df['Steps'].max()

plt.bar(df['Day'], df['Steps'], color='g')
plt.bar(df['Day'][mask], df['Steps'][mask], color='r')
plt.title('Steps per Day of Week')
plt.xlabel('Day')
plt.ylabel('Steps')
plt.grid(True)
plt.show()