import os
import pandas as pd
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEWS_PATH = 'data/reviews.json'
WORDS_PATH = 'data/moodywords.csv'
RESULT_PATH = 'data/moodywords_result.csv'

# Run in IPython console:
# import datawrangling as dw
# dw.WordCounter()

class WordCounter:

    def __init__(self):
        self.loadData()
        self.countWords()

    def loadData(self):
        self.reviews = pd.read_json(REVIEWS_PATH)
        self.words = pd.read_csv(WORDS_PATH)

    def countWords(self):
        word_fields = list(self.words)
        self.counted = pd.DataFrame(columns = word_fields )
        for index, row in self.reviews.iterrows():
            rwords = row['text'].split()
            t = row['title']
            bid = row['number']
            data = [str(bid)]
            columns = ['Book Id']
            for mw in self.words:
                c = rwords.count(mw)
                if (c > 0):
                    data.append(str(c))
                    columns.append(mw)

            s = pd.Series(data=data, index=columns)
            self.counted = self.counted.append(s, ignore_index=True, verify_integrity=False, sort=None)

        print(self.counted)
        self.counted.to_csv(RESULT_PATH)

                