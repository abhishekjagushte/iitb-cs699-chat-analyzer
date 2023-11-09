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

#Count of messages of selected user per date having (0, 1, -1) sentiment.
def daily(selected,df,sentimnent):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value'] == sentiment]
    daily = df.groupby('only_date').count()['message'].reset_index()
    return daily

#Count of messages of selected user per {year + month number + month} having (0, 1, -1) sentiment.
def timeline(selected,df,sentiment):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value']==-sentiment]
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

#Percentage of message contributed having (0, 1, -1) sentiment.
def percentage(df,sentiment):
    df = round((df['user'][df['value']==sentiment].value_counts() / df[df['value']==sentiment].shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return df
