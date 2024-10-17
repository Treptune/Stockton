from indicators.sentiment import score_text, get_headers
from statistics import fmean

# note: since sentiment analyzers can't analyze from the perspective
# of only one company so must weight this so it doesn't have too
# much influence over the other indicators.
def media_opinion(ticker: str) -> float:
    headers = get_headers(ticker)
    sentiments = []

    for header in headers:
        sentiments.append(score_text(header))

    return fmean(sentiments), dict(zip(sentiments, headers))
