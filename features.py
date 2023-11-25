import pandas as pd
from wordcloud import WordCloud
from collections import Counter

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
def daily(selected,df,sentiment):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value'] == sentiment]
    daily = df.groupby('only_date').count()['message'].reset_index()
    return daily

#Count of messages of selected user per {year + month number + month} having (0, 1, -1) sentiment.
def timeline(selected, df, sentiment):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value'] == -sentiment]
    timeline = df.groupby(['year', 'month_num', 'month', 'day']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(str(timeline['day'][i]) + "-" + str(timeline['month_num'][i]) + "-" + str(timeline['year'][i]))
    timeline['day'] = time
    return timeline

#Percentage of message contributed having (0, 1, -1) sentiment.
def percentage(df,sentiment):
    df = round((df['user'][df['value']==sentiment].value_counts() / df[df['value']==sentiment].shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return df

# Wordcloud from words in message.
def wordcloud(selected,df,sentiment):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected != 'Overall':
        df = df[df['user'] == selected]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    temp['message'] = temp['message'][temp['value'] == sentiment]
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

# Common words having (0, 1, -1) sentiment
def common_words(selected,df,sentiment):
    f = open('stop_hinglish.txt','r')
    stop_words = f.read()
    if selected != 'Overall':
        df = df[df['user'] == selected]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    for message in temp['message'][temp['value'] == sentiment]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)         
    # Most common 20 entries
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df
