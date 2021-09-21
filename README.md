# moodybooks
Exploring segmentation of books by reviews

## Visualisation 1: Most occuring mood word
```python
df = pd.read_csv('data/moodywords_result.csv')
df.count()
```
How many occurences is necessary for a book to be qualified for the mood label?
The number of hits can be increased by adding **synonyms** and **exclude suffixes** from the word base. 

![Alt text](screenshots/visualisation1-chart.png?raw=true "Visualisation 1: Most occuring mood word")

[Code for the graph](visualisation1.ipynb) with [Jupyter](https://jupyter.readthedocs.io), by the assistance from [Seaborn](https://seaborn.pydata.org/).

## Visualisation 2: Proportion of occurences to number of words
Add column for wordcount, in result. 
How many words in total (and how many occurences) do we need in a review to be useful/reliable

## Visualisation 3: Percentage of books with occurences
