# 📊 Reddit Sentiment Analyzer

An interactive web application that analyzes sentiment across Reddit communities in real time.

Built with **Python**, **Streamlit**, **PRAW**, and **TextBlob**, the application retrieves live Reddit posts, performs natural language sentiment analysis, and visualizes community sentiment through an intuitive dashboard.

🚀 **Live Demo:** *[Reddit-Sentiment-Analyzer](https://reddit-sentiment-1.streamlit.app/)*

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Reddit API](https://img.shields.io/badge/API-Reddit-orange)
![NLP](https://img.shields.io/badge/NLP-Sentiment_Analysis-green)

---

## 🚀 Overview

Reddit hosts millions of discussions spanning technology, finance, gaming, politics, business, and countless other topics.

This application enables users to:

* Analyze sentiment within any subreddit
* Measure community positivity or negativity
* Explore discussion trends
* Visualize sentiment distribution
* Examine individual posts by sentiment category

The system fetches live Reddit content, performs sentiment analysis using natural language processing techniques, and presents the results through an interactive dashboard.

---

## ✨ Features

### 🔴 Live Reddit Data

* Fetches recent posts from any public subreddit
* Connects directly to the Reddit API using PRAW
* Supports configurable post limits

### 🧠 Sentiment Analysis

* Analyzes titles and post content
* Calculates sentiment polarity scores
* Calculates subjectivity scores
* Classifies posts into:

  * Positive
  * Negative
  * Neutral

### 📊 Interactive Dashboard

* Real-time sentiment statistics
* Sentiment distribution visualizations
* Community-level sentiment overview
* Interactive filtering and exploration

### 📈 Data Insights

* Total posts analyzed
* Average sentiment score
* Average subjectivity score
* Positive/Negative/Neutral breakdown

### 📋 Post-Level Analysis

* Browse posts grouped by sentiment
* Identify highly positive discussions
* Discover controversial or negative topics
* Explore subreddit mood patterns

---

## 🎯 Business Value

This project demonstrates how publicly available social media data can be transformed into actionable insights.

Potential applications include:

* Brand sentiment monitoring
* Market research
* Community engagement analysis
* Product feedback tracking
* Public opinion analysis
* Trend monitoring
* Social listening

---

## 🏗 System Architecture

```text id="u5ayqf"
User
 │
 ▼
Streamlit Dashboard
 │
 ▼
Reddit API (PRAW)
 │
 ▼
Post Collection
 │
 ▼
TextBlob NLP Engine
 │
 ▼
Sentiment Classification
 │
 ▼
Visual Analytics Dashboard
```

---

## 🛠 Technology Stack

| Component          | Technology       |
| ------------------ | ---------------- |
| Frontend           | Streamlit        |
| Language           | Python           |
| Reddit Integration | PRAW             |
| NLP                | TextBlob         |
| Data Processing    | Pandas           |
| Date Handling      | Datetime         |
| Visualization      | Streamlit Charts |

---

## ⚙️ Installation

### Clone Repository

```bash id="q73vbp"
git clone https://github.com/jv0019/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```

### Install Dependencies

```bash id="m7q2qq"
pip install -r requirements.txt
```

---

## 🔑 Reddit API Configuration

To access Reddit data, create API credentials.

### Step 1: Create a Reddit App

Visit:

```text id="7rq37h"
https://www.reddit.com/prefs/apps
```

Create a new application and note:

* Client ID
* Client Secret
* User Agent

### Step 2: Configure Environment Variables

```env id="0rn45l"
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

---

## ▶️ Running the Application

Launch the Streamlit application:

```bash id="wfrg68"
streamlit run main.py
```

The application will open in your browser automatically.

Default local address:

```text id="2lbttq"
http://localhost:8501
```

---

## 📖 Usage

### Analyze a Subreddit

1. Enter a subreddit name
2. Select the number of posts to analyze
3. Click **Analyze**
4. Review sentiment statistics
5. Explore visualizations
6. Inspect posts by sentiment category

### Example Subreddits

```text id="42i1ph"
technology
python
news
datascience
artificial
machinelearning
stocks
worldnews
```

---

## 📊 Metrics Generated

### Sentiment Metrics

| Metric             | Description                             |
| ------------------ | --------------------------------------- |
| Polarity           | Measures positive vs negative sentiment |
| Subjectivity       | Measures opinion vs factual content     |
| Sentiment Category | Positive, Negative, or Neutral          |

### Dashboard Statistics

* Total Posts Analyzed
* Positive Post Count
* Negative Post Count
* Neutral Post Count
* Average Polarity
* Average Subjectivity

---

## 📂 Project Structure

```text id="g4xh8k"
reddit-sentiment-analyzer/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 💡 Example Use Cases

### Business & Marketing

* Brand monitoring
* Product launch feedback
* Competitor sentiment tracking

### Research

* Social media analytics
* Community behavior analysis
* Trend detection

### Personal Exploration

* Monitor favorite communities
* Compare subreddit sentiment
* Discover discussion trends

---

## 🚀 Future Improvements

Planned enhancements:

* [ ] Sentiment tracking over time
* [ ] Word frequency analysis
* [ ] Keyword filtering
* [ ] Topic modeling
* [ ] Export results to CSV
* [ ] Historical subreddit comparison
* [ ] VADER sentiment analysis
* [ ] Transformer-based NLP models
* [ ] AI-generated sentiment summaries

---

## 📜 License

MIT License

---

## 👤 Author

**Jivitesh Sachdev**

Software Development • Data Analytics • NLP • AI Applications

GitHub: https://github.com/jv0019

---

### Keywords

Python • NLP • Sentiment Analysis • Reddit API • Streamlit • Data Analytics • Social Media Analytics • TextBlob • Data Visualization • Natural Language Processing • Dashboard Development
