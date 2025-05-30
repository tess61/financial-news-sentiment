# 📈 Financial Solutions – Sentiment and Technical Analysis Project

This project analyzes the relationship between **financial news sentiment** and **stock price movements** for major tech companies (AAPL, AMZN, GOOG, META, MSFT, NVDA, TSLA).  
It combines **Natural Language Processing (NLP)** for sentiment scoring and **technical analysis** using financial indicators.

> This repository contains work completed for **Task 1 (EDA & Sentiment Analysis)** and **Task 2 (Technical Analysis)** of a larger multi-step financial data pipeline.

---

## 📌 Project Structure

```bash
    solar-challenge-week1/
├── data/
│ ├── news_data/ # Raw and processed news data
│ └── yfinance_data/ # Historical stock price CSVs
│
├── notebooks/
│ ├── eda.ipynb # Task 1 notebook
│ └── task2_technical_analysis.ipynb# Task 2 notebook
│
├── scripts/
│ └── technical_analysis.py # Technical indicator functions
│
├── requirements.txt
└── README.md
```


---

## ✅ Tasks Overview

### 🔍 Task 1: Exploratory Data Analysis & Sentiment Scoring

**Goals:**
- Clean and prepare financial news headline data
- Apply sentiment analysis (TextBlob)
- Aggregate sentiment scores per stock and date

**Tools Used:**
- `pandas`, `nltk`, `TextBlob`, `matplotlib`, `seaborn`

**Output:**
- `news_sentiment_processed.csv` with `stock`, `date`, `sentiment`

---

### 📊 Task 2: Technical Analysis of Stock Prices

**Goals:**
- Analyze historical stock data
- Compute technical indicators (SMA, RSI, MACD)
- Visualize indicator trends

**Tools Used:**
- `pandas`, `yfinance`, `TA-Lib`, `matplotlib`

**Output:**
- Visual plots and computed features in `task2_technical_analysis.ipynb`

---

## ⚙️ How to Reproduce

### 📁 1. Clone the Repository

```bash
git clone https://github.com/tess61/financial-news-sentiment.git
cd financial-news-sentiment
```

### 🐍 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 📦 3. Install Dependencies
✅ TA-Lib can be tricky to install. See the note below.
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
⚠️ TA-Lib Installation Note
If you encounter issues installing TA-Lib using pip, download the appropriate .whl file from Gohlke’s repository and install it manually:
```bash 
pip install TA_Lib‑0.4.0‑cp311‑cp311‑win_amd64.whl  # Use the wheel matching your Python version
```

### ▶️ 4. Run the Notebooks

#### Task 1 – Sentiment Analysis

```bash
    jupyter notebook notebooks/eda_sentiment.ipynb
```

#### Task 2 – Technical Indicators

```bash
    jupyter notebook notebooks/task2_technical_analysis.ipynb
```

## 🧪 Test Files
    
    Sentiment Output: data/FSPID_processed.csv
    Historical Stock Data: data/yfinance_data/*.csv

## 📌 KPI Achievements (Tasks 1 & 2)
KPI	Description	Status
✅ Workflow Discipline	Git branches, PRs, commits	                ✔️ Completed
✅ Sentiment Accuracy	Applied and visualized TextBlob scoring	    ✔️ Completed
✅ Technical Proficiency	Integrated and applied TA-Lib indicators	✔️ Completed
✅ Problem Solving	Resolved complex library installation issues	✔️ Completed
✅ Modularity	Used scripts and separate notebooks	                ✔️ Completed

## 🚧 Challenges & Solutions
        Issue	                            Resolution
❌ TA-Lib installation error	               ✅ Solved using Christoph Gohlke’s precompiled binary
❌ ipython incompatibility with Python 3.13	✅ Fixed by upgrading all related Jupyter dependencies
