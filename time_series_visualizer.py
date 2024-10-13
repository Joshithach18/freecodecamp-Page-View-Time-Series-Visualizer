# time_series_visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the data and set the index to the 'date' column
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# 2. Clean the data by filtering out the top 2.5% and bottom 2.5% of page views
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]

# 3. Draw the line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='tab:red')

    # Set the title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save and return the figure
    fig.savefig('line_plot.png')
    return fig

# 4. Draw the bar plot
def draw_bar_plot():
    # Prepare the data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Pivot the data to get the average page views per month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw the bar plot
    fig = df_bar.plot(kind='bar', figsize=(15, 7), legend=True).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    # Save and return the figure
    fig.savefig('bar_plot.png')
    return fig

# 5. Draw the box plot
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    # Draw the box plots using Seaborn
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save and return the figure
    fig.savefig('box_plot.png')
    return fig
