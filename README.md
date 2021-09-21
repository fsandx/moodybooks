# moodybooks
Exploring segmentation of books by reviews

## visualisation 1
```python
df = pd.read_csv('data/moodywords_result.csv')
df.count()
```

Most occuring words
How many hits? How many will be necessary?
We can improve the number of hits by adding synonyms and exclude the suffixes of the base words. 

![Alt text](screenshots/visualisation1-chart.png?raw=true "Visualisation 1: Most occuring mood word")


## Proportion of occurences to number of words
Add column for wordcount, in result. 
How many words in total (and how mnay occurences) do we need in a review to be useful/reliable

## Percentage of books with occurences
