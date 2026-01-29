# pandas is a Python library used for data manipulation and analysis
# data structures like DataFrames and Series to work with structured data
# functionalities for data cleaning, transformation, aggregation, and visualization

import pandas as pd
import matplotlib.pyplot as plt

# Create a simple data frame
data = {
    'Name': ['Alice', 'David', 'Charlie', 'Bob'],
    'Age': [24, 42, 19, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df) 

# Access rows by index location
print('\nThird Row:\n', df.iloc[2]) 

# Access columns
print("\n Name Column:\n", df['Name'])

# Filter data using a condition
olderThan30 = df[df['Age'] >= 30]
print("\nAdults 30+:\n", olderThan30)

# Add a new column
df['Occupation'] = ['Nurse', 'Biologist', 'Chef', 'Engineer']
print(df)

# Simple stats
print('\nAverage Age:\n', df['Age'].mean())
print('\nMax Age:\n', df['Age'].max())
print('Summary Statistics:\n', df.describe())

# Sort data
sorted_df = df.sort_values(by='Age')
print('\nSorted by Age:\n', sorted_df)

# --------------- Work with data from CSV file ---------------
vehicle_df = pd.read_csv('.\data\Electric_Vehicle_Population_Data.csv')
print("\nVehicle DataFrame:\n", vehicle_df.head()) # Print first 5 rows
vehicle_df.info() # Print column names and some relevant information

# Select each unique vehicle make
vehicle_makes = vehicle_df['Make'].unique()
print(vehicle_makes)

# Filter for vehicles made by Tesla
tesla_df = vehicle_df[vehicle_df['Make'] == 'TESLA']
print("\nTesla vehicles:\n", tesla_df)

# Filter using NOT
non_tesla_df = vehicle_df[vehicle_df['Make'] != 'TESLA']
print("\nNon-Tesla vehicles:\n", non_tesla_df)

# Aggregate some data
# get average electric range by vehicle make
# and filter out 0 values

avg_range_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make')['Electric Range'].mean()
print(avg_range_by_make)

# Multiple aggregates using .agg
avg_range_district_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make').agg(
    mean=('Electric Range', 'mean'), 
    sum=('Legislative District', 'sum')
    )
print(avg_range_district_by_make)

# Finally, we can visualize our data using matplotlib
# We can create a Figure - a matplotlib object that represents the entire plot area
# so you can have multiple plots at once within the area

fig, axes = plt.subplots(1, 2, figsize=(22, 10)) # 2 by 2 figures of figsize dimension

# Plot the average electric range by make as a bar chart
avg_range_by_make.plot(
    kind='bar', ax=axes[0], title="Average Electric Range by Make")
plt.xlabel("Vehicle Make")
plt.ylabel("Average Electric Range (miles)")

non_tesla_df['Model Year'].value_counts().sort_index().plot(
    kind='bar', ax=axes[1], title="Count of Non Tesla by Model Year", xlabel='Model Year', ylabel='Number of Vehicles')
plt.show()

# Export our modified DataFrame to a new CSV file

non_tesla_df.to_csv('./data/Modified_Vehicle_Data.csv', index=False)