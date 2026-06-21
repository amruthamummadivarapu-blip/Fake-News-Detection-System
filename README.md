# Fake News Detection System

A Machine Learning-based web application that predicts whether a news article is **Real News** or **Fake News**. The project uses Natural Language Processing (NLP) techniques to clean and process news text before making predictions with a trained machine learning model.

##  Features

* Detects fake and real news articles
* User-friendly Streamlit interface
* Automatic text preprocessing and cleaning
* Fast and accurate predictions
* Supports long news content

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pickle
* Regular Expressions (Regex)
* Natural Language Processing (NLP)

## How It Works

1. User enters a news article.
2. The text is cleaned and preprocessed.
3. The vectorizer converts text into numerical features.
4. The trained model analyzes the input.
5. The application displays whether the news is **Real** or **Fake**.

## Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Enhancements

* Improve model accuracy with advanced NLP models
* Add confidence score for predictions
* Support multiple languages
* Deploy the application online
