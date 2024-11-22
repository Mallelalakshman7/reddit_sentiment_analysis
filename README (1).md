
# Reddit Sentiment Analysis with Streamlit

This project is a web application built using **Streamlit** to analyze sentiment from Reddit posts. Users can search for any topic, specify a subreddit, and view sentiment distributions using both a data table and a pie chart.

---

## Features

- Search for Reddit posts based on **keywords** and optional **subreddit**.
- Perform sentiment analysis on posts' titles and content using the **VADER sentiment model**.
- Visualize sentiment results (Positive, Neutral, Negative) in an interactive **pie chart**.
- Display detailed sentiment data in a structured table format.

---

## Project Structure

```
.
├── sentiment_analysis.py       # Script for data fetching and sentiment analysis
├── app.py                      # Main Streamlit app script
├── requirements.txt            # Python dependencies for the project
├── README.md                   # Project documentation
└── .streamlit/                 # Streamlit configuration folder (optional)
```

---

## Prerequisites

1. **Python**: Make sure Python 3.8 or later is installed.
2. **Streamlit**: Used for building the web application.
3. **Matplotlib**: Required for creating the pie chart.

---

## Installation Guide

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/reddit-sentiment-analysis.git
   cd reddit-sentiment-analysis
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate    # On Linux/Mac
   env\Scripts\activate       # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open the application in your browser (usually `http://localhost:8501`).
2. Enter a **keyword** to search and an optional **subreddit**.
3. Click **Analyze Sentiment** to fetch and analyze the Reddit posts.
4. View:
   - Detailed sentiment data in a table.
   - Sentiment distribution as a pie chart.

---

## Example Output

### Input:
- Keyword: `technology`
- Subreddit: `all`

### Output:
- **Table:** Displays each post's title and sentiment scores (Positive, Neutral, Negative).
- **Pie Chart:** Visualizes the overall sentiment distribution.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For creating the web interface.
- **VADER Sentiment Model**: For sentiment analysis.
- **Matplotlib**: For generating pie charts.
- **Pandas**: For handling and processing data.
- **PRAW**: For fetching Reddit posts.

---

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [Streamlit Documentation](https://docs.streamlit.io/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
- [PRAW - Python Reddit API Wrapper](https://praw.readthedocs.io/)

---

## Author

- **Your Name** (Replace with your name or GitHub profile link)
