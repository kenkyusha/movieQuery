import pdb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class Vectorizer:
	def __init__(self):
		# The most simples vectorizer, utilizing the number of occurances
		# This yields use sparse vectors with 0 and 1-s
		# self.desc = CountVectorizer(max_features=2**12)
		# self.desc = CountVectorizer()
		
		# works best with euc
		# self.desc = HashingVectorizer(n_features=2**12)

		# Tfid weights the word counts by a measure of how often they apperas in the text
		self.desc = TfidfVectorizer(max_features=2**12)
		
		pass


	def features(self, str_lst, df):
		# Transform the data, i.e. we pass the list of strings here.
		vect_data = self.desc.fit_transform(str_lst)
		# Build the index dictionary
		index = {}
		# pdb.set_trace()
		# Store the corresponding index and its string in feature format
		for i in range(len(df.index)):
			# Shape the vectors from (1,N) to (N,)
			index[df.index[i]] = np.squeeze(vect_data[i].toarray())

		return index
	
	def transform(self, strng):
		# transform the string into lower case
		return self.desc.transform([strng.lower()])

	def extract_strings(self, df):
		str_lst = []
		for k in df.index:
			pdb.set_trace()
			# Split the movie title strings from year and lower case them
			str_lst.append(df['title'][k].split('(')[0].lower())
		return str_lst