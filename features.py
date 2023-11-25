import pandas as pd
from wordcloud import WordCloud
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
def timeline_monthly(selected, df, sentiment):
    if selected != 'Overall':
        df = df[df['user'] == selected]
    df = df[df['value']==-sentiment]
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

# Wordcloud from words in message.
def wordcloud(selected,df,sentiment):
    f = open('assets/data/hinglish.txt', 'r')
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
    f = open('assets/data/hinglish.txt','r')
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

def member_contribution(df, sentiment):
    df = round((df['user'][df['value']==sentiment].value_counts() / df[df['value']==sentiment].shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return df


def user_sentiment_summary(df):
    # Getting names per sentiment
    positive_users = df['user'][df['value'] == 1].value_counts().head(10)
    negative_users = df['user'][df['value'] == -1].value_counts().head(10)
    neutral_users = df['user'][df['value'] == 0].value_counts().head(10)

    return positive_users, neutral_users, negative_users

# Sentiment analysis function
def get_sentiment(row):
    if row["neutral"] > row["positive"] and row["neutral"] > row["negative"]:
        return 0
    if row["positive"] > row["negative"] and row["positive"] > row["neutral"]:
        return 1
    if row["negative"] >= row["positive"] and row["negative"] >= row["neutral"]:
        return -1

def sentiment_analysis(data):
    sentiments = SentimentIntensityAnalyzer()
    data["positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["message"]]
    data["negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["message"]]
    data["neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["message"]]

    data["value"] = data.apply(lambda row: get_sentiment(row), axis=1)

    return data