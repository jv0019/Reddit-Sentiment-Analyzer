import praw
import os
from datetime import datetime, timezone
from textblob import TextBlob
import streamlit as st
import pandas as pd

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

# PRAW
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Function to get and process Reddit posts
def fetch_reddit_posts(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.new(limit=limit)
    posts_data = []

    for post in posts:
        post_data = {
            "title": post.title,
            "url": post.url,
            "created_utc": datetime.fromtimestamp(post.created_utc, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
            "selftext": post.selftext
        }
        posts_data.append(post_data)
    
    return posts_data

# Function to perform sentiment analysis
def analyze_sentiment(posts_data):
    sentiments = []

    for post in posts_data:
        text = post['title'] + " " + post['selftext']
        blob = TextBlob(text)
        sentiment = blob.sentiment
        sentiments.append({
            "title": post['title'],
            "url": post['url'],
            "created_utc": post['created_utc'],
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity,
            "text": text
        })
    
    return sentiments

# Summarize sentiment analysis
def summarize_sentiments(sentiments):
    positive_posts = [post for post in sentiments if post['polarity'] > 0]
    negative_posts = [post for post in sentiments if post['polarity'] < 0]
    neutral_posts = [post for post in sentiments if post['polarity'] == 0]

    summary = {
        "total_posts": len(sentiments),
        "positive_posts": len(positive_posts),
        "negative_posts": len(negative_posts),
        "neutral_posts": len(neutral_posts),
        "average_polarity": round(sum(post['polarity'] for post in sentiments) / len(sentiments) if sentiments else 0,2),
        "average_subjectivity": round(sum(post['subjectivity'] for post in sentiments) / len(sentiments) if sentiments else 0,2),
        "positive_postlist": [post['title'] for post in positive_posts],
        "negative_postlist": [post['title'] for post in negative_posts],
        "neutral_postlist": [post['title'] for post in neutral_posts]
    }

    return summary

st.text_input("Subreddit name", key="name")
x = st.session_state.name
st.number_input("Number of posts", min_value=1, max_value=950, key = "noi")
z = st.session_state.noi
h = ["positive_postlist","negative_postlist","neutral_postlist"]
j = {}
if len(x) == 0:
    st.session_state['subname'] = False
else:
    st.session_state['subname'] = True

def run_analysis():
    st.session_state.posts_data = fetch_reddit_posts(x,z)

    # sentiment analysis
    st.session_state.sentiments = analyze_sentiment(st.session_state.posts_data)

    # Summarize sentiment analysis
    st.session_state.summary = summarize_sentiments(st.session_state.sentiments)

# process Reddit posts
try:
    left, middle, right = st.columns(3)
    y = middle.button(label="scrape",width="stretch",on_click = run_analysis)
    if not st.session_state.subname:
        st.write("subreddit name cannot be empty.")
    elif 'summary' not in st.session_state:
        st.write("Enter a subreddit name and click scrape.")
    else:    
        st.write("Summary of sentiment analysis:\n")
        for k,v in st.session_state.summary.items():
            if k not in h:
                st.write(f"{k}:{v}\n")
            else:
                chart_data = pd.DataFrame(
                    v,
                    columns=[k])
                j[k] = chart_data
                
        l = []
        m = []
        n = ["positive_posts","negative_posts","neutral_posts"]
        for k,v in st.session_state.summary.items():
                if k in n:
                    l.append(k)
                    m.append(v)
        df = pd.DataFrame(
            {
                "Sentiments": l,
                "count": m
            }
            )
        st.bar_chart(df, x="Sentiments", y="count")
        option = st.selectbox(
                "Pick a sentiment to list the posts of:",
                ("Positive", "Negative", "Neutral"),
                index=None,
                placeholder="Select sentiment...",
                )
        if option == "Positive":
            st.table(j["positive_postlist"])
        elif option == "Negative":
            st.table(j["negative_postlist"])
        elif option == "Neutral":
            st.table(j["neutral_postlist"])   
                   
except Exception as e:
    st.write(f"An error occurred: {e}")

