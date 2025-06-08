# 📱 Ethiopian Banks Mobile App Sentiment Analysis

This repository contains a complete and structured analysis of user reviews for mobile banking applications from three prominent Ethiopian banks: **Commercial Bank of Ethiopia (CBE)**, **Bank of Abyssinia (BOA)**, and **Dashen Bank**. The project includes sentiment and thematic analysis using Natural Language Processing (NLP), data management using PostgreSQL, insightful visualizations, and actionable recommendations for enhancing user satisfaction and application performance.

---

## 📁 Repository Structure

```plaintext
Eth-Bank-Apps-Sentiment-Analysis/
├── scripts/
│ ├── review_scraper.py
│ ├── review_preprocessor.py
│ ├── sentiment_analysis.py
│ └── thematic_analysis.py
│
├── notebooks/
│ ├── 1-data_collection.ipynb
│ ├── 2-sentiment_thematic_analysis.ipynb
│ ├── 3-database_storage.ipynb
│ └── 4-insights_recommendations.ipynb
│
├── data/
│ ├── reviews_raw.csv
│ ├── reviews_cleaned.csv
│ ├── reviews_with_sentiment.csv
│ └── reviews_analyzed.csv
│
├── database/
│ └── bank_reviews_dump.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Yosi2020/Eth-Bank-Apps-Sentiment-Analysis.git
cd Eth-Bank-Apps-Sentiment-Analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔍 Project Workflow

The project workflow explicitly follows four main analytical phases:

## 📌 Phase 1: Data Collection and Preprocessing

- Scraping user reviews from Google Play Store.
- Cleaning data, removing duplicates, normalizing dates, and preparing CSV files for analysis.

## 📌 Phase 2: Sentiment and Thematic Analysis

- Sentiment classification explicitly using the **DistilBERT** model.
- Keyword extraction using **TF-IDF** with custom-defined stop words.
- Assigning thematic categories explicitly to user reviews.

## 📌 Phase 3: Database Storage

- Storing processed data in **PostgreSQL**, explicitly designed for relational data management.
- Database schema clearly defined for easy data querying.
- Exporting database as an **SQL dump file** (`bank_reviews_dump.sql`).

## 📌 Phase 4: Insights and Recommendations

- Analyzing sentiment distributions, thematic issues, and rating trends.
- Generating explicit **visualizations** for clear stakeholder communication.
- Providing **practical recommendations** based explicitly on identified themes.
- Explicit acknowledgment of **ethical considerations and potential biases**.

---

# 📊 Visualizations & Recommendations

## 📊 Visualizations Included

- **Sentiment distribution** across banks.
- **Ratings distribution analysis** over time.
- **Thematic keyword cloud** visualizations.
- **Comparative analysis** of theme-based issues among banks.

---

## 📝 Recommendations Explicitly by Bank

The analysis clearly identifies each bank's key issue and provides targeted recommendations:

| Bank            | Primary Issue         | Recommendation                                                      |
| --------------- | --------------------- | ------------------------------------------------------------------- |
| **CBE**         | Performance Issues    | Enhance app stability and optimize loading times.                   |
| **Dashen Bank** | Account Access Issues | Streamline login and authentication processes.                      |
| **BOA**         | Customer Support      | Implement responsive support solutions, such as AI-driven chatbots. |

---

## ⚠️ Ethical Considerations

This analysis acknowledges several biases and limitations:

- **Negative Review Bias**: Users experiencing issues tend to leave more reviews, skewing the data negatively.
- **Sampling Bias**: Reviewers may not represent the general user population, affecting generalizability.
- **Data Limitations**: Analysis relies on publicly available data; internal app metrics or user feedback may provide additional valuable insights.

---

## 📥 Database Export (PostgreSQL Dump)

The project includes an SQL dump for quick restoration and access to the database.

**Path to database dump:**

```plaintext
database/bank_reviews_dump.sql
```

---
