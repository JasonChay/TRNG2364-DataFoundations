import matplotlib.pyplot as plt
import pandas as pd

# Challenge 1

#A weather station recorded the average temperature over 7 days.
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [12, 14, 15, 13, 16, 18, 17]

#Challenge Tasks

#Create a line plot showing temperature changes over the week.

'''Add:

A meaningful title

X-axis label

Y-axis label

Use circle markers and a dashed line.

Highlight the warmest day with a different color.

Add a grid.

(Bonus) Annotate the warmest temperature value on the chart.
'''

plt.plot(days, temperatures, marker='o', linestyle='--', color='b')
plt.xlabel('Day')
plt.ylabel('Average Temperature (F)')
plt.title('Average Temperatures This Week')
plt.grid(True)

# Highlight max temp in red
warmest_day, max_temp = days[temperatures.index(max(temperatures))], max(temperatures)
plt.scatter(warmest_day, max_temp, color='red', zorder=5, label=f'Max temp: {max_temp} F') # overlay on top of line plot
plt.legend() # annotate max temp

plt.show()

# Challenge 2

#A small shop tracked its monthly sales for the first half of the year.

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [1200, 1350, 1100, 1500, 1600, 1550]
}

df = pd.DataFrame(data)

'''
Challenge Tasks

Use pandas to inspect the data.

Create a line plot of sales over the months using matplotlib.

Add:

A title

X-axis label

Y-axis label

Highlight the month with the highest sales.

Add a grid.

(Bonus) Display the exact sales value for the highest month on the chart.
'''

df.plot(kind='line', title='Total Sales By Month', xlabel='Month', ylabel='Sales')
plt.xticks(range(0, len(df['Month'])), df['Month']) # change x-ticks from df index to Month
plt.grid(True)

# Highlight x-label with max sales
max_row = df[df['Sales'] == df['Sales'].max()]
max_row_index = max_row.index # first get row of max sales in df
target_index_int = max_row_index.item() # convert index to int
x_labels = plt.gca().get_xticklabels() # get x-tick labels
x_labels[target_index_int].set_color("red")

max_sales = max(data['Sales'])
max_sales_index = data['Sales'].index(max_sales)
max_sales_month = data['Month'][max_sales_index]

plt.annotate(
    f"Peak Sales: ${max_sales}",
    xy=(max_sales_index, max_sales),
    xytext=(max_sales_index - 2, max_sales),
    arrowprops=dict(facecolor='black', shrink=0.05, width=2, headwidth=8)
)
plt.show()