# Reddit Sentiment Analyzer

A Python web application that analyzes the sentiment of posts from any subreddit.  
The app fetches recent Reddit posts using the Reddit API, performs sentiment analysis on the content, and visualizes the results through an interactive dashboard.

The application is built with Streamlit, making it easy to explore sentiment trends across Reddit communities.

---

## Overview

This tool retrieves recent posts from a specified subreddit and evaluates the sentiment of each post using natural language processing.

The results are categorized into:

- Positive posts
- Negative posts
- Neutral posts

It also calculates summary statistics and displays a visual breakdown of sentiment distribution.

---

## Features

- Fetches recent Reddit posts using the Reddit API
- Performs sentiment analysis on post titles and text
- Calculates sentiment polarity and subjectivity
- Displays summary statistics
- Visualizes sentiment distribution with charts
- Allows users to view posts grouped by sentiment
- Interactive interface built with Streamlit

---

## Tech Stack

- **Python**
- **PRAW** – Reddit API wrapper
- **TextBlob** – Sentiment analysis
- **Streamlit** – Interactive web interface
- **Pandas** – Data handling
- **Datetime** – Timestamp processing

---

## How It Works

1. The user enters a subreddit name.
2. The application fetches recent posts using the Reddit API.
3. Each post's title and text are combined and analyzed using TextBlob.
4. Sentiment polarity and subjectivity scores are calculated.
5. Posts are categorized as:
   - Positive
   - Negative
   - Neutral
6. The application generates summary statistics and visualizations.

---

## Example Output

The dashboard displays:

- Total number of posts analyzed
- Number of positive, negative, and neutral posts
- Average sentiment polarity
- Average subjectivity score
- Bar chart showing sentiment distribution
- Tables listing posts by sentiment category

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jv0019/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Reddit API Setup

To use the Reddit API, you need API credentials.

1. Go to:  
https://www.reddit.com/prefs/apps

2. Create a new application.

3. Set environment variables on your system:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

---

## Running the Application

Start the Streamlit app:

```bash
streamlit run main.py
```

Then open the provided local URL in your browser.

---

## Usage

1. Enter a **subreddit name** (e.g., `technology`, `python`, `news`)
2. Select the **number of posts** to analyze
3. Click **Scrape**
4. View the sentiment summary and charts
5. Select a sentiment category to list corresponding posts

---

## Project Structure

```
reddit-sentiment-analyzer
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Example Use Cases

- Track community sentiment about a topic
- Analyze public opinion on news or products
- Monitor subreddit trends
- Explore sentiment patterns in online discussions

---

## Future Improvements

Potential improvements include:

- Sentiment trend tracking over time
- Word frequency analysis
- Keyword filtering
- More advanced NLP models (e.g., VADER or transformers)
- Export results to CSV
