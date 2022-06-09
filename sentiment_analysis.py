import re
from typing import List, Dict, Any
from transformers import pipeline
import plotly.express as px
import pandas as pd


def preprocess_punctuations(sentence: str) -> str:
    sentence = re.sub(r"[()~!^,?.\'$]", "", sentence)
    sentence = sentence.replace("\xad", "")
    return sentence


def predict_sentiment(texts: List[str]) -> List[Dict[str, Any]]:
    sentiment_pipeline = pipeline("sentiment-analysis")
    sentiments = sentiment_pipeline(texts, truncation="only_first")
    return sentiments


def visualize_results_and_save(sentiments: pd.DataFrame) -> str:
    fig = px.histogram(sentiments, x="sentiment")
    fig.show()
    fig.write_image("screenshot.png")
    return "screenshot.png"
