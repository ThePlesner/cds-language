import os
import spacy
nlp = spacy.load("en_core_web_sm")
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from spacytextblob.spacytextblob import SpacyTextBlob

million_headlines_file = os.path.join('..', 'assignment_data', 'abcnews-date-text.csv')

data = pd.read_csv(million_headlines_file)

spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

polarity_scores = []
counter = 0;

print(data.sample(5))

for headline_doc in nlp.pipe(data["headline_text"], batch_size=1000):
    for headline in headline_doc.sents:
        score = headline._.sentiment.polarity
        polarity_scores.append(score)
        print(f"Appnending sentence: {headline} with score {score}")
        counter += 1
    print(f"{counter} sentences so far...")

    
print(polarity_scores[1:100])