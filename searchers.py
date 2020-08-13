import numpy as np
from scipy import spatial
import pdb

class QuerySearch:
    def __init__(self, index):
        ''' store the image dictionary (key, feature)'''
        self.index = index
    def query(self, feature):
        # initialize our dictionary of results
        ''' We loop over the indexed image features and 
            calculate the distance measure between the features'''
        results = {}
        # loop over the index
        for (k, features) in self.index.items():
            # chi-squared distance widely used in CV problems
            d = self.dist_mes(features, feature, 'euc')
            # the key is image ID and the d is its distance to the feature
            results[k] = d

        # sort the distance based on the similarity
        results = sorted([(v, k) for (k, v) in results.items()])
        return results

    def dist_mes(self, x, y, mes = 'euc', eps = 1e-10):
        # pdb.set_trace()
        ''' euc - euclediean distance
            chi - chi squared distance
            cos - cosine distance
            man - manhattan distance'''
        if mes == 'euc':
            return np.linalg.norm(x-y)
        if mes == 'chi':
            chi = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)  
                          for (a, b) in zip(x, y)])
            return chi
        if mes == 'cos':
            #return 1 - spatial.distance.cosine(x, y)
            return spatial.distance.cosine(x, y)
        if mes == 'man':
            return spatial.distance.cityblock(x,y)