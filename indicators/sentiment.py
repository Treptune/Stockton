from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

analyzer = SentimentIntensityAnalyzer()

def score_text(text: str) -> float:
    avg = (score_text_tb(text) + score_text_vader(text)) / 2
    return avg


def score_text_vader(text: str) -> float:
    vs = analyzer.polarity_scores(text)
    return vs.get('compound')

def score_text_tb(text: str) -> float:
    text = TextBlob(text)
    analysis = text.sentiment
    normalized_polarity = (analysis.polarity + 1) / 2
    score = normalized_polarity*0.7 + analysis.subjectivity*0.3
    return score

