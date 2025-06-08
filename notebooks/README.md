# 📘 Notebooks

This folder contains Jupyter notebooks explicitly designed for the **Ethiopian Banks Mobile App Sentiment Analysis** project. Each notebook covers a clearly defined analytical task.

---

## 📌 Contents:

| Notebook Name                         | Description (explicitly)                                                                                                            |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `1-data_collection.ipynb`             | Explicitly details data scraping from Google Play and preprocessing steps including cleaning, normalization, and CSV export.        |
| `2-sentiment_thematic_analysis.ipynb` | Combines sentiment analysis using DistilBERT with thematic analysis and keyword extraction explicitly performed.                    |
| `3-database_storage.ipynb`            | Explicitly shows how the cleaned data is stored into PostgreSQL database directly from the notebook.                                |
| `4-insights_recommendations.ipynb`    | Explicitly generates visualizations, derives insights, recommendations, and notes ethical considerations clearly based on analysis. |

---

## ✅ Recommended Execution Order (Explicitly):

1. **Data Collection** (`1-data_collection.ipynb`)
2. **Sentiment & Thematic Analysis** (`2-sentiment_thematic_analysis.ipynb`)
3. **Database Storage** (`3-database_storage.ipynb`)
4. **Insights & Recommendations** (`4-insights_recommendations.ipynb`)

---

## 📊 Visualizations Included:

- Sentiment Distribution explicitly per bank
- Ratings Distribution explicitly analyzed
- Word Clouds explicitly based on themes
- Theme-based Issues Comparison explicitly per bank

---

## 🚨 Ethical Considerations Explicitly Stated:

- Negative review bias explicitly acknowledged (users experiencing issues are more likely to leave reviews).
- Sampling bias explicitly noted (reviewers may differ significantly from typical app users).

---

## 📂 Folder Structure Explicitly Described:

notebooks/
├── 1-data_collection.ipynb
├── 2-sentiment_thematic_analysis.ipynb
├── 3-database_storage.ipynb
└── 4-insights_recommendations.ipynb

---

## 📖 Additional Resources:

- [Google Play Scraper Documentation](https://pypi.org/project/google-play-scraper/)
- [DistilBERT Sentiment Analysis Model](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---
