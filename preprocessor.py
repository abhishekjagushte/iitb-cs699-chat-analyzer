import re
import pandas as pd

def features_extract(df):
    df['only_date'] = df['date'].dt.date # Extract date
    df['year'] = df['date'].dt.year # Extract year
    df['month_num'] = df['date'].dt.month # Extract month
    df['month'] = df['date'].dt.month_name() # Extract month name
    df['day'] = df['date'].dt.day # Extract day
    df['day_name'] = df['date'].dt.day_name() # Extract day name
    df['hour'] = df['date'].dt.hour # Extract hour
    df['minute'] = df['date'].dt.minute # Extract minute
    df = df[df['user'] != 'group_notification'] # Remove entries having user as group_notification
    return df

def seperator(df):
    names = []
    msg = []
    for message in df['user_message']:
        # Split message based on '([\w\W]+?):\s'
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]: 
            # User name
            names.append(entry[1])
            # Only message
            msg.append(" ".join(entry[2:]))
        else:
            # Adding group notifications
            names.append('group_notification')
            # Null value
            msg.append(entry[0])
    return names, msg

def preprocessing(data):
   # Regular expression
    regular_expression = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}'
    # Split text file into msg & dates based on above regular_expression.
    msg = re.split(regular_expression, data)[1:]
    dates = re.findall(regular_expression, data)
    # Creating dataframe
    df = pd.DataFrame({'user_message': msg, 'message_date': dates})
    # convert dates 'type'
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Creating new columns
    names, msg = seperator(df)
    df['user'] = names
    df['message'] = msg
    df.drop(columns=['user_message'], inplace=True)
    df = features_extract(df)
    return df
    
