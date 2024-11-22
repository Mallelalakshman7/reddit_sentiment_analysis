import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sentiment_analysis import fetch_reddit_data, analyze_sentiment

# CSS for custom styling
st.markdown(
    """
    <style>
    body {
        background-color: #f7f7f9;  /* Light grey background */
        color: #333333;             /* Dark text color */
    }
    .stButton button {
        background-color: #4CAF50;  /* Green button */
        color: white;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎯 Reddit Sentiment Analysis")
st.subheader("🌟 Search for any topic and analyze sentiment of Reddit posts!")

# Input fields
keyword = st.text_input("🔍 Enter a keyword to search:", "")
subreddit = st.text_input("📂 Enter a subreddit (or leave blank for all):", "all")

if st.button("Analyze Sentiment"):
    if keyword.strip() == "":
        st.error("❗ Please enter a keyword to search.")
    else:
        st.info(f"🔄 Searching Reddit for keyword: '{keyword}' in subreddit: '{subreddit}'")
        
        # Fetch data
        with st.spinner("Fetching data..."):
            data = fetch_reddit_data(keyword, subreddit)
        
        if not data:
            st.warning("⚠️ No results found. Try a different keyword or subreddit.")
        else:
            # Analyze sentiment
            results = []
            for post in data:
                sentiment = analyze_sentiment(post["title"] + " " + post["text"])
                results.append({
                    "Title": post["title"],
                    "Sentiment Score": sentiment["compound"],
                    "Positive": sentiment["pos"],
                    "Neutral": sentiment["neu"],
                    "Negative": sentiment["neg"]
                })

            # Create a DataFrame
            df = pd.DataFrame(results)

            # Display DataFrame
            st.write(f"### 🔎 Results for keyword: {keyword}")
            st.dataframe(df)

            # Calculate mean sentiment scores
            mean_scores = df[["Positive", "Neutral", "Negative"]].mean()

            # Create a pie chart
            fig, ax = plt.subplots()
            colors = ['#66c2a5', '#fc8d62', '#8da0cb']  # Custom colors for pie chart
            ax.pie(
                mean_scores,
                labels=mean_scores.index,
                autopct='%1.1f%%',
                startangle=140,
                colors=colors,
                wedgeprops={'edgecolor': 'black', 'linewidth': 1},
            )
            ax.set_title("Sentiment Distribution (Pie Chart)")

            # Display the chart in Streamlit
            st.pyplot(fig)
