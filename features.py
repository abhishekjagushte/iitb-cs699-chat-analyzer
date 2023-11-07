import pandas as pd

#-1 => Negative
# 0 => Neutral
# 1 => Positive

#Count of messages of selected user per day having (0, 1, -1) sentiment.
def weekly(selected,df,sentiment):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value'] == sentiment]
    return df['day_name'].value_counts()

#Count of messages of selected user per month having (0, 1, -1) sentiment.
def monthly(selected,df,sentiment):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value'] == sentiment]
    return df['month'].value_counts()

#Count of messages of selected user per date having (0, 1, -1) sentiment
def daily(selected,df,sentimnent):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value'] == sentiment]
    daily = df.groupby('only_date').count()['message'].reset_index()
    return daily
