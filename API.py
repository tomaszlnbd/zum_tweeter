import tweepy
import pandas as pd

if __name__ == '__main__':
    client = tweepy.Client(
        bearer_token='XYZ',
        consumer_key='XYZ',
        consumer_secret='XYZ',
        access_token='XYZ',
        access_token_secret='XYZ',
        wait_on_rate_limit=True)

    path = "pl_covid_tweets_clean.txt"
    df = pd.read_csv(path, delim_whitespace=True)
    print(df.head())
    df = df["tweet_id"]
    print(df.head())

    all_tweets = []
    tweet_count = df.size
    try:
        for i in range((tweet_count // 100) + 1):
            end_loc = min((i + 1) * 100, tweet_count)
            id = df[i * 100:end_loc].values.tolist()
            tweets = client.get_tweets(id)
            all_tweets.extend(tweets)
            print("POBRANO TWEETOW:")
            print((i + 1) * 100)
    except Exception as e:
        print(e)
    finally:
        with open('alltweetsPL.txt', 'w') as f:
            for item in all_tweets:
                f.write("%s\n" % item)
        f.close()