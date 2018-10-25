import pandas as pd
from sodapy import Socrata
import numpy as np

if __name__ == "__main__":
	

	path = "data/311-2017.csv"
	# Read csv file
	results = pd.read_csv(path, dtype = 'unicode', low_memory = False)
	# Change [results] to DataFrame
	results_df = pd.concat([results])

	# Take the top 10 most common complaint types
	# "groupby" clause is used to group the data by the specific type ie. ['complaint_type']
	# "count" is the number of data with the same type 
	# sort_values is use to sort the data by type 'count'
	# "head" is used to get the top elements 
	grouped = results_df.groupby(['Complaint Type']).size().reset_index(name = 'count').sort_values('count', ascending = False).head(10)
	"""
	-----------------------------------------------------------------------
	Question:  Consider only the 10 most common overall complaint types. For each borough, 
	how many of each of those 10 types were there in 2017?
	""" 
	# Filter out unspecified borough
	results_df = results_df.loc[results_df['Borough'] != 'Unspecified']
	# Loop through the top 10 most common complaint types
	# "complaint_type" is one of the top 10 most common complaint types
	for complaint_type in grouped['Complaint Type']:
		# "df" contains only data with the same type as "complaint_type"
		df = results_df[results_df['Complaint Type'] == complaint_type]
		# This statement is used for grouping the variable with the same complaint type as "complaint_type" 
		# and borough; and calculate the amount of data that fits the critirie 
		temp = df.groupby(['Borough', 'Complaint Type']).size().reset_index(name = 'count')
		if len(temp) != 0:
			print(temp)

	# """
	# -----------------------------------------------------------------------
	# """