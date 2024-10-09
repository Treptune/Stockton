from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

analyzer = SentimentIntensityAnalyzer()

def score_text_vader(text: str) -> float:
    vs = analyzer.polarity_scores(text)
    return vs.get('compound')

def score_text_tb(text: str) -> float:
    text = TextBlob(text)
    return text.sentiment

