## Install all required libraries
    > make install

## To format code:

    > make format
## To see sentiments of top 10 articles
    > make run

1. The projects starts with the main.py file, which extracts all the
data from the provided link. The extract_pages.py uses urlib3 and
beautifulSoup to extract the data.
2. The next step is to preprocess the data
3. After pre-processing, the data is then fed to transformers model to predict the sentiment.
4. The results are then visualized in the plotly.