# 📰 Stock Price Tracker & News Fetcher

This project fetches stock data and recent news articles for a given company. It checks if the stock price of Tesla Inc (TSLA) has moved significantly (more than 5%) since the previous day, and if so, it fetches the latest news related to Tesla.

## Features:
- **Stock Price Fetching:** Retrieves the stock price for TSLA using the Alpha Vantage API.
- **Price Comparison:** Compares the closing price of today and yesterday to check for significant price changes.
- **News Fetching:** Uses the NewsAPI to fetch the latest news articles related to the company when the stock price moves by more than 5%.

## How It Works:
1. **Fetch Stock Data:** The script queries the Alpha Vantage API for daily stock data for Tesla Inc (TSLA).
2. **Compare Prices:** It compares the stock's closing price from the last two days and calculates the percentage change.
3. **Fetch News:** If the price change is more than 5%, the script fetches the latest 3 news articles related to Tesla.
4. **Display Results:** The stock percentage change is shown along with the corresponding news headlines and brief descriptions.

## 🚀 Tech Stack:
- **Python:** The main programming language used to build this application.
- **Alpha Vantage API:** Used for fetching stock data.
- **NewsAPI:** Fetches the latest news articles based on keywords.
- **Requests:** Used for making HTTP requests to both the Alpha Vantage and News API.

## Installation:
1. Clone this repository:
```bash
git clone https://github.com/yourusername/stock-news-tracker
cd stock-news-tracker
