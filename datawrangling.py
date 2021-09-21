import os
import pandas as pd

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
        
        #Creating a list of all the moody words, which is the the fieldnames
        word_fields = list(self.words)
        
        #initializing a pandas dataframe
        self.counted = pd.DataFrame(columns = word_fields )
        
        # Running through all the reviews
        for index, row in self.reviews.iterrows():
 
            #create a list of all words in the review
            rwords = row['text'].split()

            # initialize the data
            data = [str(row['number']), str(len(rwords)) ]

            # initialize the data fields

            columns = ['Book Id', 'Text Size']
            
            # find occurences of "moody" words in the review
            for mw in self.words:
                
                # counting occurences of the word
                c = rwords.count(mw)
                
                # only adding the number of hits if they are more than 0
                if (c > 0):
                    data.append(str(c))
                    columns.append(mw)

            # Creating a Pandas Serie (record/row) of the data
            s = pd.Series(data=data, index=columns)
            
            # Appending the review record to the dataset
            self.counted = self.counted.append(s, ignore_index=True)

        # debug
        print(self.counted)
        
        # Writing the dataset to a csv file
        self.counted.to_csv(RESULT_PATH)

                