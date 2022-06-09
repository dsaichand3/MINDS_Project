import pandas as pd
from extract_pages import extract_data_from_aljazeera
from sentiment_analysis import (
    preprocess_punctuations,
    predict_sentiment,
    visualize_results_and_save,
)


def main():
    texts = extract_data_from_aljazeera(n=10)
    headings, content = [], []
    for text in texts:
        headings.append(preprocess_punctuations(text[0]))
        content.append(preprocess_punctuations(text[1]))

    sentiments = predict_sentiment(content)
    ans = []
    for heading, sentiment in zip(headings, sentiments):
        ans.append([heading, sentiment["label"], sentiment["score"]])
    return pd.DataFrame(ans, columns=["heading", "sentiment", "score"])


if __name__ == "__main__":
    result = main()
    print(result)

    path = visualize_results_and_save(result)
    print(f"Screenshot saved as {path}")
