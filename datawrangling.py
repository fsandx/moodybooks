# Run in IPython console:
# import datawrangling as dw
# dw.WordCounter()

import os
import pandas as pd

REVIEWS_PATH = 'data/reviews.json'
RESULT_PATH = 'data/moodywords_result.csv'

WORDS_HAPPY = ['happy','playful', 'aroused', 'cheeky', 'content', 'free', 'joyful', 'interested', 'curious', 'inquisitive', 'proud', 'successful', 'confident', 'accepted', 'respected', 'valued', 'powerful', 'courageous', 'creative', 'peaceful', 'loving', 'thankful', 'trusting', 'sensitive', 'intimate', 'optimistic', 'hopeful', 'inspired']
WORDS_SAD = ['sad', 'lonely', 'isolated', 'abandoned', 'vulnerable', 'victimized', 'fragile', 'despair', 'grief', 'powerlesss', 'hurt', 'embarrassed', 'depressed', 'inferior', 'empty', 'guilty', 'ashamed', 'remorseful']
WORDS_DISGUSTED = ['disgusted', 'disapproving', 'judgemental', 'disappointed', 'appalled', 'revolted', 'awful', 'nauseated', 'detestable', 'repelled', 'hesitant', 'angry']
WORDS_ANGRY = ['let down', 'betrayed', 'humiliated', 'disrespected', 'ridiculed', 'bitter', 'indignant', 'violated', 'mad', 'furious', 'jealous', 'aggressive', 'provoked', 'hostile', 'frustrated', 'infuriated', 'annoyed', 'distant', 'withdrawn', 'numb', 'critical', 'skeptical', 'dismissive']
WORDS_FEARFUL = ['fearful', 'scared', 'helpless', 'frightened', 'anxious', 'overwhelmed', 'worried', 'insecure', 'inadequate', 'inferior', 'weak', 'worthless', 'insignificant', 'rejected', 'excluded', 'persecuted', 'threatened', 'nervous', 'exposed']
WORDS_BAD = ["bad","bored","busy","stressed","tired","indifferent","apathetic","pressured","rushed","out of control","sleepy","unfocused"]
WORDS_SURPRISED = ["surprised","startled","confused","amazed","excited","shocked","dismayed","disillusioned","perplexed","astonished",'awe',"eager","energetic"]

class WordCounter:

    def __init__(self):
        self.loadData()
        self.countWords()

    def loadData(self):
        self.reviews = pd.read_json(REVIEWS_PATH)

    def countWords(self):
        #Create a single list of all words
        words = [WORDS_HAPPY, WORDS_SAD,WORDS_DISGUSTED, WORDS_ANGRY, WORDS_FEARFUL, WORDS_BAD, WORDS_SURPRISED]

        #Creating a list of all the first words, which will be the fieldnames
        word_fields = [words[0][0], words[1][0],words[2][0], words[3][0], words[4][0], words[5][0], words[6][0]]
        
        #initializing a pandas dataframe
        self.counted = pd.DataFrame(columns = word_fields )
        
        # Running through all the reviews
        for index, row in self.reviews.iterrows():
 
            #create a list of all words in the review
            rwords = row['text'].split()

            # initialize the data
            data = [str(row['number']), str(len(rwords)) ]

            # initialize additional fields
            columns = ['id', 'words']

            # find occurences of "moody" words in the review
            for wlist in words:
                count = 0
                for w in wlist:
                    # counting occurences of the word
                    count = count + rwords.count(w)
                #adding the number of hits
                data.append(str(count))
                columns.append(wlist[0])

            # Creating a Pandas Serie (record/row) of the data
            s = pd.Series(data=data, index=columns)
            
            # Appending the review record to the dataset
            self.counted = self.counted.append(s, ignore_index=True)

        # debug
        print(self.counted)
        
        # Writing the dataset to a csv file
        self.counted.to_csv(RESULT_PATH)

                