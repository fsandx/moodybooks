# moodybooks
Exploring a moody classification of books, by analyzing reviews.
BookSpider.py - used for collecting 

## Visualisation 1: Most occuring mood word
```python
df = pd.read_csv('data/moodywords_result.csv')
df.count()
```
How many occurences is necessary for a book to be qualified for the mood label?
The number of hits can be increased by adding **synonyms** and **exclude suffixes** from the word base. 

![Alt text](screenshots/visualisation1-chart.png?raw=true "Visualisation 1: Most occuring mood word")

[Code for the graph](visualisation1.ipynb) with [Jupyter](https://jupyter.readthedocs.io), by the assistance from [Seaborn](https://seaborn.pydata.org/).

## Visualisation 2: Relation between review length and number of word hits
A linear regression plot, showing how a length of a review text effects the number of occurences of moody word.
The greater the length the larger the variety. 
How many words in total (and how many occurences) do we need in a review for the classification to be useful/relevant?
![Alt text](screenshots/visualisation2-chart.png?raw=true "Visualisation 2: Relation between review length and number of word hits")

[Code for the graph](visualisation2.ipynb) with [Jupyter](https://jupyter.readthedocs.io), by the assistance from [Seaborn](https://seaborn.pydata.org/).


## Visualisation 3: List of top moody books
![Alt text](screenshots/visualisation3-list.png?raw=true "Visualisation 3: List of top moody books")
![Alt text](screenshots/visualisation3.png?raw=true "Visualisation 3: Plotted titles")

## Visualisation 4: List books in each mood genre


## Data wrangling
The 100 words I am using is originally arranged as a wheel with three layers.
The inner core layer consists of 7 parent words, which all the other words are children, or grandchildren of.
The hierarchical model suggest me to use json instead of csv for an accurate representation of the relationships.
But I have choosen to simplify the model, and only register the occurences of any word, in one of the seven parent groups, which means
I can stick to 2D csv data source, with the 7 parents as columns and the number of "hits" for each review, as rows.   


# Context
Counting the occurence of words doesn't say anything about the context. For example: we count the word "joy" in the sentence: "This is not joy".

# Naive Bayesian applied to synonyms
The research project that came up with the list of words was done by eliminating words that was semantically close to each other. 
We could use a naive bayesian approach to examine how probabible it is that people would classify the word as a synonym to one of our predefined labels rather than to any else. 

## Other data sources
- what does normal readers write about the book, analyze comments in social media.
- If we only use one single review as a source for the calssification it becomes a classification of the review, rather than the book. 
- But that might be interesting for a literary magazine / website.
- It can also be interesting to see how much a particular review differes from the clasification of the text in the actual book.

## Other parameters than nr of word occurences that can help determine the classification
- popularity among people with certain demographic qualities
- written by an author that often writes in the space
- quoted and referenced to by those with an over weighing interest in that particular mood.
- book is more read/bought (and borrowed from libraries) during special times of the year.

## Conclusion
- IWith the respect to Moddy Books's business model, I would recommend one, or borth of the below paths: 
1) Increase hits by adding synonyms and exlude suffixes, additional fetch comments about the book from social media.
2) Examine the best way to implement a rating system where the above used word classification can be used.