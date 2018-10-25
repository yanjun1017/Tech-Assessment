
import pandas as pd
from sodapy import Socrata
import numpy as np

if __name__ == "__main__":
	

	path = "data/311-2017.csv"
	# Read csv file
	results = pd.read_csv(path, dtype = 'unicode', low_memory = False)
	# Change [results] to DataFrame
	results_df = pd.concat([results])

	"""
	-----------------------------------------------------------------------
	Question:  Consider only the 10 most common overall complaint types.  
	For the 10 most populous zip codes, how many of each of those 10 types were there in 2017?
	""" 
	# Take the top 10 most common complaint types
	# "groupby" clause is used to group the data by the specific type ie. ['complaint_type']
	# "count" is the number of data with the same type 
	# sort_values is use to sort the data by type 'count'
	# "head" is used to get the top elements 
	grouped = results_df.groupby(['Complaint Type']).size().reset_index(name = 'count').sort_values('count', ascending = False).head(10)
	grouped1 = results_df.groupby(['Incident Zip']).size().reset_index(name = 'count').sort_values('count', ascending = False).head(10)
	# Filter out unspecified borough
	results_df = results_df.loc[results_df['Borough'] != 'Unspecified']
	# Loop through the top 10 most common zip code
	# "incident_zip" is one of the top 10 most common zip code
	for incident_zip in grouped1['Incident Zip']:
		# Loop through the top 10 most common complaint types
		# "complaint_type" is one of the top 10 most common complaint types
		for complaint_type in grouped['Complaint Type']:
			# print(complaint_type)
			# "df" contains only data with the same type as "complaint_type"
			df = results_df[(results_df['Incident Zip'] == incident_zip) & (results_df['Complaint Type'] == complaint_type)]
			# This statement is used for grouping the variable with the same complaint type as "complaint_type" 
			# and zip code; and calculate the amount of data that fits the critirie 
			temp = df.groupby(['Incident Zip', 'Complaint Type']).size().reset_index(name = 'count')
			# print(temp)
			if len(temp) != 0:
				print(temp)
	"""
	-----------------------------------------------------------------------
	"""
