# movieQuery

## requirements:
pip install pandas
pip install scikit-learn
pip install scipy
pip install numpy

## data
> wget http://files.grouplens.org/datasets/movielens/ml-25m.zip

> unzip -a ml-25m.zip

or 

> chmod +x get_data.sh

> ./get_data.sh

## scripts
* main.py - python3 main.py #path2movies.csv #path2ratingscsv
* descriptors.py - the functionality to transform the strings into feature vectors (builds index with features)
* searchers.py - the functionality to query/search among the entries of the indexes (calculates differences)

## intro

Firstly, we have movie data base and we would like to build a search engine for finding movies in a movie database. The search function is implemented such that it can be queryed using a string of characters, and returns top 10 hits sorted in order of relevance. This search engine only allow querying by title for simplicity.
This is implemented in the function *query_indexes*.

Secondly, we want to see relevance of the movies, this is implemented by function *query_ranked*, which takes into account the average rating of the movie.

## issues

* some movies have only few ratings, so perhaps it is more useful to use the occurance weighted by the score.
