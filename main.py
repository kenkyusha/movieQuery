import pdb
import numpy as np
import time
from descriptors import Vectorizer
from searchers import QuerySearch
import sys
import pandas as pd

def query_indexes(search_str, df):
    # runs over the list of strings
    for el in search_str:
        # pdb.set_trace()
        queryFeatures = desc.transform(el)
        # queryFeatures = desc.transform([el.lower()])
        queryFeatures = np.squeeze(queryFeatures.toarray())
        # our results are ordered 
        results = searcher.query(queryFeatures)
        print('search is done for: ', el)
        for j in range(0, 10):
            # grab the result 
            (score, key) = results[j]
            result = df['title'][key]
            #pdb.set_trace()
            print("\t{}. {} : {:.3f}".format(j + 1, result, score))
            #print("\t{}. {} : {:.3f}, rating = {:.2f}".format(j + 1, result, score, df2['rating'][key].mean()))

def query_ranked(search_str, df, df2):
    for el in search_str:
        queryFeatures = desc.transform(el)
        queryFeatures = np.squeeze(queryFeatures.toarray())
        # our results are ordered from smallest difference to biggest!
        results = searcher.query(queryFeatures)
        ranked_idx = {}
        print('search is done for: ', el)
        for j in range(0, 10):
            ranked_idx[results[j][1]] = df2['rating'][results[j][1]].mean()
        ranked_idx = sorted([(v, k) for (k, v) in ranked_idx.items()], reverse=True)
        print("\tMovie Title: \t\t Rating:")
        for j in range(0, 10):
            print("\t{} : \t{:.1f}".format(df['title'][ranked_idx[j][1]], ranked_idx[j][0]))
        # pdb.set_trace()
        # print(ranked_idx)

if __name__ == "__main__":
    # start_time = time.time()

    # path to movie database files (CSV)
    try:
        mpath = sys.argv[1]
    except:
        mpath = 'ml-25m/movies.csv'
    # path to the rankins files
    try:
        rpath = sys.argv[2]
    except:
        rpath = 'ml-25m/ratings.csv'
    
    # load the csv files with PANDAS!
    df = pd.read_csv(mpath, index_col='movieId')
    df2 = pd.read_csv(rpath, index_col='movieId')

    # 1. Initialize the vectorizer
    desc = Vectorizer()
    # 2. Extract strings
    str_lst = desc.extract_strings(df)
    # 3. Extract features
    index = desc.features(str_lst, df)
    print('indexing done')

    # 4. Init Search query
    searcher = QuerySearch(index)
    # 5. Find similar matches!
    search_str = ['apocalypse','terminator', 'star empire', 'New York']

    # Query our strings using the simple query method
    query_indexes(search_str, df)
    
    # Query our string using also the rating
    query_ranked(search_str, df, df2)
    # print('All done, took: ', time.time()-start_time, ' seconds.')
