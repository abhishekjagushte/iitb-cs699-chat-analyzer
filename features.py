import pandas as pd

# -1 => Negative
# 0 => Neutral
# 1 => Positive

#Count of messages of selected user per day having k(0/1/-1) sentiment.
def weekly(selected_user,df,k):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    df = df[df['value'] == k]
    return df['day_name'].value_counts()
