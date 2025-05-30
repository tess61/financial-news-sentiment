import pandas as pd
from textblob import TextBlob

def compute_sentiment(text):
    return TextBlob(text).sentiment.polarity

def prepare_news_data(news_df):
    news_df['date'] = pd.to_datetime(news_df['date']).dt.date
    news_df['sentiment'] = news_df['headline'].apply(compute_sentiment)
    daily_sentiment = news_df.groupby(['stock', 'date'])['sentiment'].mean().reset_index()
    return daily_sentiment

def prepare_stock_data(stock_df):
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
    stock_df['Return'] = stock_df['Close'].pct_change()
    return stock_df[['Date', 'Return']]

def merge_data(news_sentiment_df, stock_returns_df, stock_symbol):
    stock_returns_df = stock_returns_df.rename(columns={'Date': 'date'})
    merged_df = pd.merge(news_sentiment_df[news_sentiment_df['stock'] == stock_symbol],
                         stock_returns_df, on='date', how='inner')
    return merged_df

def compute_correlation(merged_df):
    return merged_df['sentiment'].corr(merged_df['Return'])
